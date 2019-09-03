import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QLineEdit()
        self.initUI()

    def click(self):
        clickedButton = self.sender()
        digitValue = clickedButton.text()
        remain = self.grid.text()
        self.grid.setText(remain+digitValue)

    def click_plus(self):
        clickedButton = self.sender()
        operant = clickedButton.text()
        remain = self.grid.text()
        if remain[-1] != operant:
            self.grid.setText(remain+operant)

    def click_del(self):
        remain = self.grid.text()
        self.grid.setText(remain[:-1])

    def click_enter(self):
        remain = self.grid.text()
        total = eval(remain)
        self.grid.setText(str(total))

    def click_clear(self):
        self.grid.setText('')

    def click_minus(self):
        clickedButton = self.sender()
        operant = clickedButton.text()
        remain = self.grid.text()
        if remain[-1] != operant:
            self.grid.setText(remain+operant)
    
    def click_multiply(self):
        clickedButton = self.sender()
        operant = clickedButton.text()
        remain = self.grid.text()
        if remain[-1] != operant:
            self.grid.setText(remain+operant)

    def click_divide(self):
        clickedButton = self.sender()
        operant = clickedButton.text()
        remain = self.grid.text()
        if remain[-1] != operant:
            self.grid.setText(remain+operant)


    def initUI(self):
        self.grid.setPlaceholderText('0')
        self.grid.setReadOnly(True)
        self.grid.setAlignment(Qt.AlignRight)

        oneButton = QPushButton('1', self)
        oneButton.clicked.connect(self.click)
        twoButton = QPushButton('2', self)
        twoButton.clicked.connect(self.click)
        threeButton = QPushButton('3', self)
        threeButton.clicked.connect(self.click)
        fourButton = QPushButton('4', self)
        fourButton.clicked.connect(self.click)
        fiveButton = QPushButton('5', self)
        fiveButton.clicked.connect(self.click)
        sixButton = QPushButton('6', self)
        sixButton.clicked.connect(self.click)
        sevenButton = QPushButton('7', self)
        sevenButton.clicked.connect(self.click)
        eightButton = QPushButton('8', self)
        eightButton.clicked.connect(self.click)
        nineButton = QPushButton('9', self)
        nineButton.clicked.connect(self.click)
        zeroButton = QPushButton('0', self)
        zeroButton.clicked.connect(self.click)
        delButton = QPushButton('Del')
        delButton.clicked.connect(self.click_del)
        plusButton = QPushButton('+')
        plusButton.clicked.connect(self.click_plus)
        enterButton = QPushButton('Enter')
        enterButton.clicked.connect(self.click_enter)
        clearButton = QPushButton('C')
        clearButton.clicked.connect(self.click_clear)
        minusButton = QPushButton('-')
        minusButton.clicked.connect(self.click_minus)
        multiplyButton = QPushButton('*')
        multiplyButton.clicked.connect(self.click_multiply)
        divideButton = QPushButton('/')
        divideButton.clicked.connect(self.click_divide)
        
        hbox0 = QHBoxLayout()
        hbox0.addStretch(1)
        hbox0.addWidget(plusButton)
        hbox0.addWidget(minusButton)
        hbox0.addWidget(multiplyButton)
        hbox0.addWidget(divideButton)
        hbox0.addStretch(1)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(sevenButton)
        hbox1.addWidget(eightButton)
        hbox1.addWidget(nineButton)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(fourButton)
        hbox2.addWidget(fiveButton)
        hbox2.addWidget(sixButton)
        hbox2.addStretch(1)
        
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(oneButton)
        hbox3.addWidget(twoButton)
        hbox3.addWidget(threeButton)
        hbox3.addStretch(1)
        
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        #zeroButton.resize(50, 200)
        hbox4.addWidget(zeroButton, 200)
        hbox4.addWidget(delButton)
        hbox4.addStretch(1)
        
        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)
        vbox1.addLayout(hbox4)
        vbox1.addStretch(1)
        #self.setLayout(vbox1)

        vbox2 = QVBoxLayout()
        vbox2.addStretch(1)
        vbox2.addWidget(clearButton, 200)
        vbox2.addWidget(enterButton, 200)
        vbox2.addStretch(1)

        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addLayout(vbox1)
        hbox5.addLayout(vbox2)
        hbox5.addStretch(1)
        #self.setLayout(hbox5)

        vbox3 = QVBoxLayout()
        vbox3.addStretch(1)
        vbox3.addWidget(self.grid)
        vbox3.addLayout(hbox0)
        vbox3.addLayout(hbox5)
        vbox3.addStretch(1)
        self.setLayout(vbox3)


        self.setWindowTitle('Num Pad')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
        
