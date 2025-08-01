import argparse
import pandas as pd


def compare_excel(file1: str, file2: str) -> None:
    """Compare two Excel files and print the differences."""
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    if df1.equals(df2):
        print("The Excel files are identical.")
        return

    # Align dataframes so columns match
    df1, df2 = df1.align(df2, join="outer", axis=1)

    diff = df1.compare(df2, keep_shape=True, keep_equal=False)
    print("Differences found between the Excel files:")
    print(diff)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare two Excel files and show differences.")
    parser.add_argument("file1", help="Path to the first Excel file")
    parser.add_argument("file2", help="Path to the second Excel file")
    args = parser.parse_args()

    compare_excel(args.file1, args.file2)


if __name__ == "__main__":
    main()
