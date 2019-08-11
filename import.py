import pymysql
import csv

db_args = dict(
	host='localhost',
	user='prize_drawing',
	password='123',
	db='prizes',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
)
connection = pymysql.connect(**db_args)
cursor = connection.cursor(pymysql.cursors.DictCursor)

with open ('attendees.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		sql = f"INSERT INTO attendees (badge_name, first_name, last_name) VALUES ('{row[0]}', '{row[1]}', '{row[2]}')"
		cursor.execute(sql)
	connection.commit()
		
connection.close()