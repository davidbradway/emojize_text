# Emoji

## Setup

```bash
# Update to Python3.6 in Windows Subsytem for Linux
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt update
sudo apt install python3.6

#virtualenv -p python3 env
python3.6 -m venv env --without-pip
source env/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python3
pip3 install -r requirements.txt

jupyter lab
# or
python emojize_text.py
```
