import pymysql
import random

db_args = dict(
	host='localhost',
	user='prize_drawing',
	password='123',
	db='prizes',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
)

connection = pymysql.connect(**db_args)
with connection.cursor(pymysql.cursors.DictCursor) as cursor:
	sql = "SELECT id, badge_name, first_name, last_name FROM attendees"
	cursor.execute(sql)
	name_list = cursor.fetchall()
	
	i = 1
	while len(name_list) > 0:
		input()
		entry = name_list.pop(random.randrange(len(name_list)))
		print(
			str(i) + ".\r\n" +
			f"Badge Name: {entry['badge_name']}\r\n" +
			f"Name: {entry['first_name']} {entry['last_name']}"
		)
		i += 1
		sql = f"DELETE FROM attendees WHERE id={entry['id']}"
		cursor.execute(sql)
		connection.commit()