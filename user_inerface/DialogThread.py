# -*- coding: utf-8 -*-

from PyQt4 import QtCore
import time

class DialogThread(QtCore.QThread):
    finish_signal = QtCore.pyqtSignal(dict)

    def __init__(self, delay_timer, parent = None):
        super(DialogThread, self).__init__(parent)
        self.delay_timer = delay_timer

    def run(self):
        time.sleep(self.delay_timer)
        # 通知显示结束了
        self.finish_signal.emit({})
