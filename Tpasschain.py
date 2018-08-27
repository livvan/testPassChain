# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QToolTip, QPushButton, QAction, QTextEdit, QApplication, QMainWindow, QMessageBox, \
  QDesktopWidget, QGridLayout, QWidget


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

  timeExamples()

  newWindow = WindowExample()
  newWindow.show()

  sys.exit(app.exec_())

def timeExamples():
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

class WindowExample(QMainWindow):

  def __init__(self):
    super().__init__()

    self.initDefault()


  def initDefault(self):

    QToolTip.setFont(QFont('SansSerif', 10))

    self.setToolTip('This is a sample window')

    #create menu item
    newAct = QAction('New', self)
    newAct.setShortcut('Ctrl+N')

    saveAct = QAction('Save', self)
    saveAct.setShortcut('Ctrl+S')

    loadAct = QAction('Load', self)
    loadAct.setShortcut('Ctrl+L')

    viewStatAct = QAction('View statusbar', self, checkable=True)
    viewStatAct.setStatusTip('View statusbar')
    viewStatAct.setChecked(True)
    viewStatAct.triggered.connect(self.toggleStatus)

    exitAct = QAction('&Exit', self)
    exitAct.setShortcut('Ctrl+Q')
    exitAct.setStatusTip('Exit application')
    exitAct.triggered.connect(self.close)

    #add menu to menubar
    menubar = self.menuBar()
    mainMenu = menubar.addMenu('&Main')

    #add menu items to menu
    mainMenu.addAction(newAct)
    mainMenu.addAction(saveAct)
    mainMenu.addAction(loadAct)
    mainMenu.addAction(viewStatAct)
    mainMenu.addAction(exitAct)

    #creat text block
    textInput = QTextEdit()

    #create sava button
    saveButton = QPushButton('Save', self)
    saveButton.resize(saveButton.sizeHint())

    #create exit button
    exitButton = QPushButton('Exit', self)
    exitButton.setToolTip('This is a sample <b>Exit</b> button')
    exitButton.resize(exitButton.sizeHint())
    exitButton.setStatusTip('Exit application')
    exitButton.clicked.connect(self.close)

    #create grid layout
    grid = QGridLayout()
    grid.setSpacing(10)

    grid.addWidget(textInput, 0, 0, 1, 4)
    grid.addWidget(saveButton, 1, 2)
    grid.addWidget(exitButton, 1, 3)

    workspaceWidget = QWidget()
    workspaceWidget.setLayout(grid)
    self.setCentralWidget(workspaceWidget)

    self.setGeometry(300, 300, 300, 220)
    self.center()
    self.setWindowTitle('Sample Window')
    self.setWindowIcon(QIcon('sample.png'))

    self.statusBar().showMessage('Ready')

  def center(self):
    selfFrame = self.frameGeometry()
    desktopCenter = QDesktopWidget().availableGeometry().center()
    selfFrame.moveCenter(desktopCenter)
    self.move(selfFrame.topLeft())

  def closeEvent(self, event):

    reply = QMessageBox.question(self, 'Exit', "Are you really want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
      event.accept()
    else:
      event.ignore()

  def toggleStatus(self, state):
    if state:
      self.statusBar().showMessage('Ready')
      self.statusBar().show()
    else:
      self.statusBar().hide()

if __name__ == "__main__":
  main()
