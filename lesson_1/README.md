# Lesson 1:

### Copying repository
If you want to contribute to existing repository then you have to *Fork* existing repository. After forking, GitHub will copy desired Repository to your account to give you ability to work with code (add, change, delete) without be a hindrance to *Parent Repository* or to another developers.
*This action executed in web interface of GitHub, inside parent repository.*

### Getting copy of repository to your PC
To get this repository locally, you have to chose folder on your PC that you going to use for your programming projects and run **GitBash** in it. Within git bash you have to execute only one command (replace your name!):
```
git clone https://github.com/{YourGitName}/FromZeroToHero.git
```
And **Git** automatically download create new Repository to your folder (with all folders, subfolders and files). In case, if you need to update state of Repository that was cloned before, you have to execute another command:
```
git pull origin master
```
Or you  can delete Repository folder, and clone it again.

### Updating copy of repository from your PC
If you finished your hard work and improve Repository by made it better, faster, clever, and now you ready to commit you changes and share it with a world (or Worlds, depends on your religion), so you have to:

##### a. check status of your changes
To check status (what Git think about you and your work) you have to execute command:
```
git status
```
Within the report Git will show you what files:
* was changed and waiting for add
* was added but was not included in commit request
* was included in commit request, but wasn't sent to your Repository

##### b. add changes to your *commit* request
To add changes you need to execute command:
```
git add {what to add}
```

##### c. make your *commit* request
To commit files you was add step before, you have to execute:
```
git commit -am"{your commentary}"
```

##### d. push your *commit* request to your repository
To push your changes to your web repository, you have to execute:
```
git push origin master
```
*In this step Git will ask your UserName and Password.*

### Updating Parent repository with your changes
TBD for next lesson
