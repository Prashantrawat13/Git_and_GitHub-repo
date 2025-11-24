from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["tododb"]  # Database
todos_collection = db["todos"]  # Collection

# Route to serve To-Do HTML page
@app.route('/')
def todo_page():
    return render_template('todo.html')

# API route to submit To-Do item
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')

    # Insert into MongoDB
    todos_collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return jsonify({"message": "Item saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
