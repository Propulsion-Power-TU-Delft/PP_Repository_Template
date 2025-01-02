# Basic Git Instructions for Collaborative Development

| Author  | E.C.Bunschoten  |
|------|------|
| Year  | 2025  |
| Group  | FPT  |

Keeping track of changes in code is hard enough for a project with one member. With multiple contributers, it can become very chaotic very quickly! GitHub offers a solution to this problem by keeping track of changes in code files, allowing for multiple contributers to work on the same code. This document provides some basic tips and tricks for code development using Git.

## Getting Started

In order to use Git effectively, first you need to create a GitHub account. On the [GitHub webpage](https://github.com), create an account on your name.

Next, you need to install Git onto your system. GitHub has a useful [desktop application](https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop) for Windows and MacOS, but not for Linux. General installation instructions for Git can be found [here](https://github.com/git-guides/install-git). 

## The git repository

Git allows for consistent, collaborative code development. The code and development history are shared through a *repository*. A new repository can be [created from scratch](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories), [duplicated](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository), or [forked](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo), depending on the aim of the project. Once a repository has been created, it can be shared to other collaborators through [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). For your thesis or project, you can duplicate this template repository and bring it under your name and set your own rules.

Every git repository has at least one owner and within the repository, rules and permissions apply. These rules enable who can or can't contribute to the project and include security tokens which have to be used for pushing or changes to versions of the code. 

## Synchronization
Once you have the repository code onto your system, the collaborative development can start. This takes the form of synchronizing your *local* code with the *cloud*. Updating the code on your local machine is done through a so-called **pull**, while updating the cloud with the changes you made locally is done through a **push**. Here follows a recommended recipe for updating your repository with your local changes:

1. **Update repository:** Before making any new changes, update your local repository settings with those of the cloud.
```
git remote update <repo name>
```
2. **Update branch:** ensure that the version of the code you are working on is up-to-date by performing a pull. Here, the branch \<branch name\> is updated.
```
git pull <repo name> <branch name>
```
3. **Implement changes:** write new code, generate new files, etc.

4. **Add new files (if any):** If you add new files to your project and want them to be synchronized with your repository, they need to be added through git. This can be done through
```
git add <file names>
```

5. **Commit changes:** By default, all changes you make to the code are ignored by git. Only by *commiting* your changes are those changes registered in the repository history. Each commit has a label which makes managing the code history very convenient and has a *message* attached which briefly summarizes the changes in the commit. It is recommended to make commits for each individual file that has been changed as shown in this example:
```
git commit <file 1> -m"commit message 1"
git commit <file 2> -m"commit message 2"
git commit <file 3> -m"commit message 3"
...
```
It is possible, although **not recommended** to simultaneously commit all changed files with a single commit:
```
git commit -am"commit message"
```
The reason for this is that sometimes new, hidden files may be created such as caches, binaries, and hidden files from your code editor. By committing all files, these hidden files may be included in your repository which could fill up your repository quickly if you are not careful. In addition, it is much easier to back-track changes in your code when files are committed individually. 

6. **Update repository and branch again:** Before making a push, ensure that your repository has been updated according to the changes of your collaborators. While you were implementing new features into your code, it could be that others have been pushing new features as well.
```
git remote update <repo name>
git pull <repo name> <branch name>
```

7. **Resolve conflicts (if any):** Resolve any conflicts if present (more on this later).

8. **Push changes:** Now your local code can be safely pushed to the cloud and shared with your collaborators. 
```
git push <repo name> <branch name>
```

Even when working on your own, it is recommended to follow these development instructions as it yields some benefits:

- **Back-up:** By regularly synchornizing your local code with the cloud, you are creating a back-up. In case you lose access to your computer, you can still access the code from a new machine as long as you can log in to your github account.

- **Device synchonization:** By using git, it is very easy to synchonize changes in your code across multiple devices. You can have a copy of your code on your own laptop, TU Delft workstation and on DelftBlue and keep them all up-to-date by updating the repository on a regular basis. No need for copying of individual files.

- **Reverting changes:** The code history of your repository allows you to back-track in case something breaks in your code. For every file in the repository, git allows you to display its history per commit and allows you to revert back to these commits accordingly. 

Different versions of the code within a repository are called *branches*. When a repository is created, Git generates a default branch under the name "main" (legacy "master"). When cloning a repository onto your system, it by default checks out the "main" branch. Typically, branches are used for release versions of the code and the development of new features. An existing branch (in this example named "branch1") of the code in the repository can be accessed by navigating to the repository folder on your system and is acceessed
```
git checkout branch1
```
```
git checkout -b newbranch
```
