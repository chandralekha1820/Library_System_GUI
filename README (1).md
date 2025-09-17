# 📚 Library System GUI

A simple Python application with **Tkinter** and **MySQL** for managing a library.  
Users can add books by ISBN and title, search for books, and save records to a file.

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
source .venv/bin/activate   # For Linux/Mac
.venv\Scripts\activate      # For Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup MySQL database
Run these commands in MySQL before starting the app:
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

## 🛠 Tech Stack
- Python (Tkinter)
- MySQL (mysql-connector-python)

---

## 📂 Repository Structure
```
Library_System_GUI/
│── FinalExamGUI_ChandraLekha.py     # Main GUI application
│── README.md                        # Project documentation
│── requirements.txt                 # Dependencies
│── .gitignore                       # Ignore unnecessary files
```
