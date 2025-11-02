from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QPushButton, QVBoxLayout, QLabel
)
app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Generator Number!")
main_window.resize(700, 500)

#lable
lbl_title = QLabel("Press The Button To Generate Number!")
lbl_result = QLabel("????")
btn_generate = QPushButton("Generate!")

#penataan garis panduan
layot_main = QVBoxLayout()
layot_main.addWidget(lbl_title, alignment=Qt.AlignmentFlag.AlignCenter) 
layot_main.addWidget(lbl_result, alignment=Qt.AlignmentFlag.AlignCenter) 
layot_main.addWidget(btn_generate, alignment=Qt.AlignmentFlag.AlignCenter) 

def random_number():
    number = randint(1, 1000)
    lbl_result.setText(str(number))

btn_generate.clicked.connect(random_number)

main_window.setLayout(layot_main)
main_window.show()
app.exec_()