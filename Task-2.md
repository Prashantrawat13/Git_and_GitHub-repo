Now we'll be Doing out 2nd task on Git and GitHub.


# Task 2 . Create a new branch named <your_name>_new (e.g., Tutedude_new).

In the earlier **Task 1** we had created an repository and added it to the local.

- Then we've created a Branch named "prashantrawat13".

- Then added some file using the branch and then **merged it into the main Branch**.


Now let's start with creating a New branch name : `Prashant_new`

	To create a new brach, the command we'll be using :

```
git branch -c prashant_new
```


### Photo New branch

In this we've first checked how many branches are there then created a new one and then Checked again.

- You can check if the branch is created or not by using the command `git branch`

***


### a. Update the content of the JSON file used for the /Api route in this branch.


Let's first switch to the "*Prashant_new*" Branch.   Command `git switch Prashant_new`

### photo new switch 

Now let's open our **Folder in the VS-Code**

- In VS-Code we'll now make some adjustment in the **Data.json file**.

### Photo Json-change

- In this We have added the 4th line in the existed file.

***

### b. Merge the <your_name>_new branch into the main branch.

For that first we'll first add and commit the changes from the branch, and them merge it from the main branch.

### Photo of json-commit

- In this we've added the data.json to staging. `git add Flask-project-copy/data.json`

- Then checked the status. `git status`

- And at last Commited it from our new branch.  `git commit -m "your-statement"`

Now we'll we merging the *Prashant_new* branch with the main branch.
- For that first let's switch to main branch. `git switch main`

Now that we are in the main Branch let's merge it with the "Prashant_new" branch.

```
git merge Prashant_new
```

### Photo of new merge

Now with this we've merged the *main branch* and the *Prashant_new* Branch

***

### c. If there are conflicts during the merge, resolve them by accepting the changes from the <your_name>_new branch.


We have successfully merged with the main branch.
- And there is no conflicts.

***

### d. Add the resolved changes to the staging area, commit them, and push the updates to the remote repository.


 Now we'll be pushing our Local Repository to Remote Repository (GitHub)

### Photo on new-push

The Command we've used is :
```
git push origin HEAD:main
```

I pushed it from my Prashant_new branch so I have to use 'HEAD:main' You can just use :

```
git push origin
```

But from the main Branch

### Photo of new-push


***
***

