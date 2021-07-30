import sys
from PyQt5 import QtCore,QtWidgets,Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QMovie,QPixmap

app = QApplication(sys.argv)

window = QWidget()
window.setFixedSize(720,480)
# ใส่สีพื้นหลังเป็นสี Light Cyan
window.setStyleSheet("background: #B0E2FF;")

grid = QGridLayout()

i1 = QLabel()
i1.setStyleSheet(
    "background-color: #CD5C5C;"+
    "border-radius: 15px;"+
    "font-size: 30px;"+
    "color: 'white';"+
    "font: 'TH Sarabun New';"
    )
i1.setText("! ! แจ้งเตือนการทานยา ! !")
i1.setAlignment(QtCore.Qt.AlignCenter)

i2pic = QPixmap("icon\medicine.png")
i2 = QLabel()
i2.setPixmap(i2pic)
i2.setAlignment(QtCore.Qt.AlignCenter)

i3 = QLabel()
i3.setStyleSheet("background-color: #CD5C5C;"+
    "border-radius: 15px;"+
    "font-size: 30px;"+
    "color: 'white';"+
    "font: 'TH Sarabun New';"
    )
i3.setText("ยาฆ่าเชื้อ<br>1 เม็ด")
i3.setAlignment(QtCore.Qt.AlignCenter)

grid.addWidget(i1,0,0,1,2)
grid.addWidget(i2,1,0,4,1)
grid.addWidget(i3,1,1,4,1)

window.setLayout(grid)

window.show()
sys.exit(app.exec_())