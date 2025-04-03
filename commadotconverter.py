import os

def convert_commas_to_periods(folder_path):
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist.")
        return
    
    # Process all .txt files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith("properties.txt"):  # Ignore the properties files so that they dont cause error
            continue
        if filename.endswith(".txt"):  # Only process .txt files
            file_path = os.path.join(folder_path, filename)
            
            try:
                # Read the file content
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Replace commas with periods
                updated_content = content.replace(',', '.')
                
                # Write the modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                
                print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing .txt files: ")
    convert_commas_to_periods(folder_path)