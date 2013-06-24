#测试数据库sqlite3
__author__ = 'hiCyoung'
import sqlite3

def main():
    db = sqlite3.connect("test.db")
    db.row_factory = sqlite3.Row
    db.execute("DROP  TABLE IF EXISTS test")
    db.execute("CREATE  TABLE test (id int,name text)")
    db.execute("INSERT INTO {} (id,name) VALUES(?,?)".format("test"),("1","cy"))
    db.execute("INSERT INTO test (id,name) VALUES(?,?)",("2","cy2"))
    db.execute("INSERT INTO test (id,name) VALUES(?,?)",("3","cy3"))
    db.commit()
    cursor = db.execute("SELECT id,name FROM test")
    for i in cursor:
        print(dict(i))
        print(i['name'])
    # cursor.fetchone()

main()
