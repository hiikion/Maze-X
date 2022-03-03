import ctypes

def msgbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, title, text, style)
