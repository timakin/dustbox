# -*- coding: utf-8 -*-
import MySQLdb
import csv

#DBに接続
db = MySQLdb.connect(user="test", passwd="testpassword", db="test")
c = db.cursor()
c.execute('DELETE FROM testcsv')
c.execute('ALTER TABLE testcsv AUTO_INCREMENT = 1')
#CREATE TABLE test.testcsv
#     (
#     id INT(11) NOT NULL AUTO_INCREMENT,
#     time VARCHAR(32),
#     study VARCHAR(32),
#     value INT(11),
#     PRIMARY KEY (id)
#     );


csv_data = csv.reader(file('roudou.csv'))
for row in csv_data:
	c.execute('INSERT INTO testcsv(time, study, value) VALUES("%s", "%s", "%s")' % (row[1], row[5], row[7]))
#close the connection to the database.
db.commit()

c.execute('SET NAMES utf8')
c.execute('SELECT * FROM testcsv')
result = c.fetchall()
sum = 0
i = 0
for row in result:
	print row[0], row[1], row[2], row[3]

#SELECT AVG(value) from test.testcsv where id>=2 and id=<6
#これで、総数以外の平均値を出す事ができる。
c.close()

print "Done"
