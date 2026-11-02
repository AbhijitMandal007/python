import tkinter as tk
from tkinter import messagebox
import importlib

db = importlib.import_module("19b")

def start():
    root = tk.Tk()
    root.title("Library Management")

    tk.Label(root, text="Title").grid(row=0, column=0)
    title = tk.Entry(root)
    title.grid(row=0, column=1)

    tk.Label(root, text="Author").grid(row=1, column=0)
    author = tk.Entry(root)
    author.grid(row=1, column=1)

    tk.Label(root, text="ISBN").grid(row=2, column=0)
    isbn = tk.Entry(root)
    isbn.grid(row=2, column=1)

    def add():
        db.add(title.get(), author.get(), isbn.get())
        messagebox.showinfo("Success", "Book Added")

    tk.Button(root, text="Add Book", command=add).grid(row=3, column=1)

    tk.Label(root, text="Book ID").grid(row=4, column=0)
    book = tk.Entry(root)
    book.grid(row=4, column=1)

    tk.Button(
        root, text="Issue",
        command=lambda: db.issue(book.get())
    ).grid(row=5, column=0)

    tk.Button(
        root, text="Return",
        command=lambda: db.return_book(book.get())
    ).grid(row=5, column=1)

    tk.Label(root, text="Search").grid(row=6, column=0)
    search = tk.Entry(root)
    search.grid(row=6, column=1)

    result = tk.Listbox(root, width=60)
    result.grid(row=8, column=0, columnspan=2)

    def find():
        result.delete(0, tk.END)
        for b in db.search(search.get()):
            result.insert(tk.END, b)

    tk.Button(root, text="Search", command=find).grid(row=7, column=1)

    root.mainloop()