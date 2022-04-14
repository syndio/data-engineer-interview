import argparse
import sqlite3
from csv import DictReader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ingest-filename', dest='ingest_filename', help='the relative path to the data file we are ingesting')
    parser.add_argument('--db-filename', dest='db_filename', help='the relative path to the database file we are inserting data in')
    args = parser.parse_args()

    # extract
    records = csv_to_map(args.ingest_filename)

    # transform
    # ... your code here

    # load
    try:
        sqlite_conn = sqlite3.connect(args.db_filename)
        cursor = sqlite_conn.cursor()
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
