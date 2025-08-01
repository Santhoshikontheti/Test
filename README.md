# Test

This repository contains a simple Python script to compare two Excel files.

## Usage

Install dependencies (requires `pandas`):

```bash
pip install pandas openpyxl
```

Run the script with two Excel files:

```bash
python compare_excel.py first.xlsx second.xlsx
```

The script prints `The Excel files are identical.` if they match, otherwise it shows a table of differences using `pandas.DataFrame.compare`.
