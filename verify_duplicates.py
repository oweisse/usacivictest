import json

with open('questions.json', 'r') as f:
    questions = json.load(f)

print("Checking for duplicate stories within questions...")
issues_found = False

for q in questions:
    stories_seen = {}
    q_issues = []
    
    # We want to check the *meaningful* part of the story.
    # We recently added "Answer Text: Story Text" prefix.
    # We should detect if the "Story Text" part is identical across different answers.
    
    for ans in q['answers']:
        story = ans['story']
        text = ans['text']
        
        # Split prefix if present
        # Heuristic: split by ": " and take the last part, or just the whole thing if no colon
        # But wait, some stories might validly share text if they are synonyms?
        # But usually distinct answers should have distinct context or at least tailored text.
        
        # If the story is identical (ignoring the prefix we added), it's a "duplicate" in the user's eyes.
        
        # Extract the "story content"
        if ": " in story:
            # We assume the user sees "Answer: [Duplicate Text]"
            # So duplicate text after the colon is the issue.
            story_content = story.split(": ", 1)[1]
        else:
            story_content = story
            
        if story_content in stories_seen:
            q_issues.append(f"  - '{text}' shares story with '{stories_seen[story_content]}'")
        else:
            stories_seen[story_content] = text
            
    if q_issues:
        print(f"Question {q['id']}: {q['question']}")
        for issue in q_issues:
            print(issue)
        issues_found = True

if not issues_found:
    print("No duplicates found!")
