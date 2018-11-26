# -*- coding: utf-8 -*-

import sys
from os import getenv

from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import QToolTip, QPushButton, QAction, QTextEdit, QApplication, QMainWindow, QMessageBox, \
  QDesktopWidget, QGridLayout, QWidget, QLCDNumber, QSlider, QInputDialog, QFrame, QColorDialog, QFileDialog


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
    actionNew = QAction('New', self)
    actionNew.setStatusTip('New')
    actionNew.setShortcut('Ctrl+N')

    actionSave = QAction('Save', self)
    actionSave.setStatusTip('Save')
    actionSave.setShortcut('Ctrl+S')

    actionLoad = QAction(QIcon('load.png'),'Load', self)
    actionLoad.setStatusTip('Load')
    actionLoad.setShortcut('Ctrl+L')
    actionLoad.triggered.connect(self.showLoadDialog)

    actionToggleStatusBar = QAction('View statusbar', self, checkable=True)
    actionToggleStatusBar.setStatusTip('View statusbar')
    actionToggleStatusBar.setChecked(True)
    actionToggleStatusBar.triggered.connect(self.toggleStatus)

    actionExit = QAction('&Exit', self)
    actionExit.setShortcut('Ctrl+Q')
    actionExit.setStatusTip('Exit application')
    actionExit.triggered.connect(self.close)

    #add menu to menubar
    menubar = self.menuBar()
    menuMain = menubar.addMenu('&Main')

    #add menu items to menu
    menuMain.addAction(actionNew)
    menuMain.addAction(actionSave)
    menuMain.addAction(actionLoad)
    menuMain.addAction(actionToggleStatusBar)
    menuMain.addAction(actionExit)

    #create text block
    textMain = QTextEdit()
    textMain.setMouseTracking(True)

    #create lcd number screen
    lcdnumber = QLCDNumber(self)
    lcdnumber.setMouseTracking(True)

    #create slider
    sliderLcd = QSlider(Qt.Horizontal, self)
    sliderLcd.valueChanged.connect(lcdnumber.display)
    sliderLcd.setMouseTracking(True)

    #create color select button
    buttonColor = QPushButton('Color', self)
    buttonColor.setToolTip('This is sample <b>Color Select Dialog</b> button')
    buttonColor.setToolTip('Select color')
    buttonColor.resize(buttonColor.sizeHint())
    buttonColor.clicked.connect(self.showColorDialog)

    #create save button
    buttonSave = QPushButton('Save', self)
    buttonSave.setToolTip('This is a sample <b>Save</b> button')
    buttonSave.setStatusTip('Save changes')
    buttonSave.resize(buttonSave.sizeHint())
    buttonSave.clicked.connect(self.buttonClicked)

    #create exit button
    buttonExit = QPushButton('Exit', self)
    buttonExit.resize(buttonExit.sizeHint())
    buttonExit.setToolTip('This is a sample <b>Exit</b> button')
    buttonExit.setStatusTip('Exit application')
    buttonExit.clicked.connect(self.close)

    #create color frame
    col = QColor(0, 0, 0)
    self.frameColored = QFrame(self)
    self.frameColored.setStyleSheet("QWidget { background-color: %s }" % col.name())
    self.frameColored.setMouseTracking(True)

    #create grid layout
    grid = QGridLayout()
    #grid.setColumnStretch(5, 5)
    grid.setSpacing(20)

    grid.addWidget(textMain, 0, 0, 1, 2)
    grid.addWidget(lcdnumber, 0, 2, 1, 1)
    grid.addWidget(sliderLcd, 1, 0, 1, 3)
    grid.addWidget(buttonColor, 2, 1)
    grid.addWidget(buttonSave, 2, 2)
    grid.addWidget(buttonExit, 2, 3)
    grid.addWidget(self.frameColored, 0, 3, 2, 1)

    #workspaceWidget = QWidget()
    workspaceWidget = QWidget()
    workspaceWidget.setLayout(grid)
    workspaceWidget.setMouseTracking(True)

    self.showGreetDialog()

    self.setGeometry(300, 300, 300, 220)
    self.center()
    self.setCentralWidget(workspaceWidget)
    #self.setWindowTitle('Sample Window')
    self.setWindowIcon(QIcon('sample.png'))
    self.setMouseTracking(True)

    self.statusBar().showMessage('Ready')

  def center(self):
    selfFrame = self.frameGeometry()
    desktopCenter = QDesktopWidget().availableGeometry().center()
    selfFrame.moveCenter(desktopCenter)
    self.move(selfFrame.topLeft())

  def showGreetDialog(self):
    stringAnswer, boolAnswer = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

    if boolAnswer:
      if stringAnswer == '':
        stringAnswer = 'Placeholder'
      self.setWindowTitle('Sample Window for {}'.format(stringAnswer))
    else:
      self.setWindowTitle('Sample Window')

  def showColorDialog(self):
    color = QColorDialog.getColor()

    if color.isValid():
      self.frameColored.setStyleSheet("QWidget { background-color: %s }" % color.name())

  def showLoadDialog(self):
    fileName = QFileDialog.getOpenFileName(self, 'Load file', getenv('USERPROFILE') + '/Documents')

    if fileName[0]:
      file = open(fileName[0], 'r')

      with file:
        data = file.read()
        self.textEdit.setText(data)

  def closeEvent(self, event):

    reply = QMessageBox.question(self, 'Exit', "Are you really want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
      event.accept()
    else:
      event.ignore()

  def keyPressEvent(self, keyPressed):
    if keyPressed.key() == Qt.Key_Escape:
      self.close()

  def buttonClicked(self):

    self.statusBar().showMessage('\'{}\' button was pressed'.format(self.sender().text()))

  def toggleStatus(self, state):
    if state:
      self.statusBar().showMessage('Ready')
      self.statusBar().show()
    else:
      self.statusBar().hide()

  def mouseMoveEvent(self, e):
    x = e.x()
    y = e.y()

    text = "x: {0},  y: {1}".format(x, y)
    self.statusBar().showMessage(text)


if __name__ == "__main__":
  main()
