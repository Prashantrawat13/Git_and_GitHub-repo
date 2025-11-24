# Task 3. Branch Creation

We have completed the task 1 and task 2.
- Now we'll be Doing the task -3.


### a. Create two branches: master_1 and master_2 from the main branch.

Let's start with Creating the new Branches :
- master_1 and master_2

### Photo of master-branch 

***


### b. Feature Development in master_1:
  

#### 1. In the master_1 branch, create a To-Do Page in the frontend.

- **The page should contain a form with the following fields:**
	-  **Item Name**
	-  **Item Description**

Then switch to the master_1 branch 
`git switch master_1`

Let's start with the folder creation.
- First create an folder name : "ToDo" .
- `mkdir ToDo`

In the folder make an folder name : "Templates".
`mkdir Templates`

And in the "Templates" Folder we'll create an **todo.html file**.
`vim todo.html`

- With this you will open the editor that'll look like this

### Photo of Vim editor

When you are in editor, Do this:
- Press `i` to insert 
- And then paste this code or your If you have any.

```
<!DOCTYPE html>
<html>
<head>
    <title>To-Do Page</title>
</head>
<body>
    <h2>To-Do Item</h2>
    <form action="/submittodoitem" method="POST">
        <label>Item Name:</label>
        <input type="text" name="itemName" required><br><br>

        <label>Item Description:</label>
        <textarea name="itemDescription" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>

```

- After the code is pasted then Press `Esc` (escape button on keyboard)
- Then type `:wq` to save and exit the vim editor

### Photo Of code-looks


Now we'll commit the changes we did from the "**master_1**" Branch

- First we should add them to the staging.
`git add ./templates/todo.html`

- Then commit them with a message.
`git commit -m "Added the frontend of the todo in the todo folder"`

### Photo of master-1 commit


***

### c. Backend API in master_2:

 
#### 1. In the master_2 branch, create a backend route named /submittodoitem .

- **This route will:**
	- Accept **itemName** and **itemDescription** via a POST request.
	- Store these details in a MongoDB database.


In this we'll be working under the ToDo folder

In this we'll make an file name : `app.py`
-  You can create app.py using the touch command or in the VS-code manually and then paste the Code.

-  Or you can Copy me and make do it inside the Vim editor.

-  Let's create the app.py file using vim.
`vim app.py`        ||   What vim command do is, it opens the file in editor mode and if there is no file of such name then It'll create the file and open it in the editor.

Then the editor will be opened, 

- Firstly click `i` to insert

- Then paste the code :

```
from flask import Flask, request, jsonify, render_template

from pymongo import MongoClient

  

app = Flask(__name__)

  

# Connect to MongoDB

client = MongoClient("Here you'll paste your mongodb clint link")

db = client["tododb"]  # Database

todos_collection = db["todos"]  # Collection

  

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

```


To leave the editor:
- First press `Esc` then type `:wq` to save and exit the editor.

### Photo of the app-code


**This is what it'll Look like**

After it you can add the changes to the staging
- `git add .`

Then commit it with the message:
- `git commit -m "Added the app.py file to the master_2 branch"`

### Photo of the master-2-commit


***


### d. Merging Changes:

**Merge the changes from both master_1 and master_2 into the main branch.**

Let's merge the branches to the main branch

- For that first we'll first change to the main Branch.
- `git switch main`


-  Then we'll firstly merge the **master_1 branch**
- `git merge master_1`


- After merging master_1 branch 
	- Add it to staging. `git add .`
	- Then Commit it.  : `git commit "Merged the mster_1 branch to the main branch"`


- Then we'll do the same to **master_2 branch**
- `git merge master_2`


- After merging master_2 branch 
	- Add it to staging. `git add .`
	- Then Commit it.  : `git commit "Merged the mster_2 branch to the main branch"`


Then push it to the **Remote origin** :

```
git push origin main
```


### Photo of main push


***
***
