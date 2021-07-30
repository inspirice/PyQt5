import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer 
from PyQt5.QtGui import QMovie

class AnimationScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1080,800)
        
        label_animation = QLabel(self)

        self.movie = QMovie('eyes.gif')
        label_animation.setMovie(self.movie)

        self.startAnimation()

        self.show()

    def startAnimation(self):
        self.movie.start()

app = QApplication(sys.argv)

demo = AnimationScreen()
demo.show()

app.exit(app.exec_())
