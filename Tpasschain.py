import sys

from PyQt5.QtCore import QDateTime, Qt


def main():
  print()

  # open file on text mode, selecting encoding
  data = open("test.txt", mode = "w", encoding='utf-8')
  # open file in binary mode
  rawdata = open("test", "w+b")

  # print out into eviroment
  print("startup arguments: {}".format(sys.argv))
  print()
  # write to text file
  data.write("{}".format(sys.argv))
  # write in binary file
  rawdata.write(str.encode("{}".format(sys.argv)))

  timeExmaples()

  sys.exit(0)

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


if __name__ == "__main__":
  main()
