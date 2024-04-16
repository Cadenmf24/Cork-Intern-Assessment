import sqlite3

con = sqlite3.connect("CorkInternAssessment.db")

cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)")

res = cur.execute("Select name FROM sqlite_master")

print(res.fetchone())