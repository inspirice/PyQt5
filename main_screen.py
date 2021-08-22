from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QMovie, QIcon, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

grid = QGridLayout()
vboxLayout = QVBoxLayout()

widgets = {
    "ani": [],
    "call": [],
    "warn": [],
    "music": [],
    "a1": [],
    "a2": [],
    "a3": [],
    "i1": [],
    "i2": [],
    "i3": [],
    "out": [],
    "out_back": []
}

def clear_widget():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range (0, len(widgets[widget])):
            widgets[widget].pop()

def start_call():
    clear_widget()
    call_screen()

def back_main():
    clear_widget()
    main_screen()

def start_warn():
    clear_widget()
    out_screen()

def start_music():
    clear_widget()
    music_screen()

#********************
#     main
#********************

def main_screen():
    #create eyes animation show
    ani_pic = QMovie('main\e4.gif')
    ani = QLabel()
    ani.setMovie(ani_pic)
    ani.setAlignment(QtCore.Qt.AlignCenter)
    ani_pic.start()

    call = QPushButton()
    call_icon = QPixmap('icon\call.png')
    call.setIcon(QIcon(call_icon))
    call.setText("  โทร")
    call.setStyleSheet(
        "font-size: 20px;"+
        "color: #10359e;"+
        "font: 'TH Sarabun New';"+
        "background-color: #b1d0ec;"+
        "border-radius: 15px;"+
        "padding: 10px;"+
        "icon-size: 30px"
    )
    call.clicked.connect(start_call)

    warn = QPushButton("  ขอความช่วยเหลือ")
    warn_icon = QPixmap('icon\warning_small.png')
    warn.setIcon(QIcon(warn_icon))
    warn.setStyleSheet(
        "font-size: 20px;"+
        "color: #10359e;"+
        "font: 'TH Sarabun New';"+
        "background-color: #b1d0ec;"+
        "border-radius: 15px;"+
        "padding: 10px;"+
        "icon-size: 30px"
    )
    warn.clicked.connect(start_warn)

    music = QPushButton("  เปิดเพลง")
    music_icon = QPixmap('icon\music_small.png')
    music.setIcon(QIcon(music_icon))
    music.setStyleSheet(
        "font-size: 20px;"+
        "color: #10359e;"+
        "font: 'TH Sarabun New';"+
        "background-color: #b1d0ec;"+
        "border-radius: 15px;"+
        "padding: 10px;"+
        "icon-size: 30px"
    )
    music.clicked.connect(start_music)

    widgets["ani"].append(ani)
    widgets["call"].append(call)
    widgets["warn"].append(warn)
    widgets["music"].append(music)

    grid.addWidget(ani,0,0,2,3)
    grid.addWidget(call,3,0,1,1)
    grid.addWidget(warn,3,1,1,1)
    grid.addWidget(music,3,2,1,1)

#********************
#     call
#********************

def call_screen():
    a1 = QLabel()
    a1.setStyleSheet(
        "background-color: #90C695;"+
        "border-radius: 15px;"+
        "font-size: 30px;"+
        "color: 'white';"+
        "font: 'TH Sarabun New';"
        )
    a1.setText("โทรหาคุณลูก")
    a1.setAlignment(QtCore.Qt.AlignCenter)
    widgets["a1"].append(a1)

    a2 = QLabel()
    widgets["a2"].append(a2)

    a3 = QPushButton()
    a3pic = QPixmap("icon\call.png")
    a3.setIcon(QIcon(a3pic))
    a3.setStyleSheet(
        "border-style: outset;"+
        "padding: 10px;"+
        "icon-size: 50px"
    )
    widgets["a3"].append(a3)
    a3.clicked.connect(back_main)
    

    grid.addWidget(a1,0,2,1,3)
    grid.addWidget(a2,1,0,7,7)
    grid.addWidget(a3,7,3,1,1)

#********************
#     activity
#********************

def activity_screen():
    i1 = QLabel()
    i1.setStyleSheet(
        "background-color: #CD5C5C;"+
        "border-radius: 15px;"+
        "font-size: 30px;"+
        "color: 'white';"+
        "font: 'TH Sarabun New';"
        )
    i1.setText("! ! แจ้งเตือนการพักผ่อน ! !")
    i1.setAlignment(QtCore.Qt.AlignCenter)
    widgets["i1"].append(i1)

    i2pic = QPixmap("icon\sleep.png")
    i2 = QLabel()
    i2.setPixmap(i2pic)
    i2.setAlignment(QtCore.Qt.AlignCenter)
    widgets["i2"].append(i2)

    i3 = QLabel()
    i3.setStyleSheet("background-color: #CD5C5C;"+
        "border-radius: 15px;"+
        "font-size: 30px;"+
        "color: 'white';"+
        "font: 'TH Sarabun New';"
        )
    i3.setText("ได้เวลานอนแล้ว")
    i3.setAlignment(QtCore.Qt.AlignCenter)
    widgets["i3"].append(i3)

    grid.addWidget(i1,0,0,1,2)
    grid.addWidget(i2,1,0,4,1)
    grid.addWidget(i3,1,1,4,1)

#********************
#     SOS
#********************

def out_screen():
    out = QLabel()
    out_pic = QPixmap("icon\warning.png")
    out.setPixmap(out_pic)
    out.setAlignment(QtCore.Qt.AlignCenter)
    widgets["out"].append(out)

    out_back = QPushButton()
    out_back.setStyleSheet(
        "border: outset;"+
        "height: 50px;")
    out_back.clicked.connect(back_main)
    widgets["out_back"].append(out_back)


    grid.addWidget(out,0,1)
    grid.addWidget(out_back,1,1)

#********************
#     music
#********************

def music_screen():
    player = QLabel
    player.mediaPlayer = QMediaPlayer()
    videowidget = QVideoWidget()

    openMedia = QPushButton('Open View')

    vboxLayout = QVBoxLayout()
    vboxLayout.addWidget(videowidget)
    vboxLayout.addWidget(openMedia)

    player.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('https://www.youtube.com/watch?v=yeRPkLr1sNA')))
    player.mediaPlayer.play()