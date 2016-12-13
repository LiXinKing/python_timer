# -*- coding: utf-8 -*-
import threading
from user_inerface.DialogAlarm import DialogAlarm

g_DialogType2Func = {
    "DialogAlarm" : DialogAlarm
}

# TODO:add a QtThread to fix Dialog show error http://blog.csdn.net/mr_zing/article/details/46945011
class DialogManagement(object):
    @classmethod
    def show_Dialog(cls, msg, type):
        func = g_DialogType2Func.get(type, None)
        if func is not None:
            func().show_dialog(msg)
