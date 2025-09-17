import tkinter
from tkinter import messagebox
import mysql.connector

def add_book():
    try:
        isbn = isbnEntry.get()
        title = titleEntry.get()

        
        dbaccess = mysql.connector.connect(host="localhost", user="root", password="", database="library_ChandraLekha")
        sql = dbaccess.cursor()
        insert_query = "INSERT INTO book (isbn, title) VALUES (%s, %s)"
        values = (isbn, title)
        sql.execute(insert_query, values)
        dbaccess.commit()

        message = ("The following book is successfully added to the library:\n" +
                   "ISBN: " + isbn + "\n" +
                   "Title: " + title)
        messagebox.showinfo("Success", message)

        dbaccess.close()
    except Exception as err:
        print("Database error:", err)

def save_book():
    isbn = isbnEntry.get()
    title = titleEntry.get()

    with open("book.txt", "a") as writer:
        writer.write(isbn + ", " + title + "\n")
        writer.close()

    messagebox.showinfo("Saved", "Book saved to file.")
  
#mainFrame

appFrame=tkinter.Tk()
appFrame.geometry("400x220")
appFrame.title("Library System ChandraLekha")

isbnLabel=tkinter.Label(text="ISBN: ")
isbnLabel.place(x=80,y=20);

isbnEntry=tkinter.Entry()
isbnEntry.place(x=120,y=20);

titleLabel=tkinter.Label(text="Title: ")
titleLabel.place(x=80,y=60);

titleEntry=tkinter.Entry()
titleEntry.place(x=120,y=60);

addButton=tkinter.Button(text="Add New Book", command=add_book)
addButton.place(x=90,y=120)

searchButton=tkinter.Button(text="Search ISBN")
searchButton.place(x=200,y=120)

saveButton=tkinter.Button(text="Save Book", command=save_book)
saveButton.place(x=140,y=170)
