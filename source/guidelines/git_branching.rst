=============
Git branching
=============

Pull request workflow
=====================

Developers are encouraged to follow the "pull request" workflow described below. It is a lightweight workflow in 9 steps. One of its benefits is the existence of a single long-lived branch in the remote repository. 

Below is an overview of the workflow:

1. Check that your local Git repository displays a single local branch `master` and a single remote-tracking branch `origin/master`

    - `git branch --all`

2. Update the local `master` branch from the remote repository

    - `git pull origin master`

3. Create a local branch; Assume that it has a "short" life time

    - `git branch <branch_name>` 

4. Switch to that short-lived branch

    - `git checkout <branch_name>`

5. Commit the changes

    - `git add <file_name>`
    - `git commit -m <message>`

6. Push your commit(s) to the corresponding remote branch

    - `git push -u origin <branch_name>`

7. Open a pull request on GitHub to merge the remote branch into `master`
8. Discuss your changes with the reviewer(s); Note that “Create a Merge Commit” is turned off to keep a "linear" Git history; Only “Rebase & Merge” and “Squash & Merge” are allowed; After merging, the remote branch is automatically deleted
9. Remove the short-lived local branch & the corresponding remote-tracking branch, and update the local `master` branch

    - `git checkout master`
    - `git branch --delete <branch_name>`
    - `git remote prune origin`
    - `git pull origin master`