import sys
# файл назови  main.py
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)

        self.name_label1 = QLabel(self)  # поле с надписью
        self.name_label1.setText("х1: ")
        self.name_label1.move(40, 40)  # .move чтобы двигать по оХ оУ

        self.name_input1 = QLineEdit(self)  # поле для ввода
        self.name_input1.move(90, 40)

        self.name_label2 = QLabel(self)  # поле с надписью
        self.name_label2.setText("х2: ")
        self.name_label2.move(40, 80)  # .move чтобы двигать по оХ оУ

        self.name_input2 = QLineEdit(self)  # поле для ввода
        self.name_input2.move(90, 80)

        self.name_label3 = QLabel(self)  # поле с надписью
        self.name_label3.setText("х3: ")
        self.name_label3.move(40, 120)  # .move чтобы двигать по оХ оУ

        self.name_input3 = QLineEdit(self)  # поле для ввода
        self.name_input3.move(90, 120)

        self.name_label4 = QLabel(self)  # поле с надписью
        self.name_label4.setText("х4: ")
        self.name_label4.move(40, 160)  # .move чтобы двигать по оХ оУ

        self.name_input4 = QLineEdit(self)  # поле для ввода
        self.name_input4.move(90, 160)

        self.label = QLabel(self)
        self.label.resize(150, 50)
        self.label.move(160, 200)


        self.btn = QPushButton('Посчитать', self)
        self.btn.resize(100, 50)
        self.btn.move(40, 200)
        self.btn.clicked.connect(self.func)
    def func(self):
        try:# тут ты получил и тут лучше работать с полученным
            x1 = float(self.name_input1.text()) # Получим текст из поля ввода1
            x2 = float(self.name_input2.text())  # Получим текст из поля ввода2
            x3 = float(self.name_input3.text())  # Получим текст из поля ввода3
            x4 = float(self.name_input4.text())# Получим текст из поля ввода4
            y = x1 + x2 + x3 + x4 # убери свои иксы, и вставь сюда код
            # за место суммы поставь свою операцию
            # тут писать можно
            self.label.setText('')
            self.label.setText(f"Ваш результат: {y}")  # вывод
            print(y)
        except:
            self.label.setText('')
            self.label.setText('Введите 4 числа')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())