from less_dop_1.task_2.piano_ui import Ui_Form
from PyQt5 import QtCore, QtMultimedia, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import sys

from PyQt5.QtCore import Qt


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.players = None
        self.load_mp3s()
        self.init_buttons()

    def init_buttons(self):
        # main pitches
        self.A.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_Y,
            QtCore.Qt.NoModifier)))
        self.B.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_U,
            QtCore.Qt.NoModifier)))
        self.C.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_Q,
            QtCore.Qt.NoModifier)))
        self.D.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_W,
            QtCore.Qt.NoModifier)))
        self.E.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_E,
            QtCore.Qt.NoModifier)))
        self.F.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_R,
            QtCore.Qt.NoModifier)))
        self.G.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_T,
            QtCore.Qt.NoModifier)))
        # sharps
        self.A_sharp.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_7,
            QtCore.Qt.NoModifier)))
        self.C_sharp.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_2,
            QtCore.Qt.NoModifier)))
        self.D_sharp.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_3,
            QtCore.Qt.NoModifier)))
        self.F_sharp.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_5,
            QtCore.Qt.NoModifier)))
        self.G_sharp.clicked.connect(lambda: app.sendEvent(self, QtGui.QKeyEvent(
            QtGui.QKeyEvent.KeyPress,
            QtCore.Qt.Key_6,
            QtCore.Qt.NoModifier)))

    def load_mp3s(self):
        media = [QtCore.QUrl.fromLocalFile(i) for i in
                 [t for t in os.listdir() if '.mp3' in t]]
        media.sort()
        print(media)
        content = [QtMultimedia.QMediaContent(i) for i in media]
        self.players = [QtMultimedia.QMediaPlayer() for _ in content]
        for i in range(len(content)):
            self.players[i].setMedia(content[i])

    def keyPressEvent(self, event):
        # A
        if event.key() == Qt.Key_Y:
            self.players[0].stop()
            self.players[0].play()
        # B
        elif event.key() == Qt.Key_U:
            self.players[1].stop()
            self.players[1].play()
        # C
        elif event.key() == Qt.Key_Q:
            self.players[2].stop()
            self.players[2].play()
        # D
        elif event.key() == Qt.Key_W:
            self.players[3].stop()
            self.players[3].play()
        # E
        elif event.key() == Qt.Key_E:
            self.players[4].stop()
            self.players[4].play()
        # F
        elif event.key() == Qt.Key_R:
            self.players[5].stop()
            self.players[5].play()
        # G
        elif event.key() == Qt.Key_T:
            self.players[6].stop()
            self.players[6].play()
        # A#
        elif event.key() == Qt.Key_7:
            self.players[7].stop()
            self.players[7].play()
        # C#
        elif event.key() == Qt.Key_2:
            self.players[8].stop()
            self.players[8].play()
        # D#
        elif event.key() == Qt.Key_3:
            self.players[9].stop()
            self.players[9].play()
        # F#
        elif event.key() == Qt.Key_5:
            self.players[10].stop()
            self.players[10].play()
        # G#
        elif event.key() == Qt.Key_6:
            self.players[11].stop()
            self.players[11].play()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
