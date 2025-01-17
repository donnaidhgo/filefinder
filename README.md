# FileFinder

FileFinder is a Python program designed to search for files across all drives on a Windows system with advanced filtering options to streamline searches.

## Features

- Search for files using a filename pattern (e.g., `*.txt`).
- Filter search results by minimum file size.
- Filter search results by file extension.

## Requirements

- Python 3.x

## Usage

The program can be run from the command line with the following syntax:

```bash
python filefinder.py [pattern] --path [search_path] --size [min_size] --extension [file_extension]
```

### Arguments

- `pattern`: The pattern to search for, such as `*.txt` for all text files.
- `--path`: The root directory to start the search from (default is `C:\`).
- `--size`: Minimum size of the file in bytes.
- `--extension`: File extension filter (e.g., `.txt`).

### Example

To search for all `.txt` files larger than 1KB in the `C:\Users\Documents` directory:

```bash
python filefinder.py *.txt --path C:\Users\Documents --size 1024 --extension .txt
```

## License

This project is licensed under the MIT License.