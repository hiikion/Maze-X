from util.getOffsets import *
from util.msgbox import *

import datetime

time = "Последнее обновление оффсетов: " + datetime.datetime.utcfromtimestamp(timestamp).strftime("%d.%m.%Y %H:%M")
msgbox('информация', time, 0)