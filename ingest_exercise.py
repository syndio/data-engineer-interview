import argparse
import sqlite3
from csv import DictReader
from datetime import datetime, date
import os
import glob


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ingest-directory', dest='ingest_directory', help='the relative path to the directory containing data files we are ingesting')
    parser.add_argument('--db-filename', dest='db_filename', help='the relative path to the database file we are inserting data in')
    args = parser.parse_args()

    # extract
    all_records = []
    csv_files = glob.glob(os.path.join(args.ingest_directory, '*.csv'))
    if not csv_files:
        print(f"No CSV files found in directory: {args.ingest_directory}")
        return

    print(f"Found files to ingest: {csv_files}")

    for csv_file in csv_files:
        print(f"Ingesting file: {csv_file}")
        records = csv_to_map(csv_file)
        all_records.extend(records)

    print(f"Total records extracted: {len(all_records)}")

    # transform
    # TODO: Normalize column names to snake_case, parse dates, cast numeric fields.
    # TODO: Calculate derived column `tenure_days` = (today - start_date).
    transformed_records = []
    for row in all_records:
        # placeholder: append row as-is
        transformed_records.append(row)

    # load
    try:
        sqlite_conn = sqlite3.connect(args.db_filename)
        cursor = sqlite_conn.cursor()
        # TODO: Create table raw_employees if not exists

        print("Clearing existing data from raw_employees table...")
        cursor.execute("DELETE FROM raw_employees")
        print("Existing data cleared.")

        # TODO: Insert transformed_records into `raw_employees`
        sqlite_conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error loading table", error)
    finally:
        if sqlite_conn:
            sqlite_conn.close()

    # ... insert the transformed records into your sqlite schema


# csv_to_map takes a relative path to a csv file and returns a list of dictionaries, using the header row as the keys
def csv_to_map(ingest_filename):
    records = []
    with open(ingest_filename, 'r') as ingest_file:
        csv_dict_reader = DictReader(ingest_file)
        for row in csv_dict_reader:
            records.append(row)
    return records


if __name__ == "__main__":
    main()
