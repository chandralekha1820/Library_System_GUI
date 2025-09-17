
# 📚 Library System GUI

A simple **Python desktop application** built with **Tkinter** and **MySQL** to manage a library.  
The app allows users to add new books, search existing ones, and save records into a local text file.

---

## ✨ Features
- 📝 **Add Book** → Insert a new book by ISBN and Title into the MySQL database  
- 🔍 **Search ISBN** → Find a book’s title by its ISBN  
- 💾 **Save Book** → Save book records into a local text file (`book.txt`)  
- ✅ **User-Friendly GUI** → Built with Tkinter, simple and interactive  
- ⚡ **Error Handling** → Database errors are caught and shown to the user  

---

## 🛠 Tech Stack
- **Programming Language**: Python 3.x  
- **GUI Framework**: Tkinter  
- **Database**: MySQL (via `mysql-connector-python`)  
- **Storage**: Local text file for book logs  

---

## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/username/Library_System_GUI.git
cd Library_System_GUI
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup MySQL Database
Run these commands in MySQL:
```sql
CREATE DATABASE library_ChandraLekha;
USE library_ChandraLekha;
CREATE TABLE book (
    isbn VARCHAR(20) PRIMARY KEY,
    title VARCHAR(100)
);
```

### 5. Run the application
```bash
python FinalExamGUI_ChandraLekha.py
```

---

## 📊 Example Usage
1. Open the app  
2. Enter **ISBN** and **Title** → click **Add New Book**  
   - Saves record into MySQL  
   - Shows confirmation message  
3. Click **Search ISBN** to look up any book  
4. Click **Save Book** to store the details in a `book.txt` file  

---

## 📂 Repository Structure
```
Library_System_GUI/
│── FinalExamGUI_ChandraLekha.py     # Main GUI application
│── README.md                        # Documentation
│── requirements.txt                 # Dependencies
│── .gitignore                       # Ignore unnecessary files
│── LICENSE                          # Open-source license (MIT)
```

---

## 🔮 Future Improvements
- Add support for **updating & deleting books**  
- Show a **list of all books** in the GUI  
- Improve UI styling with `ttk` or custom themes  
- Add user login for multi-user library management  


Improve UI styling with ttk or custom themes

Add user login for multi-user library management
