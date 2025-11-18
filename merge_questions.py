import json
import os
import glob

def merge_questions(input_dir='audit_batches_corrected', output_file='questions_base_updated.json'):
    # Look for all json files in the input directory
    files = sorted(glob.glob(os.path.join(input_dir, '*.json')))
    
    if not files:
        print(f"No JSON files found in {input_dir}")
        return
        
    all_questions = []
    seen_ids = set()
    
    print(f"Found {len(files)} files to merge.")
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                batch = json.load(f)
                
            if isinstance(batch, list):
                for q in batch:
                    if 'id' in q:
                        if q['id'] not in seen_ids:
                            all_questions.append(q)
                            seen_ids.add(q['id'])
                        else:
                            print(f"Duplicate ID found: {q['id']} in {file_path}. Skipping.")
                    else:
                        print(f"Question missing ID in {file_path}. Skipping.")
            else:
                print(f"File {file_path} does not contain a JSON list. Skipping.")
                
        except json.JSONDecodeError as e:
            print(f"Error decoding {file_path}: {e}")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    print(f"Merged {len(all_questions)} unique questions.")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    print(f"Saved merged questions to {output_file}")

if __name__ == "__main__":
    # Ensure the directory exists
    if not os.path.exists('audit_batches_corrected'):
        os.makedirs('audit_batches_corrected')
        print("Created 'audit_batches_corrected' directory. Place your corrected JSON files here.")
    
    merge_questions()

