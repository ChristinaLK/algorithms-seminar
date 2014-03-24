Collaboration (Bash version)
---------------------------

1. Create a fork of the desired central repository on GitHub (easy as clicking 
the fork button).  This is where you will "push" your changes and submit pull
requests.  

2. In the shell, cd into the directory where you'd like the files 
to go.  Clone will make a directory for you.  Clone this repository, using the format 
	~~~
	$git clone <url-of-your-fork>
	~~~

3.  Now you should have a folder (wherever you saved the clone) on your computer 
that contains all the files from the remote.  Open this, fiddle around with the code, 
do what you like.  Once you've made a series of changes you want to "save", use the 
following commands:
	~~~
	$git status
	~~~
will show you which files you changed.  
	~~~
	$git add <files changed>
	~~~
stages the files.  You can use the flag -A instead of filenames to add all files.  
Then commit.  
	~~~
	$git commit -m "put your commit message here"
	~~~

4.  Once you have made all the changes you want to submit to the master repository, 
type in:
	~~~
	$git push origin master
	~~~ 

5. Submit a pull request from your fork of the repository (there will be a button 
somewhere on the repository page).  

6. To update your local copy from the central repository will require two steps.  First, you must 
add the central repository as a remote to your project.  
	~~~
	$git remote add <name-for-remote> <url-for-master-repo>
	~~~ 
Then "pull".  
	~~~
	$git pull <name-chosen-above> master
	~~~ 

If you have a merge conflict, edit the documents listed as being in conflict, then 
add and commit them as in 3.  

###Note on workflow

It is helpful to pull from the central repository 
on a semi-regular basis in order to keep up with 
changes.  