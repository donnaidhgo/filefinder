import os
import fnmatch
import argparse

def find_files(pattern, path, size=None, extension=None):
    """Search for files matching the pattern with optional size and extension filters."""
    
    matches = []
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, pattern):
            filepath = os.path.join(root, filename)
            if extension and not filename.endswith(extension):
                continue
            if size:
                file_size = os.path.getsize(filepath)
                if file_size < size:
                    continue
            matches.append(filepath)
    return matches

def main():
    parser = argparse.ArgumentParser(description='Searches for files across all drives with advanced filtering options.')
    parser.add_argument('pattern', type=str, help='The pattern to search for (e.g., *.txt)')
    parser.add_argument('--path', type=str, default='C:\\', help='The root directory to start the search from.')
    parser.add_argument('--size', type=int, help='Minimum size of the file in bytes.')
    parser.add_argument('--extension', type=str, help='File extension filter (e.g., .txt)')
    
    args = parser.parse_args()
    
    matches = find_files(args.pattern, args.path, args.size, args.extension)
    
    if matches:
        print("Files found:")
        for match in matches:
            print(match)
    else:
        print("No files found matching the criteria.")

if __name__ == '__main__':
    main()