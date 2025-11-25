import sqlite3

db = sqlite3.connect("users.db")
cursor = db.cursor()

username = input("Enter username: ")
query = f"SELECT * FROM users WHERE username = '{username}'"
