import sqlite3
from datetime import datetime


Db_Name ="expense.db"

def connect_db():
    return  sqlite3.connect(Db_Name)

def add_expense(name,price,category):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO expenses (name, amount, category , date ) VALUES (?,?,?,?)""",
    (name, price, category , datetime.now().strftime("%Y-%m-%d %H:%M")))

    conn.commit() 
    conn.close()

def delete_expense(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def view_expenses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL

    )""")
    conn.commit()
    conn.close()