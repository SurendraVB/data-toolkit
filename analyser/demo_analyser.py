import csv
import sys
from collections import defaultdict

def analyze_csv(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            print("File is empty.")
            return

        print("\n=== Basic CSV Analysis ===\n")

        # Row count
        print(f"Total Rows: {len(rows)}")

        # Columns
        columns = reader.fieldnames
        print(f"Columns: {', '.join(columns)}\n")

        # Missing values
        missing_counts = defaultdict(int)

        for row in rows:
            for col in columns:
                if row[col] is None or row[col].strip() == "":
                    missing_counts[col] += 1

        print("Missing Values:")
        for col in columns:
            print(f"  {col}: {missing_counts[col]}")

        # Basic type inference
        print("\nBasic Type Guess:")
        for col in columns:
            sample_value = next((row[col] for row in rows if row[col]), "")
            
            if sample_value.isdigit():
                dtype = "Integer"
            else:
                try:
                    float(sample_value)
                    dtype = "Float"
                except:
                    dtype = "Text"

            print(f"  {col}: {dtype}")

        print("\nAnalysis Complete.\n")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    file_path = input("Enter CSV file name: ")
    analyze_csv(file_path)
