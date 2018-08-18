# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox


def main():
  app = QApplication(sys.argv)

  # open file on text mode, selecting encoding
  data = open("test.txt", mode = "w", encoding='utf-8')
  # open file in binary mode
  rawdata = open("test", "w+b")

  # print out into eviroment
  print()
  print("startup arguments: {}".format(sys.argv))
  print()
  # write to text file
  data.write("{}".format(sys.argv))
  # write in binary file
  rawdata.write(str.encode("{}".format(sys.argv)))

  timeExmaples()

  newWindow = WindowExample()
  newWindow.show()

  sys.exit(app.exec_())

def timeExmaples():
  now = QDateTime.currentDateTime()

  print("Timestamp: {}".format(now.toSecsSinceEpoch()))
  print("Local datetime: {}".format(now.toString(Qt.ISODate)))
  print("Universal datetime: {}".format(now.toUTC().toString(Qt.ISODate)))
  print("The offset from UTC is: {} hours".format(now.offsetFromUtc()/3600))

  print("Time zone: {0}".format(now.timeZoneAbbreviation()))
  if now.isDaylightTime():
    print("The current date falls into DST time")
  else:
    print("The current date does not fall into DST time")

class WindowExample(QWidget):

  def __init__(self):
    super().__init__()

    self.initDefault()


  def initDefault(self):
    QToolTip.setFont(QFont('SansSerif', 10))

    self.setToolTip('This is a sample window')

    exitButton = QPushButton('Exit', self)
    exitButton.setToolTip('This is a sample <b>Exit</b> button')
    exitButton.resize(exitButton.sizeHint())
    exitButton.move(50, 50)
    exitButton.clicked.connect(self.close)

    self.setGeometry(300, 300, 300, 220)
    self.setWindowTitle('Sample Window')
    self.setWindowIcon(QIcon('sample.png'))

  def closeEvent(self, event):

    reply = QMessageBox.question(self, 'Exit', "Are you really want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
      event.accept()
    else:
      event.ignore()


if __name__ == "__main__":
  main()
