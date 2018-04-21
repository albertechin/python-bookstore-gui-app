import sqlite3

def connect():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

connect()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()

    return rows

def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()

def search(title="", author = "", year = 0, isbn = 0):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()

    return rows

# def search(title="", author = "", year = 0, isbn = 0):
#     conn = sqlite3.connect("book.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM book WHERE title LIKE '%'?'%' OR author LIKE %?% OR year LIKE %?% OR isbn LIKE %?%",(title, author, year, isbn))
#     rows = cur.fetchall()
#     conn.close()

#     return rows


# insert("Holy Crap", "Monkey King", 4561, 78946)
# delete(1)


# insert("Banana Land", "Monkey King", 4561, 78946)
# insert("Monster Ball", "Lunatic", 1961, 78445)
# insert("Manly Gayle", "Universe Boss", 2015, 78656)

# print(view())
