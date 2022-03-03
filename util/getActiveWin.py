from win32gui import GetWindowText, GetForegroundWindow

def gameIsActive():
    return GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive - Direct3D 9"
