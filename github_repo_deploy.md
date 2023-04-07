# Create GitHub Personal Access Token

1. go to settings
![](https://i.imgur.com/7nBIFK5.png)

2. scroll down, find "Developer settings" on the left side
![](https://i.imgur.com/yLoGIIm.png)

3. create personal access tokens (classic)
![](https://i.imgur.com/4axrteS.png)

## How to clone repo with token

#### Option 1: Use GitHub CLI

1. Install GitHub CLI
```shell
type -p curl >/dev/null || sudo apt install curl -y \
&& curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y \
&& gh auth login
```