# Week 3 setup

Choose the guide for your computer:

* macOS: `setup-macos.md`
* Windows with Ubuntu on WSL2: `setup-windows-wsl.md`

Do not mix the two sets of commands.

## GitHub account

You need a GitHub account before the exercise. On [github.com](https://github.com), choose **Sign up**: use an email address you can open in class, pick a username (it is public and becomes part of every repository URL), verify the email, and stay on the free plan. Use the same email later in `git config --global user.email`.

## Ready means

By the end of setup, you should be able to show:

```sh
which git
git --version
git config --global user.name
git config --global user.email
which claude
claude --version
```

`which` prints where the shell found a command. A printed version means it runs.

You should also have a `workspaces` folder inside your home folder.

Windows students should be working in a VS Code window connected to `WSL: Ubuntu`. Their integrated terminal should report `Linux` when they run:

```sh
uname -s
```

## If something fails

Copy the complete error message before you change anything. Compare your output with your group, then use the troubleshooting section of your platform guide.

