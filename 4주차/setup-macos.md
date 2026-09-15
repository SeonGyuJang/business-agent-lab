# Week 3 setup: macOS

Use the macOS Terminal app (Applications > Utilities, or search for Terminal in Spotlight) or the terminal inside VS Code (Terminal > New Terminal, or Control+`). Both run the same shell, zsh. The prompt looks like `user@mac ~ %`.

## 1. Know where you are

```sh
whoami
pwd
echo $HOME
```

A new terminal window normally opens in your home folder, shown as `~`. Run `pwd` to check rather than assume.

Create the folder used for course repositories:

```sh
mkdir -p ~/workspaces
cd ~/workspaces
pwd
```

## 2. Install Git

Check first:

```sh
which git
git --version
```

`which git` prints `/usr/bin/git` when Git is installed, and nothing when it is not.

If macOS asks to install Command Line Tools, approve the installation. If no prompt appears and Git is missing, run:

```sh
xcode-select --install
```

After installation finishes, verify again:

```sh
git --version
```

Apple's Command Line Tools package includes Git. See [Apple's installation guide](https://developer.apple.com/documentation/xcode/installing-the-command-line-tools) and the [Git installation page](https://git-scm.com/install/mac).

## 3. Tell Git who writes your commits

Use your real name and an email address connected to your GitHub account:

```sh
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Check the saved values:

```sh
git config --global user.name
git config --global user.email
```

These values label commits. They are not login credentials.

## 4. Install Claude Code

Run Anthropic's native installer on the stable channel:

```sh
curl -fsSL https://claude.ai/install.sh | bash -s stable
```

Close and reopen the terminal, then verify:

```sh
which claude
claude --version
claude doctor
```

`which claude` should print `/Users/<you>/.local/bin/claude`.

Start Claude Code once and complete the browser sign-in:

```sh
claude
```

Type `/help` to confirm that the session is working, then type `exit` or press `Control-D`.

The native installer and supported login methods are documented in [Claude Code setup](https://code.claude.com/docs/en/setup).

## 5. Final check

```sh
cd ~/workspaces
pwd
which git
git --version
git config --global user.name
git config --global user.email
which claude
claude --version
```

## Troubleshooting

### `claude: command not found`

Close every terminal window and open a new one. If the problem remains, check whether the installer placed the executable in the usual location:

```sh
~/.local/bin/claude --version
```

If that command works, the installer succeeded and the new terminal has not picked up the updated PATH. Follow the PATH section in [Claude Code installation troubleshooting](https://code.claude.com/docs/en/troubleshoot-install). If it does not work, rerun the installer and save its complete output.

### `git` still does not work

Check whether Command Line Tools finished installing:

```sh
xcode-select -p
```

If the command reports no active developer directory, rerun:

```sh
xcode-select --install
```

### Claude sign-in does not finish

Run Claude again and choose the subscription login option. Confirm that the browser uses the account with Claude Code access.
