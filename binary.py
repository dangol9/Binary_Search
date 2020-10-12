from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):

    numbers = []
    amount_numbers = int(input("Enter amount of numbers: "))
    i = 0

    while i < amount_numbers:
        i += 1
        number = int(input("Enter {} number: ".format(i)))
        numbers.append(number)

    numbers.sort()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Binary search ")

        self.setGeometry(100, 100, 500, 500)

        self.UiComponents()

        self.show()

    def UiComponents(self):

        self.start = True

        self.label_list = []

        self.desired = int(input("Enter desired number to search: "))

        self.first = 0

        self.last = len(self.numbers) - 1

        self.mid = 0

        c = 0

        for i in self.numbers:

            label = QLabel(str(i), self)

            label.setStyleSheet("border : 1px solid black;" "background : white;" "border-radius: 8px;")

            label.setAlignment(Qt.AlignTop)

            label.setGeometry(50 + c * 30, 50, 20, 20)

            self.label_list.append(label)

            c = c + 1

        self.result = QLabel("To search : " + str(self.desired), self)

        self.result.setGeometry(0, 200, 400, 40)

        self.result.setFont(QFont('Helvetica [Cronyx]', 15))

        self.result.setAlignment(Qt.AlignCenter)

        timer = QTimer(self)

        timer.timeout.connect(self.showTime)

        timer.start(1000)

    def showTime(self):

        if self.start:
            # mid index
            self.mid = (self.first + self.last)//2

            # if first index become greater than last index
            if self.first > self.last:

                self.start = False

                self.result.setFont(QFont('Helvetica [Cronyx]', 15))
                self.result.setStyleSheet("background : red;")
                self.result.setText("Not Found")

            # if mid value is equal to the desired value
            if self.numbers[self.mid] == self.desired:

                self.start = False
                num = self.desired
                self.result.setFont(QFont('Helvetica [Cronyx]', 15))
                self.result.setStyleSheet("background : green;")
                self.result.setText(f"Found number {num} at index : " + str(self.mid))

                self.label_list[self.mid].setStyleSheet("border : 1px solid black;" "border-radius: 10px;" "background-color : green")

            # if not equal to mid value
            else:
                self.label_list[self.mid].setStyleSheet("border : 1px solid black;" "border-radius: 10px;" "background-color : grey")

            # mid value is higher
            if self.numbers[self.mid] > self.desired:
                # change last index
                self.last = self.mid - 1

            # if mid value is smaller
            if self.numbers[self.mid] < self.desired:
                # change first index
                self.first = self.mid + 1

App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
