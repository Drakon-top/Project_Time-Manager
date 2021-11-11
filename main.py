import sys
import sqlite3
import random
from PySide2 import *
from interface import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Math")
        self.ui.first.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.first_page))
        self.ui.second.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.second_page))
        self.ui.third.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.third_page))
        self.ui.forth.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.forth_page))
        self.ui.six.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.six_page))
        self.ui.seven.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.seven_page))
        self.ui.task_but.clicked.connect(self.task_start)

        self.ui.otvet_test.clicked.connect(self.proverka)
        self.ui.new_task.clicked.connect(self.task_create)
        self.show()

    def task_start(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.task)
        self.task_create()

    def task_create(self):
        con = sqlite3.connect("tests.db")
        num = self.ui.comboBox_number.currentText()
        res = con.cursor().execute(
            "SELECT * FROM tasks WHERE number == ?", (int(num),)).fetchall()
        _tsk = random.choice(res)
        self.otvet = float(_tsk[4])
        self.ui.labe_text.setText(_tsk[2])
        self.ui.label_image.setPixmap(QPixmap(u":/newPrefix/pict/{}".format(_tsk[3])))

    def proverka(self):
        try:
            num = float(self.ui.line_otvet.text())
            if self.otvet == num:
                self.ui.label_true.setText("Верно")
            else:
                self.ui.label_true.setText("Не верно(")
        except:
            self.ui.label_true.setText("Неверный ввод(")




if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec_())
