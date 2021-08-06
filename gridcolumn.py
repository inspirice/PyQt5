import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

app = QApplication(sys.argv)

window = QWidget()
window.setFixedSize(720,480)
window.setStyleSheet("background: #E9967A;")

grid = QGridLayout()

box1 = QLabel()
box1.setStyleSheet(
    "background-color: #008B45;"+
    "border-radius: 15px;"+
    "font-size: 20px;"+
    "color: 'white';"
    )
box1.setText("0,0,1,1")
box1.setAlignment(QtCore.Qt.AlignCenter)

box2 = QLabel()
box2.setStyleSheet(
    "background-color: #008B45;"+
    "border-radius: 15px;"+
    "font-size: 20px;"+
    "color: 'white';"
    )
box2.setText("1,0,1,1")
box2.setAlignment(QtCore.Qt.AlignCenter)

box3 = QLabel()
box3.setStyleSheet(
    "background-color: #008B45;"+
    "border-radius: 15px;"+
    "font-size: 20px;"+
    "color: 'white';"
    )
box3.setText("2,0,1,1")
box3.setAlignment(QtCore.Qt.AlignCenter)

box4 = QLabel()
box4.setStyleSheet(
    "background-color: #008B45;"+
    "border-radius: 15px;"
    "font-size: 20px;"+
    "color: 'white';"
    )
box4.setText("3,0,1,1")
box4.setAlignment(QtCore.Qt.AlignCenter)

box5 = QLabel()
box5.setStyleSheet("background-color: #008B45;"+
    "border-radius: 15px;"
    "font-size: 20px;"+
    "color: 'white';"
    )
box5.setText("0,1,2,1")
box5.setAlignment(QtCore.Qt.AlignCenter)

box6 = QLabel()
box6.setStyleSheet("background-color: #008B45;"+
    "border-radius: 15px;"
    "font-size: 20px;"+
    "color: 'white';"
    )
box6.setText("0,2,3,1")
box6.setAlignment(QtCore.Qt.AlignCenter)

box7 = QLabel()
box7.setStyleSheet("background-color: #008B45;"+
    "border-radius: 15px;"
    "font-size: 20px;"+
    "color: 'white';"
    )
box7.setText("0,3,4,1")
box7.setAlignment(QtCore.Qt.AlignCenter)

grid.addWidget(box1,0,0,1,1)
grid.addWidget(box2,1,0,1,1)
grid.addWidget(box3,2,0,1,1)
grid.addWidget(box4,3,0,1,1)
grid.addWidget(box5,0,1,2,1)
grid.addWidget(box6,0,2,3,1)
grid.addWidget(box7,0,3,4,1)

window.setLayout(grid)

window.show()
sys.exit(app.exec_())