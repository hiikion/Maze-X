import pymem, ctypes
from util.msgbox import msgbox

import util.softExit as softExit


try:
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

except Exception as _except:
    msgbox('Ошибка', str(_except), str("Ошибка."), 0)
    softExit.pExit()