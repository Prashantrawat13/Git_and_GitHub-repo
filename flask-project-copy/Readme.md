
---

# **Project Documentation: Flask API + MongoDB Form Submission**

---

## **Introduction**

This project demonstrates how to build a small web application using **Flask** as the backend framework. It contains two main features:

1. An `/api` route that reads data from a file (`data.json`) and returns it as JSON.

2. A frontend form that allows users to submit data into **MongoDB Atlas**.

   * On success → user is redirected to a "Data submitted successfully" page.

   * On error → the user stays on the same page and sees the error message.

This project helped me understand Flask routing, working with JSON files, handling forms, connecting to MongoDB, and rendering templates.

---

## **Project Structure**

```

project/

│ app.py

│ data.json

│ templates/

│     form.html

│     success.html

```

### **File Descriptions**


|      File        |        Purpose                         |
| ---------------- | ---------------------------------------|
|                  |                                        |
| **app.py**       | The main Flask application             |
|                  |                                        |
| **data.json**    | Stores sample data returned by the API |
|                  |                                        |
| **form.html**    | Frontend form page                     |
|                  |                                        |
| **success.html** | Success message page                   |

---

## **Backend (Flask) Overview**

### **1. `/api` Route**

This route reads data from the `data.json` file and returns it in JSON format using `jsonify()`.

#### Code:

```python

@app.route('/api')

def api_data():

    with open("data.json", "r") as file:

        data = json.load(file)

    return jsonify(data)

```

#### How it works:

* `data.json` is opened

* Data is loaded as a Python list/dictionary

* Flask converts it into a proper JSON API response

---

### **2. Form Submission to MongoDB Atlas**

Users can enter their **name** and **age** in an HTML form.

The backend then:

* Validates the input

* Inserts the data into MongoDB Atlas

* Redirects to `/success` upon success

* Shows the error on the same page if something goes wrong

#### Code:

```python

@app.route("/", methods=["GET", "POST"])

def form():

    if request.method == "POST":

        try:

            name = request.form.get("name")

            age = request.form.get("age")

            if not name or not age:

                raise ValueError("Name and age are required!")

            collection.insert_one({

                "name": name,

                "age": int(age)

            })

            return redirect(url_for("success"))

        except Exception as e:

            return render_template("form.html", error=str(e))

    return render_template("form.html", error=None)

```

#### Concepts Learned:

* Processing HTML POST forms in Flask

* Handling validation errors

* Redirecting after successful operations

* Displaying the same page with error feedback

---

## **Frontend Templates**

### **1. `form.html`**

Contains:

* Input fields for name and age

* POST form

* Dynamic error message area

```html

<form method="POST">

    <label>Name:</label><br>

    <input type="text" name="name"><br><br>

    <label>Age:</label><br>

    <input type="number" name="age"><br><br>

    <button type="submit">Submit</button>

</form>

```
<img width="828" height="510" alt="image" src="https://github.com/user-attachments/assets/62140a7f-3548-44ff-9f19-607357096e70" />

This is the web page of the form.

---
### **2. `success.html`**

A simple page showing confirmation of successful submission.

---
```html

<h1>Data submitted successfully</h1>

```
<img width="864" height="476" alt="image" src="https://github.com/user-attachments/assets/e3e5642a-4d68-4660-8af8-2ef552f353c9" />

This is the web page when the form is filled successfully.

---

## **MongoDB Atlas Setup**

To connect MongoDB Atlas to the Flask application:

1. Create a MongoDB Atlas cluster.

2. Create a database and a collection.

3. Get your connection string.

4. Replace the placeholder in:

``` python

client = MongoClient("YOUR_MONGODB_ATLAS_CONNECTION_STRING")

```

Now Flask can insert documents into the cloud database.

---

## **How to Run the Project**

### Step 1 — Install dependencies

```

pip install flask pymongo

```

### Step 2 — Start the server

```

python app.py

```

### Step 3 — Open in browser

Form Page:

```

http://127.0.0.1:5000/

```
<img width="1470" height="364" alt="image" src="https://github.com/user-attachments/assets/6db52f01-a137-4b8f-b2ce-1a4060050d7e" />

This is the Command Prompt, and in this you can see how we got the local host IP to check the Server.


API Route:

```

http://127.0.0.1:5000/api

```

---

## **What I Learned**

* Creating routes in Flask

* Reading and sending JSON responses

* Handling HTML form submissions

* Error handling techniques

* Using MongoDB Atlas for persistent storage

* Using template rendering in Flask

* Redirecting users after successful actions

This project helped me understand both frontend → backend → database workflow in a real-world context.

---

## **Conclusion**

This is a good beginner-friendly project to understand how a full-stack application works using Flask and MongoDB. It covers API development, template rendering, form handling, and database integration.

*********
***



