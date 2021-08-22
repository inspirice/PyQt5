#หน้าหลักเปิดโปรแกรม
import sys
from PyQt5.QtWidgets import QApplication, QWidget
#function imports
from main_screen import main_screen, grid, vboxLayout

#initiallize GUI Application
app = QApplication(sys.argv)

#window and setting
window = QWidget()
window.setFixedSize(800,480)
window.setStyleSheet("background: #dbeeff;")

main_screen()

window.setLayout(grid)
window.setLayout(vboxLayout)
window.show()
sys.exit(app.exec_())