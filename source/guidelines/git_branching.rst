=============
Git branching
=============

Pull request workflow
=====================

Developers are encouraged to follow the "pull request" workflow described below. It is a lightweight workflow in 9 steps. One of its benefits is the existence of a single long-lived branch in the remote repository. 

Below is an overview of the workflow:

1. Check that your local Git repository displays a single local branch `master`

- `git branch --all`

2. Create a local branch; Assume that this branch will have a short life time

- `git branch <branch>` 

3. Switch to that branch

- `git checkout <branch>`

4. Commit the changes

- `git add .`
- `git commit -m <message>`

5. Push your commit(s) to the corresponding remote branch_name

- `git push -u origin <branch>`

6. Open a pull request on GitHub to merge the remote branch into `master`
7. Discuss your changes with the reviewer(s); Note that “Create a Merge Commit” is turned off to keep well-managed Git histories; Only “Rebase & Merge” and “Squash & Merge” are allowed; After merging, the remote branch is automatically deleted
8. In your local Git repository, switch to `master` and delete the local branch

- `git checkout <branch>` 
- `git branch --delete <branch>`

9. Update the local `master` branch

- `git pull`

