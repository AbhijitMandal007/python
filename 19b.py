import sqlite3

def connect():
    return sqlite3.connect("library.db")

def setup():
    db = connect()
    db.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            isbn TEXT,
            status TEXT DEFAULT 'Available'
        )
    """)
    db.commit()
    db.close()

def add(title, author, isbn):
    db = connect()
    db.execute(
        "INSERT INTO books(title,author,isbn) VALUES(?,?,?)",
        (title, author, isbn)
    )
    db.commit()
    db.close()

def search(text):
    db = connect()
    rows = db.execute(
        "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
        ("%" + text + "%", "%" + text + "%")
    ).fetchall()
    db.close()
    return rows

def issue(book_id):
    db = connect()
    db.execute(
        "UPDATE books SET status='Issued' WHERE id=?",
        (book_id,)
    )
    db.commit()
    db.close()

def return_book(book_id):
    db = connect()
    db.execute(
        "UPDATE books SET status='Available' WHERE id=?",
        (book_id,)
    )
    db.commit()
    db.close()