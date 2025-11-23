from flask import Flask, jsonify, request, render_template, redirect, url_for
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# -------- MongoDB Atlas Connection --------
client = MongoClient("YOUR_MONGODB_ATLAS_CONNECTION_STRING")
# Connection string should look something like this {"mongodb+srv://prashant2003_db:<password>@cluster-name.4dqpndz.mongodb.net/?appName=Cluster-name"}

db = client["Cluster-assignment"]
collection = db["backend-base"]

# -------- 1. /api route returning JSON stored in file --------
@app.route('/api')
def api_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)


# -------- 2. Frontend form to insert data into MongoDB --------
@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            age = request.form.get("age")

            if not name or not age:
                raise ValueError("Name and age are required!")

            # Insert into MongoDB Atlas
            collection.insert_one({
                "name": name,
                "age": int(age)
            })

            # Redirect on success
            return redirect(url_for("success"))

        except Exception as e:
            # Error stays on same page
            return render_template("form.html", error=str(e))

    return render_template("form.html", error=None)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
