import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# --- LOCAL DATABASE CONNECTION ---
# This connects to the MongoDB server running on your own laptop (Compass)
MONGO_URI = "mongodb://127.0.0.1:27017/"

# serverSelectionTimeoutMS=2000 makes it fail fast if your MongoDB service isn't on
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)

try:
    # Check if the local server is running
    client.admin.command('ping')
    print("✅ SUCCESS: Connected to Local MongoDB (Compass)!")
except Exception as e:
    print(f"❌ CONNECTION ERROR: {e}")
    print("Make sure 'MongoDB Server' is started in your Windows Services!")

db = client["studentDB"]
students_col = db["students"]

# --- ROUTES ---

@app.route('/')
def index():
    try:
        all_students = list(students_col.find())
        return render_template('index.html', students=all_students)
    except Exception as e:
        return f"Local Database Error: {e}"

@app.route('/add')
def add_page():
    return render_template('add.html')

@app.route('/add_logic', methods=['POST'])
def add_logic():
    name = request.form.get('name')
    roll = request.form.get('roll_no')
    marks = request.form.get('marks')
    
    if name and roll:
        students_col.insert_one({
            "name": name, 
            "roll_no": roll, 
            "marks": int(marks)
        })
    return redirect(url_for('index'))

@app.route('/update')
def update_page():
    return render_template('update.html')

@app.route('/update_logic', methods=['POST'])
def update_logic():
    roll = request.form.get('roll_no')
    new_marks = request.form.get('marks')
    
    if roll and new_marks:
        students_col.update_one(
            {"roll_no": roll}, 
            {"$set": {"marks": int(new_marks)}}
        )
    return redirect(url_for('index'))

@app.route('/confirm_delete/<roll>')
def confirm_delete(roll):
    return render_template('delete.html', roll_no=roll)

@app.route('/delete_logic/<roll>', methods=['POST'])
def delete_logic(roll):
    students_col.delete_one({"roll_no": roll})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)