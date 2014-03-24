Collaboration (SmartGit version)
-------------------------------

1. Create a fork of the desired central repository on GitHub (easy as clicking 
the fork button).  This is where you will "push" your changes and submit pull
requests.  

2. Clone this repository.  To do this, open SmartGit and in the File menu, select 
Clone.  You will need to enter the URL of your fork, and the location where you'd like
the files to go.  You don't need to check or un-check any of the other boxes.  This will
also create a "project" which is how you manage things in SmartGit.  

3.  Now you should have a folder (wherever you saved the clone) on your computer 
that contains all the files from the remote.  Open this, fiddle around with the code, 
do what you like.  Once you've made a series of changes you want to "save", go back 
to SmartGit.  Click on the "review" button in the top right corner.  This will bring up
a window with all your changed or added documents.  Select your changes and click the 
stage button.  Once everything you want to commit is staged, click the commit button
and enter a descriptive commit message.  

4.  Once you have all the changes you want to submit to the master repository, go back to 
the main window of smartgit.  Your local changes will be shown in the "outgoing" pane. 
Click on the "push" button on the left.  You'll have to 
log in, but your changes will get sent to your fork of the central repository.  

5. Submit a pull request from your fork of the repository (there will be a button 
somewhere on your repository page).  

6. To update your local copy from the central repository will require two steps.  
First, you must add the central repository as a remote to your project, by going 
to the remote menu and choosing "add".  Put in the url of the central repo, plus a 
name for your own use.  The remote will appear in the left pane under "branches."  
Right-click on the remote's name and select pull. 

###Note on workflow

It is helpful to pull from the central repository 
on a semi-regular basis in order to keep up with 
changes.   