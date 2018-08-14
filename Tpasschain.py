import sys
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


def main():

  # open file on text mode, selecting encoding
  data = open("test.txt", mode = "w", encoding='utf-8')
  # open file in binary mode
  rawdata = open("test", "w+b")

  nowDate = QDate.currentDate()
  nowTime = QTime.currentTime()
  print("current timestamp: {} {}".format(nowDate.toString(Qt.ISODate),nowTime.toString(Qt.DefaultLocaleLongDate)))

  # print out into eviroment
  print("startup arguments: {}".format(sys.argv))
  # write to text file
  data.write("{}".format(sys.argv))
  # write in binary file
  rawdata.write(str.encode("{}".format(sys.argv)))

  sys.exit(0)


if __name__ == "__main__":
  main()
