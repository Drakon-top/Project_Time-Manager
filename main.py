import sys
import os
import datetime
import sqlite3

from PySide2 import *
from ui_interface import *
from PySide2 import QtGui
from PySide2 import QtCore

Color_light = [(255, 255, 243), (221, 255, 255), (0, 0, 0), (166, 246, 255), u"QPushButton{\n"
                                                                             "background-color: rgb(0, 0, 0, 0);\n"
                                                                             "border: none;\n"
                                                                             "}\n"
                                                                             "QFrame{\n"
                                                                             "background-color: rgb(0, 0, 0, 0);\n"
                                                                             "}\n"
                                                                             "QWidget{\n"
                                                                             "	color: rgb(0, 0, 0);\n"
                                                                             "}", "::section{Background-color:rgb(255,255,255)}", (255, 255, 255)]
Color_dark = [(0, 47, 49), (0, 84, 93), (255, 255, 255), (41, 93, 117), u"QPushButton{\n"
                                                                        "background-color: rgb(0, 0, 0, 0);\n"
                                                                        "border: none;\n"
                                                                        "}\n"
                                                                        "QFrame{\n"
                                                                        "background-color: rgb(0, 0, 0, 0);\n"
                                                                        "}\n"
                                                                        "QWidget{\n"
                                                                        "	color: rgb(193, 255, 222);\n"
                                                                        "}", "::section{Background-color:rgb(51, 40, 68)}", (56, 36, 57)]


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Настройки окна
        # Для темной темы, списки QLabel
        self.list_widget_extreme = [self.ui.top_widget, self.ui.left_body, self.ui.right_body]
        self.list_widget_body = [self.ui.bottom_widget, self.ui.header_body]
        self.list_text = [self.ui.text_deal, self.ui.text_home, self.ui.text_deal,
                          self.ui.text_proces, self.ui.text_progress, self.ui.text_purpose,
                          self.ui.text_complet, self.ui.text_version, self.ui.text_label_name,
                          self.ui.text_not_complet, self.ui.text_page_purpose, self.ui.url_yandex]
        self.list_table = [self.ui.table_purpouse, self.ui.table_task, self.ui.table_subtask,
                           self.ui.table_task_deal]
        self.line_combo_widget = [self.ui.line_edit_pur_id, self.ui.line_edit_task,
                                  self.ui.line_edit_subtask, self.ui.combo_box_task,
                                  self.ui.comboBox_pur_impo, self.ui.combo_box_suptask_zel,
                                  self.ui.plain_text_for_pur]
        self.changeTitle(False)

        self.ui.checkBox_drak_tem.stateChanged.connect(self.changeTitle)
        self.ui.check_box_every_day.stateChanged.connect(self.evryday_connect)
        self.flag_set_suprose_every = False
        self.setWindowTitle("Time Manager")
        self.connection = sqlite3.connect("purpose_db.db")
        res = self.connection.cursor().execute(
            "SELECT name FROM purposes WHERE completed == false").fetchall()
        self.ui.combo_box_suptask_zel.addItems([i[0] for i in res])
        self.ui.url_yandex.setText(
            '<a href="https://yandexlyceum.ru/" style="color:rgb(94, 255, 209)"> for Yandex Lyceum </a>')
        self.ui.url_yandex.setOpenExternalLinks(True)

        # add task, pur, sub
        self.ui.button_completed_pur.clicked.connect(self.purpose_update)

        self.ui.but_home.clicked.connect(lambda: self.slide_menu_left())
        self.ui.button_add_podzadacha.clicked.connect(self.add_suptask)
        self.ui.butt_add_purpouse.clicked.connect(self.add_purpos)
        self.ui.button_add_task.clicked.connect(self.add_task)
        self.ui.button_complet_task.clicked.connect(self.task_update)
        self.ui.button_complet_subtask.clicked.connect(self.subtask_update)
        res = self.connection.cursor().execute(
            "SELECT name FROM subtasks WHERE completed == false").fetchall()
        self.ui.combo_box_task.addItems([i[0] for i in res])
        self.draw_page_del()
        # self.draw_page_purpose()

        # основные 3 кнокпи
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.restore_button.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.close_button.clicked.connect(lambda: self.close())

        # connect page
        self.ui.button_purpose.clicked.connect(self.draw_page_purpose)
        self.ui.button_Add.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_page))
        self.ui.button_task.clicked.connect(self.draw_page_del)
        self.ui.button_deal.clicked.connect(self.draw_progress_page)

        # сортировка таблицы целей
        self.list_reverse = [False] * 7
        self.ui.sort_name.clicked.connect(lambda: self.draw_page_purpose(1))
        self.ui.sort_importanse.clicked.connect(lambda: self.draw_page_purpose(2))
        self.ui.sort_date_start.clicked.connect(lambda: self.draw_page_purpose(3))
        self.ui.sor_date_end.clicked.connect(lambda: self.draw_page_purpose(4))
        self.ui.sort_complet.clicked.connect(lambda: self.draw_page_purpose(6))

        self.draw_page_purpose()
        self.show()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def evryday_connect(self, state):
        if state == Qt.Checked:
            self.flag_set_suprose_every = True
            self.ui.text_date_end_sup.setVisible(False)
            self.ui.date_suptask.setVisible(False)
        else:
            self.flag_set_suprose_every = False
            self.ui.text_date_end_sup.setVisible(True)
            self.ui.date_suptask.setVisible(True)

    def add_suptask(self):
        name = self.ui.text_name_suptask.text()
        name_purpose = self.ui.combo_box_suptask_zel.currentText()
        con = sqlite3.connect("purpose_db.db")
        cur = con.cursor()
        if not self.flag_set_suprose_every:
            dates = " ".join(list(map(str, list(self.ui.date_suptask.date().getDate()))))
            cur.execute("""INSERT INTO 
            subtasks(name, for_purpouse, everyday, date) 
            VALUES (?, ?, ?, ?)""", (name, name_purpose, False, dates))
        else:
            cur.execute("""INSERT INTO 
            subtasks(name, for_purpouse, everyday) 
            VALUES (?, ?, ?)""", (name, name_purpose, True))
        con.commit()
        self.ui.text_console.setText("Add subtasks!")
        # importanse = self.ui.comboBox_sup_impo.currentText()
        self.connection = sqlite3.connect("purpose_db.db")
        res = self.connection.cursor().execute(
            "SELECT name FROM subtasks WHERE completed == false").fetchall()
        self.ui.combo_box_task.clear()
        self.ui.combo_box_task.addItems([i[0] for i in res])
        self.show()
        # for_what = self.ui.plain_text_for.toPlainText()

    def add_purpos(self):
        name = self.ui.text_name_pur.text()
        impotance = self.ui.comboBox_pur_impo.currentText()
        for_what = self.ui.plain_text_for_pur.toPlainText()
        con = sqlite3.connect("purpose_db.db")
        date_now = datetime.datetime.now().strftime("%Y %m %d")
        # date_now = date_now.replace(" ", ".")
        cur = con.cursor()
        dates = " ".join(list(map(str, list(self.ui.date_suptask.date().getDate()))))
        cur.execute("""INSERT INTO 
        purposes(name, importance, date_start, date_end, for_what) 
        VALUES (?, ?, ?, ?, ?)""", (name, int(impotance), date_now, dates, for_what))
        con.commit()
        self.ui.text_console.setText("Add purpose!")

        self.connection = sqlite3.connect("purpose_db.db")
        res = self.connection.cursor().execute(
            "SELECT name FROM purposes WHERE completed == false").fetchall()
        self.ui.combo_box_suptask_zel.clear()
        self.ui.combo_box_suptask_zel.addItems([i[0] for i in res])

        self.show()

    def add_task(self):
        name = self.ui.text_name_pur.text()
        subtask = self.ui.combo_box_task.currentText()
        times = self.ui.datetime_task.time().toString()[:5]
        dates = " ".join(list(map(str, list(self.ui.datetime_task.date().getDate()))))
        con = sqlite3.connect("purpose_db.db")
        cur = con.cursor()
        cur.execute("""INSERT INTO 
                tasks(name, for_subtask, date, time) 
                VALUES (?, ?, ?, ?)""", (name, subtask, dates, times))
        con.commit()
        self.ui.text_console.setText("Add task!")
        self.show()

    def draw_page_purpose(self, n=0):
        self.ui.stackedWidget.setCurrentWidget(self.ui.goal_page)
        self.connection = sqlite3.connect("purpose_db.db")
        res = self.connection.cursor().execute("SELECT * FROM purposes").fetchall()
        res = self.sort_res_sup(res, n)
        self.ui.table_purpouse.setColumnCount(7)
        self.ui.table_purpouse.setRowCount(0)
        date_now = datetime.datetime.now().strftime("%Y %m %d")
        now = datetime.date(int(date_now.split()[0]), int(date_now.split()[1]),
                            int(date_now.split()[2]))
        not_done = 0
        for i in range(len(res)):
            self.ui.table_purpouse.setRowCount(
                self.ui.table_purpouse.rowCount() + 1)
            if res[i][6]:
                pass
                # self.ui.table_purpouse.s
            dat = res[i][4]
            end = datetime.date(int(dat.split()[0]), int(dat.split()[1]), int(dat.split()[2]))
            for j, elem in enumerate(res[i]):
                self.ui.table_purpouse.setItem(
                    i, j, QTableWidgetItem(str(elem)))
                if j == 6:
                    if res[i][6]:
                        self.ui.table_purpouse.item(i, j).setBackground(QtGui.QColor(0, 248, 32))
                    else:
                        if now > end:
                            self.ui.table_purpouse.item(i, j).setBackground(QtGui.QColor(188, 0, 6))
                            not_done += 1

        # lcd
        self.ui.lcd_pur_com.display(len(list(filter(lambda x: x[6] == 1, res))))
        self.ui.lcd_pur_now.display(
            len(res) - not_done - len(list(filter(lambda x: x[6] == 1, res))))
        self.ui.lcd_pur_overd.display(not_done)

    def draw_progress_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.progress_page)
        self.connection = sqlite3.connect("purpose_db.db")
        res = self.connection.cursor().execute("SELECT * FROM tasks").fetchall()
        res = sorted(res, key=lambda x: x[4])
        self.ui.table_task_deal.setColumnCount(6)
        self.ui.table_task_deal.setRowCount(0)
        date_now = datetime.datetime.now().strftime("%Y %m %d")
        now = datetime.date(int(date_now.split()[0]), int(date_now.split()[1]),
                            int(date_now.split()[2]))
        times = datetime.datetime.now().time().strftime("%H:%M")
        n = 0
        complet = 0
        overdue = 0
        for i in range(len(res)):
            dat = res[i][3]
            end = datetime.date(int(dat.split()[0]), int(dat.split()[1]), int(dat.split()[2]))
            if now != end:
                continue
            self.ui.table_task_deal.setRowCount(
                self.ui.table_task_deal.rowCount() + 1)
            for j, elem in enumerate(res[i]):
                self.ui.table_task_deal.setItem(
                    n, j, QTableWidgetItem(str(elem)))
                if j == 5:
                    if res[i][j]:
                        self.ui.table_task_deal.item(n, j).setBackground(QtGui.QColor(0, 248, 32))
                        complet += 1
                    else:
                        if times > res[i][4]:
                            self.ui.table_task_deal.item(n, j).setBackground(QtGui.QColor(188, 0, 6))
                            overdue += 1
            n += 1

        # lcd
        self.ui.lcd_task_complet.display(complet)
        self.ui.lcd_task_now.display(n - complet - overdue)
        self.ui.lcd_task_notcomplet.display(overdue)

    def sort_res_sup(self, res, n=0):
        self.list_reverse[n] = not self.list_reverse[n]
        if n == 3:
            new_res = sorted(res,
                             key=lambda x: datetime.date(int(x[3].split()[0]), int(x[3].split()[1]),
                                                         int(x[3].split()[2])),
                             reverse=not self.list_reverse[n])
            return new_res
        if n == 4:
            new_res = sorted(res,
                             key=lambda x: datetime.date(int(x[4].split()[0]), int(x[4].split()[1]),
                                                         int(x[4].split()[2])),
                             reverse=not self.list_reverse[n])
            return new_res
        if n == 0 or n == 2:
            return sorted(res, key=lambda x: int(x[n]), reverse=not self.list_reverse[n])
        return sorted(res, key=lambda x: x[n], reverse=not self.list_reverse[n])

    def draw_page_del(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.task_page)
        self.connection = sqlite3.connect("purpose_db.db")
        res = self.connection.cursor().execute("SELECT * FROM subtasks").fetchall()
        self.ui.table_subtask.setColumnCount(6)
        self.ui.table_subtask.setRowCount(0)
        date_now = datetime.datetime.now().strftime("%Y %m %d")
        now = datetime.date(int(date_now.split()[0]), int(date_now.split()[1]),
                            int(date_now.split()[2]))
        for i in range(len(res)):
            self.ui.table_subtask.setRowCount(
                self.ui.table_subtask.rowCount() + 1)
            if not res[i][3]:
                dat = res[i][4]
                end = datetime.date(int(dat.split()[0]), int(dat.split()[1]), int(dat.split()[2]))
            else:
                end = 0
            for j, elem in enumerate(res[i]):
                self.ui.table_subtask.setItem(
                    i, j, QTableWidgetItem(str(elem)))
                if j == 5 and end != 0:
                    if res[i][5]:
                        self.ui.table_subtask.item(i, j).setBackground(QtGui.QColor(0, 248, 32))
                    else:
                        if now > end:
                            self.ui.table_subtask.item(i, j).setBackground(QtGui.QColor(188, 0, 6))
        res = self.connection.cursor().execute("SELECT * FROM tasks").fetchall()
        self.ui.table_task.setColumnCount(6)
        self.ui.table_task.setRowCount(0)
        for i in range(len(res)):
            self.ui.table_task.setRowCount(
                self.ui.table_task.rowCount() + 1)
            dat = res[i][3]
            end = datetime.date(int(dat.split()[0]), int(dat.split()[1]), int(dat.split()[2]))
            for j, elem in enumerate(res[i]):
                self.ui.table_task.setItem(
                    i, j, QTableWidgetItem(str(elem)))
                if j == 5:
                    if res[i][5]:
                        self.ui.table_task.item(i, j).setBackground(QtGui.QColor(0, 248, 32))
                    else:
                        if now > end:
                            self.ui.table_task.item(i, j).setBackground(QtGui.QColor(188, 0, 6))

    def changeTitle(self, state):
        if state == Qt.Checked:
            for i in self.list_widget_extreme:
                i.setStyleSheet(u"background:rgb{}".format(Color_dark[0]))
            for i in self.list_widget_body:
                i.setStyleSheet(u"background:rgb{}".format(Color_dark[1]))
            for i in self.list_table:
                i.setStyleSheet(u"background:rgb{}".format(Color_dark[3]))
                stylesheet = Color_dark[5]
                i.horizontalHeader().setStyleSheet(stylesheet)
                i.verticalHeader().setStyleSheet(stylesheet)
            for i in self.line_combo_widget:
                i.setStyleSheet(u"background:rgb{}".format(Color_dark[6]))
            self.ui.frame_20.setStyleSheet(u"QPushButton{\n"
                                        "	background-color: rgb(0, 118, 110);\n"
                                        " border-radius: 10px;\n"
                                        "}")
            self.ui.centralwidget.setStyleSheet(Color_dark[4])
        else:
            for i in self.list_widget_extreme:
                i.setStyleSheet(u"background:rgb{}".format(Color_light[0]))
            for i in self.list_widget_body:
                i.setStyleSheet(u"background:rgb{}".format(Color_light[1]))
            for i in self.list_table:
                i.setStyleSheet(u"background:rgb{}".format(Color_light[3]))
                stylesheet = Color_light[5]
                i.horizontalHeader().setStyleSheet(stylesheet)
                i.verticalHeader().setStyleSheet(stylesheet)
            for i in self.line_combo_widget:
                i.setStyleSheet(u"background:rgb{}".format(Color_light[6]))
            self.ui.frame_20.setStyleSheet(u"QPushButton{\n"
                                        "	background-color: rgb(175, 234, 255);\n"
                                        " border-radius: 10px;\n"
                                        "}")
            self.ui.centralwidget.setStyleSheet(Color_light[4])

    def task_update(self):
        try:
            id = self.ui.line_edit_task.text()
            con = sqlite3.connect("purpose_db.db")
            cur = con.cursor()
            cur.execute("""UPDATE tasks
            SET completed = true WHERE id = ?""", (int(id),))
            con.commit()
            self.ui.text_console.setText("Update!")
        except:
            self.ui.text_console.setText("Error!")
        self.draw_page_del()

    def subtask_update(self):
        try:
            id = self.ui.line_edit_subtask.text()
            con = sqlite3.connect("purpose_db.db")
            cur = con.cursor()
            cur.execute("""UPDATE subtasks
            SET completed = true WHERE id = ?""", (int(id),))
            con.commit()
            self.ui.text_console.setText("Update!")
        except:
            self.ui.text_console.setText("Error!")
        self.draw_page_del()

    def purpose_update(self):
        try:
            id = self.ui.line_edit_pur_id.text()
            con = sqlite3.connect("purpose_db.db")
            cur = con.cursor()
            cur.execute("""UPDATE purposes
            SET completed = true WHERE id = ?""", (int(id),))
            con.commit()
            self.ui.text_console.setText("Update!")
        except:
            self.ui.text_console.setText("Error!")
        self.draw_page_purpose()


    # slide home
    def slide_menu_left(self):
        width = self.ui.left_body.width()
        if width == 55:
            new_width = 150
        else:
            new_width = 55
        #Animation
        self.animation = QPropertyAnimation(self.ui.left_body, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
