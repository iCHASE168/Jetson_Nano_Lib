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
2. Follow the screenshot, then enter your token
![](https://i.imgur.com/GT1wQwe.png)
![](https://i.imgur.com/pJzA3D3.png)
![](https://i.imgur.com/WPKGiPO.png)
![](https://i.imgur.com/wvzVQ8M.png)
![](https://i.imgur.com/MzSoTFX.png)

#### Option 2: git clone directly and use token as your GitHub password to login
> Note: with this method, you have to re-enter (re-login) your token whenever you want to do any action such as pull or push