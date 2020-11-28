import sqlite3
import random
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--import-names', action='store_true')
args = parser.parse_args()

connection = sqlite3.connect('prizes.db')

#read csv file
if args.import_names:
	cursor = connection.cursor()
	cursor.execute("DELETE FROM attendees")
	with open ('attendees.csv', encoding="utf-8") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			sql = """ INSERT INTO attendees (badge_number, badge_name, first_name, last_name) VALUES (?, ?, ?, ?)"""
			ituple = (row[0], row[1], row[2], row[3])
			cursor.execute(sql, ituple)
	connection.commit()
	cursor.close()

#draw names and display
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
sql = "SELECT rowid, badge_number, badge_name, first_name, last_name FROM attendees WHERE awarded=0"
cursor.execute(sql)
name_list = cursor.fetchall()

i = 1
while len(name_list) > 0:
	entry = name_list.pop(random.randrange(len(name_list)))
	print(
		str(i) + ".\r\n" +
		f"Badge Number: {entry['badge_number']}\r\n" +
		f"Badge Name: {entry['badge_name']}\r\n" +
		f"Name: {entry['first_name']} {entry['last_name']}"
	)
	i += 1
	sql = f"UPDATE attendees SET awarded=1 WHERE rowid={entry['rowid']}"
	cursor.execute(sql)
	connection.commit()
	input()

cursor.close()
connection.close()
