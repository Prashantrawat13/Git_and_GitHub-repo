from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/tododb"
mongo = PyMongo(app)

@app.route('/todo')
def todo_page():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')

    # Insert into MongoDB
    todo_collection = mongo.db.todos
    todo_collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return jsonify({"message": "Item saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

