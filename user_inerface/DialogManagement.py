# -*- coding: utf-8 -*-
import threading
from user_inerface.DialogAlarm import DialogAlarm

g_DialogType2Func = {
    "DialogAlarm" : DialogAlarm
}

class DialogManagement(object):
    @classmethod
    def show_Dialog(cls, msg, type):
        func = g_DialogType2Func.get(type, None)
        if func is not None:
            func().show_dialog(msg)
