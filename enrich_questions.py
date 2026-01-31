import json

def enrich_questions(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # Load stories data
    with open('stories_data.json', 'r', encoding='utf-8') as f:
        stories = json.load(f)


    enriched_questions = []
    
    for q in questions:
        old_answers = q['answers']
        new_answers = []
        
        # If it's already in new format, skip or re-process? Assuming old format [str, str]
        
        q_id = q['id']
        # Note: keys in JSON are strings, but q['id'] is int
        q_id_str = str(q['id'])
        specific_stories = stories.get(q_id_str, {})
        
        for ans_text in old_answers:
            # Clean dirty answer text (PDF artifacts)
            # The original code handled ans_text being a dict. The new code assumes string.
            # Let's ensure ans_text is a string before cleaning.
            answer_text_val = ans_text
            if isinstance(ans_text, dict):
                answer_text_val = ans_text.get('text', '')

            clean_text = answer_text_val.replace(" C: Recent American History and Other Important Historical Information", "").strip()
            
            # Check for specific story, check for legacy 'DEFAULT' or global default
            story = specific_stories.get(clean_text)
            
            if not story:
                story = specific_stories.get("DEFAULT", "Historical context for this answer is currently being researched.")

            # Ensure the story acts as a complete sentence/paragraph.
            # If the specific story is just a description ("She was..."), prepend the name.
            # But if it's a generic default, maybe don't? 
            # User asked: "make sure the story includes the actual answer"
            
            # Heuristic: If the story doesn't start with the answer text, prepend it.
            # But handle cases like "The Civil War" vs "Civil War".
            
            # Simple approach: Always prepend answer text as a bold prefix if it's a specific story
            # Or just "Answer: Story" style.
            # Let's try: "Susan B. Anthony: She was arrested..."
            
            # Only do this if we found a SPECIFIC story (not the generic fallback)
            # OR if we want to enforce it everywhere. 
            # The user's complaint "Lucy Stone... Susan B Anthony..." implies mismatch. 
            # If I fix the match, the mismatch goes away. 
            # But the user also said "make sure the story includes the actual answer".
            
            final_story = story
            if clean_text not in final_story and story != "Historical context for this answer is currently being researched.":
                 final_story = f"{clean_text}: {story}"

            new_answers.append({
                "text": clean_text,
                "story": final_story
            })
            
        q['answers'] = new_answers
        enriched_questions.append(q)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(enriched_questions, f, indent=2, ensure_ascii=False)
    
    print(f"Enriched {len(enriched_questions)} questions with stories.")

if __name__ == "__main__":
    enrich_questions('questions.json', 'questions.json')
