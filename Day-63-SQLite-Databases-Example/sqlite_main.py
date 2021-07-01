import sqlite3


db = sqlite3.connect("book-collection.db")

cursor = db.cursor()

# Creating Tables in our Database
# cursor.execute(
#     "CREATE TABLE books (id INTEGER  PRIMARY KEY,"
#     "title varchar(250) NOT NULL UNIQUE,"
#     "author varchar(250) NOT NULL,"
#     "rating FLOAT NOT NULL)"
# )


# Add data to our table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
