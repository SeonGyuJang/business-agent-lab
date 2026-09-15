# Week 3 exercise: Build a workspace you control

**Not graded.** This is the setup you will use for the rest of the course. Do it for yourself, and get help until it works.

## Goal

Create a public `business-agent-lab` repository, complete one Git cycle manually (edit, inspect, add, commit, push, recover), ask a peer to verify it, then let Claude Code make one bounded change that you inspect yourself.

Do not start Claude Code until a classmate has checked your work (see the peer checkpoint below).

## Part 1: Create the remote repository

On GitHub, signed in (the setup page explains how to create an account):

1. Choose **New repository** from the + menu, top right.
2. Name it `business-agent-lab`, exactly.
3. Keep it **Public**.
4. Tick **Add a README file**, then **Create repository**.
5. Copy its HTTPS URL from the green **Code** button.

## Part 2: Clone and open the repository

### Goal

Place the GitHub repository inside your `workspaces` folder.

### Command

Replace `USERNAME` with your GitHub username:

```sh
cd ~/workspaces
git clone https://github.com/USERNAME/business-agent-lab.git
cd business-agent-lab
pwd
git remote -v
```

### Check

The current path should end in `business-agent-lab`. The remote named `origin` should point to your GitHub repository.

Open the folder in VS Code with **File > Open Folder**. Windows students should remain in the window marked `WSL: Ubuntu`.

## Part 3: Make a local change

Edit `README.md` so it contains:

```md
# Business Agent Lab

## What I want to build with agents

Write one or two sentences in your own words.
```

Save the file.

### Goal

See what changed before saving it to Git history.

### Command

```sh
git status
git diff
```

### Check

`README.md` should be modified. The diff should show only the words you intended to change.

## Part 4: Stage the change

### Predict

Before running the command, say what you expect `git status` to report afterward.

### Command

```sh
git add README.md
git status
git diff --staged
```

### Check

`README.md` should appear under **Changes to be committed**. The staged diff should show the version that will enter the next commit.

## Part 5: Commit the change

### Predict

Will this command send the change to GitHub, or save it only in the local repository?

### Command

```sh
git commit -m "Add course project goal"
git log --oneline
```

### Check

The new commit should appear at the top of the log. It exists locally and is not yet on GitHub.

## Part 6: Push the commit

### Predict

Which place will change: the working files, staging area, local repository, or GitHub?

### Command

```sh
git push
```

VS Code may open a browser and ask you to sign in to GitHub. Complete the sign-in, return to VS Code, and rerun `git push` if necessary.

### Check

Refresh the repository page on GitHub. The README and latest commit should be visible there.

## Part 7: Recover an unwanted edit

Add an unwanted sentence to the local `README.md` and save it.

### Predict

What should remain after restoring the file: the last committed version or the unwanted sentence?

### Command

```sh
git diff
git restore README.md
git status
```

### Check

The unwanted sentence should be gone. `git status` should report a clean working tree.

## Peer checkpoint

Work with your group. Do not start Claude Code until a classmate confirms every item:

- [ ] The public repository is named `business-agent-lab`.
- [ ] The expected README is visible on GitHub.
- [ ] `git log --oneline` shows the student's commits.
- [ ] `git status` reports a clean working tree.
- [ ] The student can explain what `add`, `commit`, and `push` changed.

Peer checker: ______________________________

## Part 8: Let Claude Code make one bounded change

Start Claude Code inside the repository:

```sh
claude
```

Give it this task:

> Read `README.md`. Add a short section titled "Working with agents" with one sentence about how I will use coding agents in this course. Do not change anything else.

Review the permission request before you approve it. After Claude finishes, run `/context` to see what filled the context window, then `/exit`.

Inspect the result:

```sh
git diff
```

Choose one path:

### Keep the change

```sh
git add README.md
git commit -m "Add working agreement"
git push
```

### Discard the change

```sh
git restore README.md
```

Finish with:

```sh
git status
claude --version
```

The working tree must be clean.

## Finish

Nothing to submit. You are done when:

1. `git status` reports a clean working tree;
2. `claude --version` prints a version; and
3. a peer has seen your `git diff` and your keep-or-restore decision.

Windows students: the lower-left corner of VS Code still says `WSL: Ubuntu`.
