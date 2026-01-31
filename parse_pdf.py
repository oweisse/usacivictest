import re
import json
import sys
from pypdf import PdfReader

def parse_pdf(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    text = ""
    # Skip page 0 (intro), start from page 1
    for page in reader.pages[1:]:
        page_text = page.extract_text()
        text += "\n" + page_text

    lines = text.split('\n')
    questions = []
    current_question = None
    
    # Regex patterns
    # Matches "1. Question text"
    question_pattern = re.compile(r'^(\d+)\.\s+(.*)')
    # Matches bullet points
    answer_pattern = re.compile(r'^\s*[•·]\s*(.*)')
    # Matches section headers or unwanted text (simple heuristic)
    # We'll just ignore lines that don't match Q or A pattern if they seem unrelated
    
    # Ignore specific phrases from headers/footers
    ignore_phrases = [
        "uscis.gov/citizenship",
        "Civics Questions and Answers",
        "of 19", # Page numbers
        "M-1778"
    ]

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if line should be ignored
        if any(phrase in line for phrase in ignore_phrases):
            continue

        # Check for Question
        q_match = question_pattern.match(line)
        if q_match:
            # Save previous question
            if current_question:
                questions.append(current_question)
            
            q_id = int(q_match.group(1))
            q_text = q_match.group(2).strip()
            
            # Check for trailing asterisk in question text
            is_65_20 = False
            if q_text.endswith('*'):
                is_65_20 = True
                q_text = q_text.rstrip('*').strip()
            
            current_question = {
                "id": q_id,
                "question": q_text,
                "answers": [],
                "is_65_20": is_65_20
            }
            continue

        # Check for standalone asterisk (65/20 rule indicator on new line)
        if line == '*' and current_question:
            current_question['is_65_20'] = True
            continue

        # Check for Answer
        a_match = answer_pattern.match(line)
        if a_match:
            if current_question:
                current_question['answers'].append(a_match.group(1).strip())
            continue
            
        # Handle continuation lines or Section Headers
        # If it looks like a section header (e.g., "A: Principles..."), ignore it for now
        # If it looks like text continuation, append to last answer or question
        if current_question:
            # Heuristic: if current question has answers, append to last answer
            if current_question['answers']:
                 # If the line starts with a capital letter and seems distinct, it might be a section header like "B: System..."
                 # Questions are linear 1-128. Section headers usually don't look like answer continuations.
                 # Let's check against a pattern for section headers
                 if ":" in line and len(line) < 50 and (line.startswith("A:") or line.startswith("B:") or line.startswith("C:")):
                     continue
                 
                 # Append to last answer
                 current_question['answers'][-1] += " " + line
            else:
                 # Append to question text
                 # Check if it's a section header
                 if ":" in line and len(line) < 50 and (line.startswith("A:") or line.startswith("B:") or line.startswith("C:")):
                     continue
                 current_question['question'] += " " + line

    # Append last question
    if current_question:
        questions.append(current_question)

    # Convert to JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully parsed {len(questions)} questions to {output_path}")

if __name__ == "__main__":
    parse_pdf("2025-Civics-Test-128-Questions-and-Answers (1).pdf", "questions.json")
