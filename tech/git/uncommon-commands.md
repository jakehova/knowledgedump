# Uncommon Situation
* You want to remove a folder/file(s) that is already part of a commit but NOT pushed to origin
 * git rm --cached <folder/file> 
 * git commit --amend -CHEAD
 * git push
* You want to remove a folder/file(s) that is already part of a commit that has been pushed to origin already
  * delete the folder or file(s) locally
  * make a commit 
  * do a soft reset that goes back to the repo BEFORE you added the file/folder you want to add (x represents the number of commits back you need to go): git reset --soft HEAD~x 
  * recommit all the changes: git commit -m "<msg for the new commit>"
  * git push
* 