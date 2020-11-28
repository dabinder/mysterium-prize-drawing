import mysql.connector
import random
import csv
import argparse

db_args = dict(
	host='localhost',
	user='prize_drawing',
	password='123',
	db='prizes',
	charset='utf8',
)
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--import-names', action='store_true')
args = parser.parse_args()

connection = mysql.connector.connect(**db_args)

#read csv file
if args.import_names:
	cursor = connection.cursor(prepared=True)
	with open ('attendees.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			sql = """ INSERT INTO attendees (badge_name, first_name, last_name) VALUES (%s, %s, %s)"""
			ituple = (row[0], row[1], row[2])
			cursor.execute(sql, ituple)
		connection.commit()
	cursor.close()

#draw names and display
cursor = connection.cursor(dictionary=True)
sql = "SELECT id, badge_name, first_name, last_name FROM attendees WHERE awarded=0"
cursor.execute(sql)
name_list = cursor.fetchall()

i = 1
while len(name_list) > 0:
	entry = name_list.pop(random.randrange(len(name_list)))
	print(
		str(i) + ".\r\n" +
		f"Badge Name: {entry['badge_name']}\r\n" +
		f"Name: {entry['first_name']} {entry['last_name']}"
	)
	i += 1
	sql = f"UPDATE attendees SET awarded=1 WHERE id={entry['id']}"
	cursor.execute(sql)
	connection.commit()
	input()

cursor.close()
connection.close()
