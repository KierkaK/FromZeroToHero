# From Zero to Hero
Bellow short instructions how to prepare your work environment to programming classes.

### 1. Create GitHub account
Open the link and follow instructions: https://github.com/join?source=login
I strongly recommend you to use your own email account, not corporate one.

### 2. Download and install GitBash
The tool can be obtained here: https://git-scm.com/download/win
If you have some questions on instalation process fill free to ask me.

### 3. Download and install Python
Yes, we're going to use Python as first programming language for backend. So distributive can be obtained at: https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe . Installation process is simple, but please remember installation folder, you will need it later.

After installation of Python you will need to reboot your PC and update internal Python libraries and install some new. Run following commands from Windows command lime (Win+R -> cmd):
```
pip3 install --upgrade pip
pip3 install jupyter
pip3 install Flask
```
*This list can be updated in future.*

### 4. Download and install IDE
*IDE - is 'Integrated Development Environment'*.
During our classes we will use **PyCharm Community Edition**: https://www.jetbrains.com/pycharm/

### 5. Browser
I also expect to see as your browser Google Chrome of Firefox.

## Setup corporate PROXY
*You need it **only** while you work inside corporate network!*
To setup proxy settings you have to define envirimental variables for your **User** (Win+R -> SystemPropertiesAdvanced). Please add two variables:
| Variable | Value |
|---|---|
| http_proxy | http://pxgot4.srv.volvo.com:8080 |
| https_proxy | http://httppxgot.srv.volvo.com:8080 |
