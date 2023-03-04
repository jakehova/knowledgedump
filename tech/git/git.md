# GIT

tool that lets you track file history

## Primary Ideas
* tell git which folder/files you want to keep track of
* tell git which folders/files you want to add to your saved changes
* tell git to record the changes

## Primary Ideas A Bit Deeper
* you tell git that you want to keep track of changes in a particular folder by using the command git init
  * this creates a folder named .git in the folder you want to keep track of.  that folder contains the files necessary for tracking the changes
* you can AND SHOULD add a ".gitignore" file.  This file tells git to ignore some files.  If your files are going to be stored remotely, then add any files or folders that contain secrets to it.  Also add any bin/exe/node_modules to it so that your repo doesnt get large with folers/files that can be regenerated using tools
* you tell git to add your changes by saying "git add <files or a '.' if you want to add everything in the current directory>" 
* you label those changes using "git commit -m "<label you want to give to your changes>"
* you move those changes to a web location by using "git push".  git push will take all the labels (commits) you created that you havent pushed yet and copy them up to the web local you specify
  * the web location is specified by specifying web address of the website location you are using.  the web location is called the "origin" when y9ou do the first push.  After you do the first push, git will remember the origin so you can just use git push to push in the future.

## Primary Commands
* git add . => adds all files in the current directory to be staged for commiting
* git commit - m "<msg>" => takes all the staged files and commits them
* git push => pushes the local commits to an origin repo


