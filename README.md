# 🎓 Student Database Management System (MongoDB - Localhost)

A simple and efficient **Student Database Management System (DBMS)** built using **Python** and **MongoDB (localhost)**.  
This project performs basic **CRUD operations** (Create, Read, Update, Delete) on student records without using any web framework.

---

## 🚀 Features

- ➕ Add new student records  
- 📋 View all students  
- 🔍 Search student by ID or name  
- ✏️ Update student details  
- ❌ Delete student records  
- 💾 Data stored in MongoDB (local database)  

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Database:** MongoDB (Localhost)  
- **Library:** pymongo  

---

## 📁 Project Structure
📦 student-dbms-mongodb
┣ 📜 main.py
┣ 📜 requirements.txt
┗ 📜 README.md

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- Python (3.x)  
- MongoDB (running on localhost)  

---

## 🔗 MongoDB Connection

The project connects to MongoDB locally using:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
collection = db["students"]

---

## 📊 Sample Student Record

```json
{
  "student_id": "101",
  "name": "John Doe",
  "age": 20,
  "course": "Computer Science"
}

---

##🔄 CRUD Operations
  #➕ Create
      Insert a new student record into the database
  #📖 Read
      Fetch and display all student records
  #✏️ Update
      Modify existing student details
  #❌ Delete
      Remove a student record using ID

---

## 👩‍💻 Author

**Laxmi Parmanandani**  
- LinkedIn: https://www.linkedin.com/in/laxmi-parmanandani-63733a386/
