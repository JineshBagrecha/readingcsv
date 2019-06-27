import pymysql
import  csv
# import mysql.connector;
connection = pymysql.connect(host="localhost", user="root", passwd="jinesh123", db="sample");
cursor = connection.cursor()

stri = """insert into store_details (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10) values ("""

f = open("C:\\Users\\Jinesh Bagrecha\\Documents\\csvex.txt", "r")

next(f)
for line in f:
    word = line.split(',')
    #print(word)
    c = len(word)
    query = stri
    #print(c)
    for i in range(c):
        query = query + "'" + word[i] + "',"
    query = query[:-1]
    query = query + ")"
    cursor.execute(query)
    #print(query)