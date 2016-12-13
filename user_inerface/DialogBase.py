# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from user_inerface.DialogThread import DialogThread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class DialogBase(object):
    """
    线程显示
    """
    def __init__(self):
        self.delay_time = 1

    def setup_ui(self, Dialog, msg):
        pass

    def retranslate_ui(self, Dialog, msg):
        pass

    def set_delay_time(self, delay_time):
        self.delay_time = delay_time

    def get_delay_time(self):
        return self.delay_time

    def show_dialog(self, msg):
        self.showThread = DialogThread(self.get_delay_time())
        self.showThread.finish_signal.connect(self.show_finish)
        self.showThread.start()

    def show_finish(self, result_dict):
        pass
