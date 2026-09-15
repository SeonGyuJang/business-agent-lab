# Week 3 setup: Windows with Ubuntu on WSL2

VS Code runs as a Windows application. Git, Claude Code, and course projects run inside Ubuntu, a second operating system that runs inside Windows as a virtual machine. You reach its terminal in one of three ways. Connect VS Code to it (section 3). Open the Windows Terminal app and choose the Ubuntu profile. Or open the Ubuntu app from the Start menu. All three run the same shell, bash, and the prompt looks like `user@windows:~$`. A prompt like `PS C:\Users\user>` is PowerShell, which is still Windows. Do not run the course commands there.

## 1. Install Ubuntu

WSL2 is the layer that runs Linux. Ubuntu is the Linux distribution you install on it. Open PowerShell and run:

```powershell
wsl --install -d Ubuntu
```

Restart Windows if it asks. Then open **Ubuntu** from the Start menu once. It asks for a Linux username and a password. Choose both and remember them.

## 2. Confirm WSL2

Open PowerShell and run:

```powershell
wsl --list --verbose
```

The Ubuntu row should show version `2`. If Ubuntu is not running, open it once from the Start menu and finish the username and password setup.

When Ubuntu asks for your password in a terminal, the screen shows no dots or other characters while you type. This is normal.

## 3. Connect VS Code to Ubuntu

1. Open VS Code on Windows.
2. Open Extensions.
3. Install Microsoft's **WSL** extension.
4. Open the Command Palette with `Ctrl+Shift+P`.
5. Run `WSL: Connect to WSL`.
6. Confirm that the lower-left corner shows `WSL: Ubuntu`.
7. Choose **Terminal > New Terminal**.

Verify the integrated terminal:

```sh
uname -s
whoami
pwd
echo $HOME
```

`uname -s` should print `Linux`. See [VS Code's WSL guide](https://code.visualstudio.com/docs/remote/wsl).

## 4. Create the workspaces folder

```sh
mkdir -p ~/workspaces
cd ~/workspaces
pwd
```

Keep course repositories under `~/workspaces`, not under `/mnt/c`. `/mnt/c` is the Windows disk seen from Ubuntu. Files there reach Linux tools through a translation layer, which is slow and breaks permissions. Microsoft gives the same advice for files that Linux tools work on. See [Working across Windows and Linux file systems](https://learn.microsoft.com/en-us/windows/wsl/filesystems).

## 5. Install Git

Inside the Ubuntu terminal in VS Code:

```sh
sudo apt update
sudo apt install -y git curl
which git
git --version
```

`which git` should print `/usr/bin/git`.

## 6. Tell Git who writes your commits

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

## 7. Install Claude Code inside Ubuntu

Do not run this command in PowerShell. Run it in the Ubuntu terminal inside the WSL-connected VS Code window:

```sh
curl -fsSL https://claude.ai/install.sh | bash -s stable
```

Close the integrated terminal and open a new one, then verify:

```sh
which claude
claude --version
claude doctor
```

`which claude` should print `/home/<you>/.local/bin/claude`.

Start Claude Code once and complete the browser sign-in:

```sh
claude
```

Type `/help` to confirm that the session is working, then type `exit` or press `Control-D`.

Anthropic's supported WSL setup is documented in [Claude Code setup](https://code.claude.com/docs/en/setup).

## 8. Final check

The lower-left corner of VS Code should still show `WSL: Ubuntu`. In the integrated terminal, run:

```sh
cd ~/workspaces
pwd
uname -s
which git
git --version
git config --global user.name
git config --global user.email
which claude
claude --version
```

## Troubleshooting

### VS Code does not show `WSL: Ubuntu`

Open the Command Palette and run `WSL: Connect to WSL`. If the command is missing, confirm that Microsoft's WSL extension is installed.

### `code` or the VS Code server fails inside WSL

The course workflow starts from the Windows VS Code application, so `code .` is optional. If the WSL connection itself fails, close VS Code, run `wsl --update` in PowerShell, and try again.

### `claude: command not found`

Close the integrated terminal and create a new one. If the problem remains, run:

```sh
~/.local/bin/claude --version
```

If that command works, the new terminal has not picked up the updated PATH. Use the PATH section in [Claude Code installation troubleshooting](https://code.claude.com/docs/en/troubleshoot-install). If it does not work, rerun the installer and save its complete output.

### Claude browser login does not return to WSL

Return to the Ubuntu terminal and follow the displayed code or URL instructions. The troubleshooting guide covers [OAuth login in WSL](https://code.claude.com/docs/en/troubleshoot-install#oauth-login-fails-in-wsl2-ssh-or-containers).

### WSL itself does not start

Copy the complete error code. Use Microsoft's [WSL troubleshooting guide](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting), then finish the setup with help once the environment works.
