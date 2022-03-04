import pymem, ctypes
from util.msgbox import msgbox
from util.getOffsets import *
import util.softExit as softExit


try:
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    engine_pointer = pm.read_uint(engine + dwClientState)

except Exception as _except:
    msgbox('Ошибка', str(_except), str("Ошибка."), 0)
    softExit.pExit()