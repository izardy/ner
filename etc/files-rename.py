import os

def rename_files(folder_path):
    """
    Rename files in the specified folder using pattern train_i_j
    where i starts from 0 and j starts from 10, incrementing by 10
    """
    try:
        if not os.path.exists(folder_path):
            raise ValueError(f"The directory {folder_path} does not exist")

        # Get list of all files in the directory
        files = sorted(os.listdir(folder_path))
        i = 0  # start value
        j = 10  # end value
        
        for filename in files:
            old_path = os.path.join(folder_path, filename)
            
            # Skip if it's a directory
            if os.path.isdir(old_path):
                continue
            
            # Get file extension
            file_extension = os.path.splitext(filename)[1]
            
            # Create new filename with train_i_j pattern
            new_filename = f"train_{i}_{j}{file_extension}"
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            if new_path != old_path:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
            
            # Increment i and j by 10 for next file
            i += 10
            j += 10

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    folder_path = "/Users/izardy/Documents/GitHub/ner/labelling/ner_news_english/data"
    rename_files(folder_path)
