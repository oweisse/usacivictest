document.addEventListener('DOMContentLoaded', () => {
    // State
    const state = {
        questions: [],
        currentIndex: 0,
        isShuffled: false,

        showingAnswer: false,
        alwaysShow: false,   // New flag
        alwaysExpand: false, // New flag
        filteredIndices: [] // Stores indices of questions to show (based on shuffle/filter)
    };

    // Elements
    const els = {
        questionText: document.getElementById('question-text'),
        cardContent: document.querySelector('.card-content'),
        answersList: document.getElementById('answers-list'),
        answerSection: document.getElementById('answer-section'),
        questionCounter: document.getElementById('question-counter'),
        badge6520: document.getElementById('badge-65-20'),
        progressContainer: document.querySelector('.progress-container'), // Added container
        progressBar: document.getElementById('progress-bar'),

        btnShowAnswer: document.getElementById('show-answer-btn'),
        navGroup: document.getElementById('nav-group'),
        btnNext: document.getElementById('next-btn'),
        btnPrevMain: document.getElementById('prev-main-btn'), // New button in card
        btnPrev: document.getElementById('prev-btn'),
        btnSkip: document.getElementById('skip-btn'),


        btnShuffle: document.getElementById('shuffle-btn'),
        btnAlwaysShow: document.getElementById('always-show-btn'),     // New
        btnAlwaysExpand: document.getElementById('always-expand-btn'), // New

        jumpInput: document.getElementById('jump-input'),
        jumpBtn: document.getElementById('jump-btn')
    };

    // Load Data
    Promise.all([
        fetch('questions.json?v=' + Date.now()).then(res => res.json())
    ])
        .then(([questionsData]) => {
            state.questions = questionsData;
            initSequence();

            // Restore state?
            const savedId = localStorage.getItem('civics_last_question_id');
            if (savedId) {
                // Find index of this ID in current sequence
                const targetId = parseInt(savedId);
                const foundIndex = state.filteredIndices.findIndex(idx => state.questions[idx].id === targetId);
                if (foundIndex !== -1) {
                    state.currentIndex = foundIndex;
                }
            }

            // Restore toggles
            state.alwaysShow = localStorage.getItem('civics_always_show') === 'true';
            state.alwaysExpand = localStorage.getItem('civics_always_expand') === 'true';

            // Set initial UI state for buttons
            els.btnAlwaysShow.setAttribute('aria-pressed', state.alwaysShow);
            if (state.alwaysShow) els.btnAlwaysShow.classList.add('active');

            els.btnAlwaysExpand.setAttribute('aria-pressed', state.alwaysExpand);
            if (state.alwaysExpand) els.btnAlwaysExpand.classList.add('active');

            renderQuestion();
        })
        .catch(err => {
            console.error(err);
            els.questionText.textContent = "Error loading questions.";
        });

    // Core Logic
    function initSequence() {
        // Create base sequence [0, 1, ..., N]
        let indices = state.questions.map((_, i) => i);



        // Shuffle?
        if (state.isShuffled) {
            shuffleArray(indices);
        }

        state.filteredIndices = indices;

        // Reset valid index if out of bounds
        if (state.currentIndex >= state.filteredIndices.length) {
            state.currentIndex = 0;
        }
    }

    function renderQuestion() {
        if (state.filteredIndices.length === 0) {
            els.questionText.textContent = "No questions match your filter.";
            return;
        }

        const realIndex = state.filteredIndices[state.currentIndex];
        const q = state.questions[realIndex];

        // UI Reset
        state.showingAnswer = false;
        els.answerSection.classList.add('hidden');
        els.btnShowAnswer.classList.remove('hidden');
        els.navGroup.classList.add('hidden'); // Hide the group

        // Ensure buttons inside are reset if needed (not strictly necessary as we hide group)
        // But let's make sure focus isn't lost weirdly if we render/re-render

        // Content
        els.questionText.textContent = `${q.id}. ${q.question}`;

        // Answers
        els.answersList.innerHTML = '';

        // Smart Grid Layout: Two columns if > 5 answers
        if (q.answers.length > 5) {
            els.answersList.classList.add('grid-columns');
        } else {
            els.answersList.classList.remove('grid-columns');
        }

        q.answers.forEach((a, index) => {
            const li = document.createElement('li');

            // Container for text and button
            const mainContent = document.createElement('div');
            mainContent.className = 'answer-main';

            const textSpan = document.createElement('span');
            textSpan.textContent = a.text; // Assuming object {text: "...", story: "..."}

            const expandBtn = document.createElement('button');
            expandBtn.className = 'expand-btn';
            expandBtn.textContent = 'Why?';
            expandBtn.title = 'Read historical context';
            expandBtn.setAttribute('aria-expanded', 'false');

            // Gemini Button
            const { btn: geminiBtn, contentDiv: geminiDiv } = createGeminiButton(q, a);

            mainContent.appendChild(textSpan);

            // Wrapper for buttons
            const btnGroup = document.createElement('div');
            btnGroup.className = 'answer-actions';
            btnGroup.appendChild(geminiBtn);
            btnGroup.appendChild(expandBtn);

            mainContent.appendChild(btnGroup);

            // Gemini Content logic moved to end of list item

            // Story container
            const storyDiv = document.createElement('div');
            storyDiv.className = 'answer-story hidden';
            storyDiv.textContent = a.story;

            // Toggle Logic
            // Toggle Logic
            const initialExpanded = state.alwaysExpand; // Check global setting

            if (initialExpanded) {
                storyDiv.classList.remove('hidden');
                expandBtn.textContent = 'Close';
                expandBtn.setAttribute('aria-expanded', 'true');
            }

            expandBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                const isExpanded = expandBtn.getAttribute('aria-expanded') === 'true';
                expandBtn.setAttribute('aria-expanded', !isExpanded);
                if (isExpanded) {
                    storyDiv.classList.add('hidden');
                    expandBtn.textContent = 'Why?';
                } else {
                    storyDiv.classList.remove('hidden');
                    expandBtn.textContent = 'Close';
                }
            });

            li.appendChild(mainContent);
            li.appendChild(storyDiv);

            // Append Gemini Content (removed)

            els.answersList.appendChild(li);
        });

        // Auto Show Answer Logic
        if (state.alwaysShow) {
            showAnswer(false); // Don't steal focus
        }
        // Meta
        els.questionCounter.textContent = `Question ${state.currentIndex + 1} of ${state.filteredIndices.length}`;
        els.progressBar.style.width = `${((state.currentIndex + 1) / state.filteredIndices.length) * 100}%`;

        // Badges
        if (q.is_65_20) {
            els.badge6520.classList.remove('hidden');
        } else {
            els.badge6520.classList.add('hidden');
        }

        // Save state
        localStorage.setItem('civics_last_question_id', q.id);

        // Force scroll to top at the very end (async to ensure layout is done)
        const resetScroll = () => {
            if (els.cardContent) els.cardContent.scrollTop = 0;
            window.scrollTo(0, 0);
        };
        requestAnimationFrame(() => {
            resetScroll();
            // Double-check after a tick for mobile browsers
            setTimeout(resetScroll, 10);
        });
    }

    function showAnswer(shouldFocus = true) {
        state.showingAnswer = true;
        els.answerSection.classList.remove('hidden');
        els.btnShowAnswer.classList.add('hidden');
        els.navGroup.classList.remove('hidden'); // Show the group
        if (shouldFocus) {
            els.btnNext.focus();
        }
    }

    function nextQuestion() {
        if (state.currentIndex < state.filteredIndices.length - 1) {
            state.currentIndex++;
            renderQuestion();
        } else {
            // Loop back or finish? Let's loop for endless practice
            state.currentIndex = 0;
            renderQuestion();
        }
    }

    function prevQuestion() {
        if (state.currentIndex > 0) {
            state.currentIndex--;
            renderQuestion();
        }
    }



    function toggleShuffle() {
        // Store current Question ID
        let currentId = null;
        if (state.filteredIndices.length > 0) {
            const realIdx = state.filteredIndices[state.currentIndex];
            if (state.questions[realIdx]) {
                currentId = state.questions[realIdx].id;
            }
        }

        state.isShuffled = !state.isShuffled;
        els.btnShuffle.setAttribute('aria-pressed', state.isShuffled);
        if (state.isShuffled) {
            els.btnShuffle.classList.add('active');
        } else {
            els.btnShuffle.classList.remove('active');
        }

        state.currentIndex = 0;
        initSequence();
        renderQuestion();
    }

    function jumpToQuestion() {
        const val = parseInt(els.jumpInput.value);
        if (isNaN(val)) return;

        // Find the index in the current filtered list that corresponds to the question ID
        // Note: Questions might be shuffled or filtered. 
        // If shuffled, we find where that Question ID is in the current shuffled sequence.
        // If filtered (65/20), we check if it exists in current filter.

        const targetQ = state.questions.find(q => q.id === val);
        if (!targetQ) {
            alert("Question not found.");
            return;
        }

        const newIndex = state.filteredIndices.findIndex(originalIndex => state.questions[originalIndex].id === val);

        if (newIndex === -1) {
            if (false) {
                // Dead code removed
            } else {
                alert("Question not available in current mode.");
            }
            return;
        }

        state.currentIndex = newIndex;
        renderQuestion();
        els.jumpInput.value = '';
    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    function handleProgressClick(e) {
        const rect = els.progressContainer.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const width = rect.width;

        let percentage = x / width;
        // Clamp 0-1
        percentage = Math.max(0, Math.min(1, percentage));

        // Calculate index
        const total = state.filteredIndices.length;
        if (total === 0) return;

        let newIndex = Math.floor(percentage * total);
        // Clamp index
        newIndex = Math.max(0, Math.min(total - 1, newIndex));

        state.currentIndex = newIndex;
        renderQuestion();
    }

    // Scrubbing support
    let isScrubbing = false;

    function handleScrubStart(e) {
        isScrubbing = true;
        handleProgressClick(e); // Jump immediately
    }

    function handleScrubMove(e) {
        if (!isScrubbing) return;
        // If mouse leaves the element, we still want to track it if possible, 
        // but window listeners are cleaner. For simplicity, we attach to container.
        handleProgressClick(e);
    }

    function handleScrubEnd() {
        isScrubbing = false;
    }

    function createGeminiButton(q, a) {
        let btn;

        // "Ask Gemini" Button (Online Copy-Paste)
        btn = document.createElement('button');
        btn.className = 'gemini-toggle-btn'; // Use the pretty style
        btn.title = 'Copy prompt and open Gemini';
        btn.innerHTML = `<span>Ask Gemini</span>`; // Text + Icon via CSS or we can add SVG back if desired, but CSS has ::before content "✨"

        // Let's make it explicit with the SVG icon to match "start botton" description if they meant Star
        // Actually, the previous CSS `gemini-toggle-btn::before` adds a sparkle.
        // Let's stick to the text "Ask Gemini" and letting the CSS add the sparkle.
        // Or better, let's keep the user's "start botton" request in mind.
        // I will use the SVG from the fallback but wrapped in the pretty class.

        btn.innerHTML = `
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:4px">
                <path d="M12 2L15 9L22 12L15 15L12 22L9 15L2 12L9 9L12 2Z" fill="currentColor" stroke="none"/>
            </svg>
            Ask Gemini
        `;

        btn.addEventListener('click', async (e) => {
            e.stopPropagation();
            const prompt = `US civic test. For the question "${q.question}" the answer is "${a.text}" - please elaborate`;
            try {
                await navigator.clipboard.writeText(prompt);
                const originalHTML = btn.innerHTML;
                btn.innerHTML = '<span>Copied!</span>';
                window.open('https://gemini.google.com/app', '_blank');
                setTimeout(() => {
                    btn.innerHTML = originalHTML;
                }, 2000);
            } catch (err) {
                window.open('https://gemini.google.com/app', '_blank');
            }
        });

        return { btn, contentDiv: null };
    }

    // Event Listeners
    els.btnShowAnswer.addEventListener('click', showAnswer);
    els.btnNext.addEventListener('click', nextQuestion);
    els.btnPrevMain.addEventListener('click', prevQuestion); // New listener
    els.btnSkip.addEventListener('click', nextQuestion); // Arrow uses same logic
    els.btnPrev.addEventListener('click', prevQuestion);

    els.btnShuffle.addEventListener('click', toggleShuffle);

    els.btnAlwaysShow.addEventListener('click', () => {
        state.alwaysShow = !state.alwaysShow;
        localStorage.setItem('civics_always_show', state.alwaysShow);
        els.btnAlwaysShow.setAttribute('aria-pressed', state.alwaysShow);
        els.btnAlwaysShow.classList.toggle('active');
        renderQuestion();
    });

    els.btnAlwaysExpand.addEventListener('click', () => {
        state.alwaysExpand = !state.alwaysExpand;
        localStorage.setItem('civics_always_expand', state.alwaysExpand);
        els.btnAlwaysExpand.setAttribute('aria-pressed', state.alwaysExpand);
        els.btnAlwaysExpand.classList.toggle('active');
        renderQuestion();
    });

    els.jumpBtn.addEventListener('click', jumpToQuestion);
    els.jumpInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.stopPropagation(); // Prevent revealing answer
            jumpToQuestion();
        }
    });

    // Progress Bar Interactions
    els.progressContainer.addEventListener('mousedown', handleScrubStart);
    els.progressContainer.addEventListener('mousemove', handleScrubMove);
    window.addEventListener('mouseup', handleScrubEnd); // Handle mouseup anywhere
    // Touch support basic
    els.progressContainer.addEventListener('touchstart', (e) => {
        e.preventDefault(); // Prevent scroll
        const touch = e.touches[0];
        const fakeE = { clientX: touch.clientX };
        handleScrubStart(fakeE);
    });
    els.progressContainer.addEventListener('touchmove', (e) => {
        e.preventDefault();
        const touch = e.touches[0];
        const fakeE = { clientX: touch.clientX };
        handleScrubMove(fakeE);
    });
    window.addEventListener('touchend', handleScrubEnd);

    // Keyboard support
    document.addEventListener('keydown', (e) => {
        if (e.key === ' ' || e.key === 'Enter') {
            if (!state.showingAnswer) showAnswer();
            else nextQuestion();
        }
        if (e.key === 'ArrowRight') nextQuestion();
        if (e.key === 'ArrowLeft') prevQuestion();
    });
});
