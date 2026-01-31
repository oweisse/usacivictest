document.addEventListener('DOMContentLoaded', () => {
    // State
    const state = {
        questions: [],
        currentIndex: 0,
        isShuffled: false,
        is6520Mode: false,
        showingAnswer: false,
        alwaysShow: false,   // New flag
        alwaysExpand: false, // New flag
        filteredIndices: [] // Stores indices of questions to show (based on shuffle/filter)
    };

    // Elements
    const els = {
        questionText: document.getElementById('question-text'),
        answersList: document.getElementById('answers-list'),
        answerSection: document.getElementById('answer-section'),
        questionCounter: document.getElementById('question-counter'),
        badge6520: document.getElementById('badge-65-20'),
        progressContainer: document.querySelector('.progress-container'), // Added container
        progressBar: document.getElementById('progress-bar'),

        btnShowAnswer: document.getElementById('show-answer-btn'),
        btnNext: document.getElementById('next-btn'),
        btnPrev: document.getElementById('prev-btn'),
        btnSkip: document.getElementById('skip-btn'),

        btnToggle6520: document.getElementById('toggle-65-20'),
        btnShuffle: document.getElementById('shuffle-btn'),
        btnAlwaysShow: document.getElementById('always-show-btn'),     // New
        btnAlwaysExpand: document.getElementById('always-expand-btn'), // New

        jumpInput: document.getElementById('jump-input'),
        jumpBtn: document.getElementById('jump-btn')
    };

    // Load Data
    fetch('questions.json')
        .then(res => res.json())
        .then(data => {
            state.questions = data;
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

        // Filter?
        if (state.is6520Mode) {
            indices = indices.filter(i => state.questions[i].is_65_20);
        }

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
        els.btnNext.classList.add('hidden');

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

            mainContent.appendChild(textSpan);
            mainContent.appendChild(expandBtn);

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
            els.answersList.appendChild(li);
        });

        // Auto Show Answer Logic
        if (state.alwaysShow) {
            showAnswer();
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
    }

    function showAnswer() {
        state.showingAnswer = true;
        els.answerSection.classList.remove('hidden');
        els.btnShowAnswer.classList.add('hidden');
        els.btnNext.classList.remove('hidden');
        els.btnNext.focus();
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

    function toggle6520() {
        // Store current Question ID
        let currentId = null;
        if (state.filteredIndices.length > 0) {
            const realIdx = state.filteredIndices[state.currentIndex];
            if (state.questions[realIdx]) {
                currentId = state.questions[realIdx].id;
            }
        }

        state.is6520Mode = !state.is6520Mode;
        els.btnToggle6520.setAttribute('aria-pressed', state.is6520Mode);
        if (state.is6520Mode) els.btnToggle6520.classList.add('active');
        else els.btnToggle6520.classList.remove('active');

        // Re-init sequence
        initSequence();
        state.currentIndex = 0;

        // Try to restore position
        if (currentId !== null) {
            // Find where this ID is in the NEW filtered list
            // If it's not in the new list (e.g. was filtered out), stay at 0
            const newIdx = state.filteredIndices.findIndex(idx => state.questions[idx].id === currentId);
            if (newIdx !== -1) {
                state.currentIndex = newIdx;
            }
        }

        renderQuestion();
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
            if (state.is6520Mode) {
                alert("That question is not part of the 65/20 set.");
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

    // Event Listeners
    els.btnShowAnswer.addEventListener('click', showAnswer);
    els.btnNext.addEventListener('click', nextQuestion);
    els.btnSkip.addEventListener('click', nextQuestion); // Arrow uses same logic
    els.btnPrev.addEventListener('click', prevQuestion);

    els.btnToggle6520.addEventListener('click', toggle6520);
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
