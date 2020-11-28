# Mysterium prize drawing

This utility script is designed to facilitate prize drawing at the end of the convention. Instead of writing names on paper and drawing out of a hat, the attendee list can be imported from CSV format and names can be drawn at random from here. While running, push enter each time to obtain a new name.
Attendees previously awarded a prize will be marked and removed from the list. If you accidentally exit the application, run without the -i argument to resume with the previous list.

## Setup
Requires SQLite (https://sqlite.org/download.html) in your PATH. Run create_db.bat to create the database and attendees table.

Replace the contents of attendees.csv with an export of this year's attendee list. The CSV file should be formatted as badge_number,badge_name,first_name,last_name.

## Usage
```
python prizes.py [-i|--import-names]
```

## Arguments
Short Value | Long Value | Description
----------- | ---------- | -----------
-i | --import-names | Looks for attendees.csv and imports the list into the local database. Any previous entries in the table will be deleted. 