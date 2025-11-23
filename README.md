
Today we'll be Doing some Task on Git and Github.


# Task 1 . Create a new GitHub repository.

### a. Clone the repository to your local machine using SSH (generate an SSH key if needed, add the public key to your GitHub account). 


Firstly we'll be starting with making a GitHub repository in our git-hub account


![account](Screen-shots\repo-name.png)

- We have created an repository named "[Git_and_GitHub-repo](https://github.com/Prashantrawat13/Git_and_GitHub-repo)"

- Now we'll be making the **clone of this repo in our Local Machine**

	- Now comes the Question How do we clone the repository from Github account to local..?
  
		- First we Click on the `<> Code` button and then Copy the HTTPS link.


![link](Screen-shots\Https-link-copy.png)


-  Now that we have our HTTPS link of the repo, now we'll make an `Folder` for the repo.
	
	-  Then name of the folder can be anything.
	
	- But we are naming it as **Git_and_GitHub-repo**, using the command `mkdir : make directory`.

	- After making the directory we can go into the directory using the `cd : change directory` command


  ![dir](Screen-shots\mk-dir.png)
  
- And now we have checked inside of the directory using `ls : list` command and it's empty.

Now to clone the repository we first have to **Initialize Git in the directory** using `git init` command.



![init](Screen-shots\Git-init.png)


After Initialization We have to **Clone the repo** and we'll be using this command.

```
git clone https://github.com/username/repository-name.git

{In the link we have to paste the link from the github account we copied earliar}
```


![clone](Screen-shots\git-clone.png)

***









- Create a new branch named after your username (e.g., Tutedude).
-  Add your Flask project files to this branch.
-  Commit the changes and merge the branch into the main branch.