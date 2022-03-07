import requests, version, re, webbrowser
from util.msgbox import *

def check_version():
    local_version = version.ver

    try:response = requests.get('https://raw.githubusercontent.com/hiikion/Maze-X/main/version.py').text
    except:
        msgbox.msgbox('Error', 'failed to get latest version', 0)
        response = None

    if response != None:
        github_version = float(re.split('=', response.strip())[1])

        if github_version > local_version:
            msgbox.msgbox('info', 'new cheat version found', 0)
            try:webbrowser.open('https://github.com/hiikion/Maze-X/releases')
            except:pass