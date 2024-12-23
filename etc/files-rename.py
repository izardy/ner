import os

folder_path="/Users/izardy/Documents/GitHub/ner/labelling/ner_news_english/train.spacy"

def rename_files(folder_path, prefix=None, replace_text="labelled", new_text="train"):
    """
    Rename files in the specified folder with different options:
    - Add a prefix to all files
    - Replace specific text in filenames
    """
    try:
        # Verify if the directory exists
        if not os.path.exists(folder_path):
            raise ValueError(f"The directory {folder_path} does not exist")

        # Get list of all files in the directory
        files = os.listdir(folder_path)
        
        for filename in files:
            old_path = os.path.join(folder_path, filename)
            
            # Skip if it's a directory
            if os.path.isdir(old_path):
                continue
                
            new_filename = filename
            
            # Add prefix if specified
            if prefix:
                new_filename = f"{prefix}_{new_filename}"
                
            # Replace text if specified
            if replace_text and new_text:
                new_filename = new_filename.replace(replace_text, new_text)
                
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            if new_path != old_path:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Specify your folder path
    folder_path = "/Users/izardy/Documents/GitHub/ner/labelling/ner_news_english/train.spacy"
    
    # Example 1: Add a prefix to all files
    rename_files(folder_path, prefix="")
    
    # Example 2: Replace text in filenames
    # rename_files(folder_path, replace_text="new_", new_text="")
