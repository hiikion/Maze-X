from util.getGameAddres import *


def class_id(entity):
    dwClientNetworkable = pm.read_uint(entity + 0x8)
    dwGetClientClassFn = pm.read_uint(dwClientNetworkable + 0x8)
    dwEntityClientClass = pm.read_uint(dwGetClientClassFn + 0x1)
    classID = pm.read_uint(dwEntityClientClass + 0x14)
    return classID

def get_dormant(entity):
    return pm.read_bool(entity + m_bDormant)

