import json
import os
import math

def split_questions(input_file='questions_base.json', output_dir='audit_batches', batch_size=50):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    total_questions = len(questions)
    num_batches = math.ceil(total_questions / batch_size)
    
    print(f"Found {total_questions} questions. Splitting into {num_batches} batches of {batch_size}.")
    
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, total_questions)
        batch = questions[start_idx:end_idx]
        
        output_file = os.path.join(output_dir, f'batch_{i+1:03d}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(batch, f, indent=2, ensure_ascii=False)
        
        print(f"Created {output_file} with {len(batch)} questions.")

if __name__ == "__main__":
    split_questions()

