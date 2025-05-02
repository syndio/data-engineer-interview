package main

import (
	"database/sql"
	"encoding/csv"
	"flag"
	"io"
	"log"
	"os"
	"path/filepath"

	_ "github.com/mattn/go-sqlite3"
)

func main() {
	fileToIngest := flag.String("file", "someFile.csv", "string: relative path to file")
	dbName := flag.String("dbName", "myDatabase.db", "string: relative path to sqlite db file")

	flag.Parse()

	// extract
	path, _ := filepath.Abs(*fileToIngest)
	f, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	records := csvToMap(f)
	_ = records

	// transform
	// ... your code here

	// load
	db, err := sql.Open("sqlite3", *dbName)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// ... insert the transformed records into your sqlite schema
}

// csvToMap takes a reader and returns an array of dictionaries, using the header row as the keys
func csvToMap(reader io.Reader) []map[string]interface{} {
	r := csv.NewReader(reader)
	var rows []map[string]interface{}
	header := make([]string, 0)
	for {
		record, err := r.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
		if len(header) == 0 {
			header = record
		} else {
			dict := make(map[string]interface{})
			for i := range header {
				dict[header[i]] = record[i]
			}
			rows = append(rows, dict)
		}
	}
	return rows
}
