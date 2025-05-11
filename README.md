# 📄 pdfMerger

A Python CLI script to merge a set of PDF files, sorted by a leading number in the filename, separated from the name by a custom delimiter.

## Requirements

- Python 3.8 or higher
- [pypdf](https://pypi.org/project/pypdf/)

## Dependencies

Install dependencies with:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate.bat
pip install pypdf
```

## Usage

```bash
python test_main.py input_dir [--separator SEPARATOR] [--output-dir DIR] [--file-name NAME] [--preview]
```

### Arguments

- `input_dir` (positional): Directory containing the PDF files to merge.
- `--separator`: Separator between the leading number and the file name (e.g., `1 - Title.pdf`, separator: `-`). Default: space `" "`.
- `--output-dir`: Directory where the merged PDF will be saved. Default: current working directory.
- `--file-name`: Name of the resulting PDF file. `.pdf` will be added if missing. Default: `MergedPdf.pdf`.
- `--preview`: Show the list of files that would be merged, without actually merging them.

## Example

Assume the folder `lectures_pdf/` contains the following files:

```
1 - Introduction.pdf
2 - Theory.pdf
3 - Exercises.pdf
```

Run:

```bash
python test_main.py lectures_pdf --separator - --file-name Summary --output-dir merged_output
```

The resulting file will be saved as:

```
merged_output/Summary.pdf
```

To preview the merge order:

```bash
python test_main.py lectures_pdf --separator - --preview
```

## Important Notes

- Files must start with an integer followed by the specified separator. 
- Corrupted or unreadable PDF files will be skipped and reported in the terminal.

## Author

**Gabriele Lo Bosco**
Bachelor's student in Computer Science
University of Basilicata

### Credits

[pypdf on PyPI](https://pypi.org/project/pypdf/)
