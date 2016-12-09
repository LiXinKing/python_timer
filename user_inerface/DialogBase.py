# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

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
    def setup_ui(self, Dialog, msg):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(20, 20)
        self.retranslate_ui(Dialog, msg)

    def retranslate_ui(self, Dialog, msg):
        Dialog.setWindowTitle(_translate("Dialog", "Test", None))

    def show_dialog(self, msg):
        app = QtGui.QApplication(sys.argv)
        form = QtGui.QWidget()
        ui = DialogBase()
        ui.setup_ui(form, "msg")
        form.show()
        sys.exit(app.exec_())
