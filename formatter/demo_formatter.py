import csv
import json
import sys

def csv_to_json(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file, indent=4)

        print("Conversion completed successfully.")
        print(f"Output saved as: {output_file}")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 demo_formatter.py input.csv output.json")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    csv_to_json(input_file, output_file)
