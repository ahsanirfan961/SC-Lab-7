import os
import sys

def find_file(directory, target_file):
    try:
        entries = os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
        return None
    except PermissionError:
        print(f"Warning: Permission denied for directory '{directory}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    for entry in entries:
        entry_path = os.path.join(directory, entry)
        
        if os.path.isfile(entry_path) and entry == target_file:
            return entry_path

        elif os.path.isdir(entry_path):
            found_path = find_file(entry_path, target_file)
            if found_path:
                return found_path  # File found in a subdirectory
    
    return None


def main():
    if len(sys.argv) != 3:
        print("Usage: python search_file.py <directory_path> <file_name>")
        return
    
    directory_path = sys.argv[1]
    file_name = sys.argv[2]
    
    result = find_file(directory_path, file_name)
    
    if result:
        print(f"File found: {result}")
    else:
        print(f"The file '{file_name}' was not found in the directory '{directory_path}' or its subdirectories.")

if __name__ == "__main__":
    main()
