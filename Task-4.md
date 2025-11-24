# Task 4. Enhancing the To-Do Form in master_1:


#### **a. In the master_1 branch, add the following fields to the To-Do form:**

- Item ID
	
- Item UUID
	
- Item Hash

#### *b. Committing in Sequence:*
    
- Add and commit each field separately in the following order:
    
- First commit: Add Item ID field.
    
- Second commit: Add Item UUID field.
    
- Third commit: Add Item Hash field.


**Now What we have to do is,**
- We'll make changes on the `todo.html` file
	-  First we'll add `Item id`
	-  Then we'll commit it .
		 
	-  Then we'll add `Item UUID`
	- Then we'll commit it.
		
	-  Then we'll add the `Item Hash`
	- Then we'll commit it.



**Now then let's start with switching to the master_1 branch**
	`git switch master_1`


**Now then we'll be adding the *Item Id* to the todo form and commit the changes.**

```
<label>Item ID:</label>
        <input type="text" name="itemId" required><br><br>
```

This is the `Item ID` that we have added in the File


#### Photo of Item-ID-add


This is how your code should Look like after adding.

Now that the changes are done, 
-  Then we'll add the changes to the staging.
-  `git add todo/templates/todo.html`
	
-  After adding we'll Commit the Changes.
-  `git commit -m "Item ID is added to the todo.html File"`


#### Photo of the Item-id Commit

Now here We have committed our Item-ID changes, Let's do every one of them one by one.

---

**Now then we'll be adding the *Item UUID* to the todo form and commit the changes.**

```
<label>Item UUID:</label>
        <input type="text" name="itemUUId" required><br><br>
```

	Usually the UUID is written in the backend but just for the show we are
	writing it, and we'll remove it by the end of this assignment.


This is the `Item UUID` that we have added in the File


#### Photo of Item-UUID-add


This is how your code should Look like after adding.

Now that the changes are done, 
-  Then we'll add the changes to the staging.
-  `git add todo/templates/todo.html`
	
-  After adding we'll Commit the Changes.
-  `git commit -m "Second commit : Item UUID is added to the todo.html File"`


#### Photo of the Item-UUid Commit

---


**Now then we'll be adding the *Item Hash* to the todo form and commit the changes.**

```
<label>Item Hash:</label>
        <input type="text" name="itemhash" required><br><br>
```

	Usually the Hash is written in the backend but just for the show we are
	writing it, and we'll remove it by the end of this assignment.

This is the `Item Hash` that we have added in the File


#### Photo of Item-Hash-add


This is how your code should Look like after adding.

Now that the changes are done, 
-  Then we'll add the changes to the staging.
-  `git add todo/templates/todo.html`
	
-  After adding we'll Commit the Changes.
-  `git commit -m "Second commit : Item Hash is added to the todo.html File"`


#### Photo of the Item-Hash Commit

***

As you all can see I've Committed it three times, Now I'll show you Commit Log.
Command used : `git log`

#### Photo of Logs

In this you can See the last 3 of my logs .

---


### c. Merging to main:

- **Merge the master_1 branch into the main branch.**

We'll first switch to the main branch:
	`git switch main`

Now Merge the **master_1 branch to the main branch**.
	`git merge master_1`

#### Photo of master-merge


***


### d. Git Reset and Commit Deletion:
    
1. In the main branch, use Git Reset to roll back to the commit where only the Item ID field was added.
	- Use `git reset --soft "Commit-id"` to ensure changes remain staged.

Now we'll be rolling back to the commit where we had just committed the Item-ID:


#### Photo of the roll-back

Now we'll be re-committing everything in a single commit

**With this instead of having this many commit, we'll only have a single commit and everything added**

---

2. Re-commit this state to the main branch.
    
- Merge this updated state to the main branch.

Now that we've done the soft reset every change is staged, 
we only have to commit now.

Then we'll commit the above 3 commit in a single commit,
	`git commit -m "Reorganizing the commits into a single commit"`


#### photo of the new-commit


***

#### Photo of new-Logs

**In these logs you can see the direct change on commit after the first commit**
- It now shows the reorganizing commit after the Item-ID commit.


***


### e. Rebasing Changes:
    
- **Rebase the updated changes in the main branch to the master_1 branch.**  

-  **Clarification :**
	- During rebasing, preserve individual commits to maintain the commit history for each change (i.e., do not squash commits).
    - Use git rebase main master_1 to integrate changes from the main branch back into the master_1 branch.



First let's switch to `master_1` branch.

Now we'll Rebase the master_1 branch by main branch.
- **And we'll see the changes it brings**

**Firstly we are seeing the logs before the Rebasing**

#### photo of before-rebasing


- Then we'll be Rebasing the master_1 branch with main.

```
git rebase main master_1
```


#### photo of rebasing

- During the rebase process there comes some conflicts, You can resolve them using the VS code.
	- You don't have to do much just accept the changes you want


- **Now that the Rebasing is done we'll se the logs and what's the difference.**


#### Photo after rebasing 

- **Now that the rebasing is done we can see the changes**
	- Here you can see after the Item-ID commit there is a new Commit showing that we have done on the main branch.
	- Previously the commits are like this : a-->b-->c.
	- But Now the commits are like this : a-->Reorganizing-->b-->c.
		
	- Here the commit that we made on main branch is shown here .



***
***
