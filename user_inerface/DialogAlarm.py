# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4 import QtGui
import sys
from user_inerface.DialogBase import DialogBase

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

class DialogAlarm(DialogBase):
    def setup_ui(self, Dialog, msg):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 80, 251, 71))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslate_ui(Dialog, msg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslate_ui(self, Dialog, msg):
        Dialog.setWindowTitle(_translate("Dialog", "Alarm", None))
        self.label.setText(_translate("Dialog", "%s" % msg, None))

    def show_dialog(self, msg):
        app = QtGui.QApplication(sys.argv)
        form = QtGui.QDialog()
        ui = DialogAlarm()
        ui.setup_ui(form, msg)
        form.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        form = QtGui.QDialog()
        ui = DialogAlarm()
        ui.setup_ui(form, "1")
        form.show()
        sys.exit(app.exec_())
