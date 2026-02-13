import csv
import sys

def remove_duplicates(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            rows = list(reader)

        if not rows:
            print("File is empty.")
            return

        header = rows[0]
        data = rows[1:]

        seen = set()
        unique_rows = []

        for row in data:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_rows.append(row)

        removed_count = len(data) - len(unique_rows)

        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            writer.writerows(unique_rows)

        print("\n=== Duplicate Cleaning Complete ===")
        print(f"Original Rows : {len(data)}")
        print(f"Removed       : {removed_count}")
        print(f"Remaining     : {len(unique_rows)}")
        print(f"Saved As      : {output_file}\n")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== CSV Duplicate Cleaner (Demo Version) ===")
    input_file = input("Enter input CSV file: ")
    output_file = input("Enter output CSV file: ")

    remove_duplicates(input_file, output_file)
