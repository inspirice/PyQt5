# PyQt5 without QT design
Python with PyQt5 Gui

Using PyQt5 tools, manage GUI pages without QT Design.
Use QGridlayout class for arranging widgets in rows and columns.

![image](https://user-images.githubusercontent.com/29938751/128553014-790f0c13-23da-49d4-9ea7-902bd238738e.png)

Use the addWidget command to add a widget that you want to create a page with (name widget,row,colunm,rowSpan,columnSpan).

Example in gridcolunm.py

grid.addWidget(box5,2,0,1,2)
grid.addWidget(box6,3,0,1,3)

rowSpan is row merging, If you enter 1, you only need 1 square in the table. If you enter 2, you want to combine the 2 fields in that row.
ColumnSpan is column merging, If you enter 1, you only need 1 square in the table. If you enter 2, you want to combine the 2 fields in that column.

