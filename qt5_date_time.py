from PyQt5.QtCore import QDate, Qt, QTime

now = QDate.currentDate()
print(now.toString('yyyy-MM-dd'))


time = QTime.currentTime()
print(time.toString())
