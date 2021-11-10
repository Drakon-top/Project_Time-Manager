# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desktopUgdjOH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(867, 672)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 0, 0, 0);\n"
"border: none;\n"
"}\n"
"QFrame{\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}\n"
"QWidget{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(56, 36, 57);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_widget = QFrame(self.centralwidget)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setStyleSheet(u"background:rgb(255, 255, 243)")
        self.top_widget.setFrameShape(QFrame.NoFrame)
        self.top_widget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.top_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, 1, 1, 1)
        self.but_home = QPushButton(self.frame_3)
        self.but_home.setObjectName(u"but_home")
        self.but_home.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u":/Icons/image/home_house_icon-icons.com_49851.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_home.setIcon(icon)
        self.but_home.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.but_home, 0, Qt.AlignLeft)

        self.text_home = QLabel(self.frame_3)
        self.text_home.setObjectName(u"text_home")
        self.text_home.setMaximumSize(QSize(70, 40))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.text_home.setFont(font)

        self.horizontalLayout_3.addWidget(self.text_home, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.top_widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(48, 48))
        self.label_2.setPixmap(QPixmap(u":/Icons/image/construction_project_plan_building_architect_design_develop-52_icon-icons.com_60223.png"))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.text_label_name = QLabel(self.frame_4)
        self.text_label_name.setObjectName(u"text_label_name")
        font1 = QFont()
        font1.setPointSize(14)
        self.text_label_name.setFont(font1)

        self.horizontalLayout_4.addWidget(self.text_label_name)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame = QFrame(self.top_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/image/button_blank_green_14986.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.restore_button = QPushButton(self.frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/image/button_blank_yellow_14988.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon2)
        self.restore_button.setIconSize(QSize(20, 20))
        self.restore_button.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.restore_button)

        self.close_button = QPushButton(self.frame)
        self.close_button.setObjectName(u"close_button")
        font2 = QFont()
        font2.setPointSize(8)
        self.close_button.setFont(font2)
        self.close_button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/image/button_blank_red_14987.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.top_widget, 0, Qt.AlignTop)

        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.left_body = QFrame(self.header)
        self.left_body.setObjectName(u"left_body")
        self.left_body.setMinimumSize(QSize(55, 0))
        self.left_body.setMaximumSize(QSize(20, 16777215))
        self.left_body.setStyleSheet(u"background:rgb(255, 255, 243);")
        self.left_body.setFrameShape(QFrame.StyledPanel)
        self.left_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_body)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.left_body)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(140, 0))
        self.left_menu.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"MS Reference Specialty")
        self.left_menu.setFont(font3)
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.left_menu)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_task = QPushButton(self.left_menu)
        self.button_task.setObjectName(u"button_task")
        self.button_task.setMaximumSize(QSize(48, 48))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/image/deal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_task.setIcon(icon4)
        self.button_task.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.button_task, 1, 0, 1, 1, Qt.AlignLeft)

        self.frame_14 = QFrame(self.left_menu)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(48, 48))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_14)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.button_Add = QPushButton(self.frame_14)
        self.button_Add.setObjectName(u"button_Add")
        self.button_Add.setMaximumSize(QSize(32, 32))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/image/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_Add.setIcon(icon5)
        self.button_Add.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.button_Add, 0, Qt.AlignLeft)


        self.gridLayout.addWidget(self.frame_14, 3, 0, 1, 1)

        self.text_purpose = QLabel(self.left_menu)
        self.text_purpose.setObjectName(u"text_purpose")
        font4 = QFont()
        font4.setPointSize(12)
        self.text_purpose.setFont(font4)

        self.gridLayout.addWidget(self.text_purpose, 0, 1, 1, 1, Qt.AlignLeft)

        self.button_deal = QPushButton(self.left_menu)
        self.button_deal.setObjectName(u"button_deal")
        self.button_deal.setMaximumSize(QSize(48, 48))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/image/graf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_deal.setIcon(icon6)
        self.button_deal.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.button_deal, 2, 0, 1, 1, Qt.AlignLeft)

        self.text_progress = QLabel(self.left_menu)
        self.text_progress.setObjectName(u"text_progress")
        self.text_progress.setFont(font4)

        self.gridLayout.addWidget(self.text_progress, 2, 1, 1, 1, Qt.AlignLeft)

        self.text_deal = QLabel(self.left_menu)
        self.text_deal.setObjectName(u"text_deal")
        self.text_deal.setFont(font4)

        self.gridLayout.addWidget(self.text_deal, 1, 1, 1, 1, Qt.AlignLeft)

        self.button_purpose = QPushButton(self.left_menu)
        self.button_purpose.setObjectName(u"button_purpose")
        self.button_purpose.setMaximumSize(QSize(48, 48))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/image/chel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_purpose.setIcon(icon7)
        self.button_purpose.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.button_purpose, 0, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.left_menu, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.left_body)

        self.header_body = QFrame(self.header)
        self.header_body.setObjectName(u"header_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header_body.sizePolicy().hasHeightForWidth())
        self.header_body.setSizePolicy(sizePolicy1)
        self.header_body.setStyleSheet(u"background:rgb(221, 255, 255);")
        self.header_body.setFrameShape(QFrame.StyledPanel)
        self.header_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.header_body)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.header_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.goal_page = QWidget()
        self.goal_page.setObjectName(u"goal_page")
        self.verticalLayout_5 = QVBoxLayout(self.goal_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_7 = QFrame(self.goal_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.text_page_purpose = QLabel(self.frame_7)
        self.text_page_purpose.setObjectName(u"text_page_purpose")
        self.text_page_purpose.setMinimumSize(QSize(30, 30))
        self.text_page_purpose.setFont(font4)
        self.text_page_purpose.setMargin(5)

        self.horizontalLayout_9.addWidget(self.text_page_purpose)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_20 = QFrame(self.goal_page)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(175, 234, 255);\n"
" border-radius: 10px;\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.sort_name = QPushButton(self.frame_20)
        self.sort_name.setObjectName(u"sort_name")
        self.sort_name.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setPointSize(9)
        self.sort_name.setFont(font5)

        self.horizontalLayout_17.addWidget(self.sort_name)

        self.sort_importanse = QPushButton(self.frame_20)
        self.sort_importanse.setObjectName(u"sort_importanse")
        self.sort_importanse.setMinimumSize(QSize(0, 30))
        self.sort_importanse.setFont(font5)

        self.horizontalLayout_17.addWidget(self.sort_importanse)

        self.sort_date_start = QPushButton(self.frame_20)
        self.sort_date_start.setObjectName(u"sort_date_start")
        self.sort_date_start.setMinimumSize(QSize(0, 30))
        self.sort_date_start.setFont(font5)

        self.horizontalLayout_17.addWidget(self.sort_date_start)

        self.sor_date_end = QPushButton(self.frame_20)
        self.sor_date_end.setObjectName(u"sor_date_end")
        self.sor_date_end.setMinimumSize(QSize(0, 30))
        self.sor_date_end.setFont(font5)

        self.horizontalLayout_17.addWidget(self.sor_date_end)

        self.sort_complet = QPushButton(self.frame_20)
        self.sort_complet.setObjectName(u"sort_complet")
        self.sort_complet.setMinimumSize(QSize(0, 30))
        self.sort_complet.setFont(font5)

        self.horizontalLayout_17.addWidget(self.sort_complet)


        self.verticalLayout_5.addWidget(self.frame_20)

        self.frame_10 = QFrame(self.goal_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.table_purpouse = QTableWidget(self.frame_10)
        if (self.table_purpouse.columnCount() < 7):
            self.table_purpouse.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_purpouse.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_purpouse.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_purpouse.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_purpouse.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_purpouse.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_purpouse.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_purpouse.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_purpouse.setObjectName(u"table_purpouse")
        self.table_purpouse.setMinimumSize(QSize(630, 0))
        self.table_purpouse.setMaximumSize(QSize(16777215, 16777215))
        self.table_purpouse.setStyleSheet(u"background:rgb(166, 246, 255)")

        self.horizontalLayout_14.addWidget(self.table_purpouse)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_21 = QFrame(self.goal_page)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.button_completed_pur = QPushButton(self.frame_21)
        self.button_completed_pur.setObjectName(u"button_completed_pur")
        font6 = QFont()
        font6.setPointSize(10)
        self.button_completed_pur.setFont(font6)

        self.horizontalLayout_18.addWidget(self.button_completed_pur, 0, Qt.AlignLeft)

        self.line_edit_pur_id = QLineEdit(self.frame_21)
        self.line_edit_pur_id.setObjectName(u"line_edit_pur_id")
        self.line_edit_pur_id.setMaximumSize(QSize(150, 150))
        self.line_edit_pur_id.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.line_edit_pur_id)


        self.verticalLayout_5.addWidget(self.frame_21)

        self.frame_8 = QFrame(self.goal_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.text_complet = QLabel(self.frame_11)
        self.text_complet.setObjectName(u"text_complet")
        self.text_complet.setFont(font4)

        self.horizontalLayout_11.addWidget(self.text_complet)

        self.lcd_pur_com = QLCDNumber(self.frame_11)
        self.lcd_pur_com.setObjectName(u"lcd_pur_com")
        self.lcd_pur_com.setMaximumSize(QSize(100, 100))
        self.lcd_pur_com.setStyleSheet(u"background-color: rgb(0, 255, 127);")

        self.horizontalLayout_11.addWidget(self.lcd_pur_com)


        self.horizontalLayout_10.addWidget(self.frame_11, 0, Qt.AlignLeft)

        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.text_proces = QLabel(self.frame_13)
        self.text_proces.setObjectName(u"text_proces")
        self.text_proces.setFont(font4)
        self.text_proces.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.text_proces)

        self.lcd_pur_now = QLCDNumber(self.frame_13)
        self.lcd_pur_now.setObjectName(u"lcd_pur_now")
        self.lcd_pur_now.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.lcd_pur_now)


        self.horizontalLayout_10.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.text_not_complet = QLabel(self.frame_12)
        self.text_not_complet.setObjectName(u"text_not_complet")
        font7 = QFont()
        font7.setPointSize(11)
        self.text_not_complet.setFont(font7)

        self.horizontalLayout_13.addWidget(self.text_not_complet)

        self.lcd_pur_overd = QLCDNumber(self.frame_12)
        self.lcd_pur_overd.setObjectName(u"lcd_pur_overd")
        self.lcd_pur_overd.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.horizontalLayout_13.addWidget(self.lcd_pur_overd)


        self.horizontalLayout_10.addWidget(self.frame_12, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_8, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.goal_page)
        self.task_page = QWidget()
        self.task_page.setObjectName(u"task_page")
        self.horizontalLayout_16 = QHBoxLayout(self.task_page)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_18 = QFrame(self.task_page)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)

        self.verticalLayout_10.addWidget(self.label_7, 0, Qt.AlignRight)

        self.table_task = QTableWidget(self.frame_18)
        if (self.table_task.columnCount() < 6):
            self.table_task.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_task.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.table_task.setObjectName(u"table_task")
        self.table_task.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.table_task)

        self.line_edit_task = QLineEdit(self.frame_18)
        self.line_edit_task.setObjectName(u"line_edit_task")
        self.line_edit_task.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.line_edit_task, 0, Qt.AlignLeft)

        self.button_complet_task = QPushButton(self.frame_18)
        self.button_complet_task.setObjectName(u"button_complet_task")
        self.button_complet_task.setMaximumSize(QSize(200, 50))
        self.button_complet_task.setFont(font7)

        self.verticalLayout_10.addWidget(self.button_complet_task, 0, Qt.AlignLeft)


        self.horizontalLayout_16.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.task_page)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)

        self.verticalLayout_11.addWidget(self.label_8, 0, Qt.AlignLeft)

        self.table_subtask = QTableWidget(self.frame_19)
        if (self.table_subtask.columnCount() < 6):
            self.table_subtask.setColumnCount(6)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_subtask.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_subtask.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_subtask.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_subtask.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_subtask.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_subtask.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        self.table_subtask.setObjectName(u"table_subtask")
        self.table_subtask.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.table_subtask)

        self.line_edit_subtask = QLineEdit(self.frame_19)
        self.line_edit_subtask.setObjectName(u"line_edit_subtask")
        self.line_edit_subtask.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.line_edit_subtask, 0, Qt.AlignRight)

        self.button_complet_subtask = QPushButton(self.frame_19)
        self.button_complet_subtask.setObjectName(u"button_complet_subtask")
        self.button_complet_subtask.setFont(font7)

        self.verticalLayout_11.addWidget(self.button_complet_subtask, 0, Qt.AlignRight)


        self.horizontalLayout_16.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.task_page)
        self.progress_page = QWidget()
        self.progress_page.setObjectName(u"progress_page")
        self.verticalLayout_12 = QVBoxLayout(self.progress_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_22 = QFrame(self.progress_page)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_9 = QLabel(self.frame_22)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)
        self.label_9.setTextFormat(Qt.PlainText)

        self.horizontalLayout_19.addWidget(self.label_9)


        self.verticalLayout_12.addWidget(self.frame_22, 0, Qt.AlignTop)

        self.frame_23 = QFrame(self.progress_page)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_23)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.table_task_deal = QTableWidget(self.frame_23)
        if (self.table_task_deal.columnCount() < 6):
            self.table_task_deal.setColumnCount(6)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_task_deal.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_task_deal.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_task_deal.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_task_deal.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_task_deal.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_task_deal.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        self.table_task_deal.setObjectName(u"table_task_deal")
        self.table_task_deal.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.table_task_deal)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.text_complet_2 = QLabel(self.frame_25)
        self.text_complet_2.setObjectName(u"text_complet_2")
        self.text_complet_2.setFont(font4)

        self.horizontalLayout_21.addWidget(self.text_complet_2)

        self.lcd_task_complet = QLCDNumber(self.frame_25)
        self.lcd_task_complet.setObjectName(u"lcd_task_complet")
        self.lcd_task_complet.setMaximumSize(QSize(100, 100))
        self.lcd_task_complet.setStyleSheet(u"background-color: rgb(0, 255, 127);")

        self.horizontalLayout_21.addWidget(self.lcd_task_complet)


        self.horizontalLayout_20.addWidget(self.frame_25, 0, Qt.AlignLeft)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.text_proces_2 = QLabel(self.frame_26)
        self.text_proces_2.setObjectName(u"text_proces_2")
        self.text_proces_2.setFont(font4)
        self.text_proces_2.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.text_proces_2)

        self.lcd_task_now = QLCDNumber(self.frame_26)
        self.lcd_task_now.setObjectName(u"lcd_task_now")
        self.lcd_task_now.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_22.addWidget(self.lcd_task_now)


        self.horizontalLayout_20.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.text_not_complet_2 = QLabel(self.frame_27)
        self.text_not_complet_2.setObjectName(u"text_not_complet_2")
        self.text_not_complet_2.setFont(font7)

        self.horizontalLayout_23.addWidget(self.text_not_complet_2)

        self.lcd_task_notcomplet = QLCDNumber(self.frame_27)
        self.lcd_task_notcomplet.setObjectName(u"lcd_task_notcomplet")
        self.lcd_task_notcomplet.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.horizontalLayout_23.addWidget(self.lcd_task_notcomplet)


        self.horizontalLayout_20.addWidget(self.frame_27, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_24)


        self.verticalLayout_12.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.progress_page)
        self.add_page = QWidget()
        self.add_page.setObjectName(u"add_page")
        self.horizontalLayout_15 = QHBoxLayout(self.add_page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_17 = QFrame(self.add_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(200, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_17)
        self.verticalLayout_9.setSpacing(11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.label = QLabel(self.frame_17)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 50))
        self.label.setFont(font4)

        self.verticalLayout_9.addWidget(self.label)

        self.text_name_suptask = QLineEdit(self.frame_17)
        self.text_name_suptask.setObjectName(u"text_name_suptask")
        self.text_name_suptask.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_9.addWidget(self.text_name_suptask)

        self.label_4 = QLabel(self.frame_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(200, 50))
        self.label_4.setFont(font7)

        self.verticalLayout_9.addWidget(self.label_4)

        self.combo_box_suptask_zel = QComboBox(self.frame_17)
        self.combo_box_suptask_zel.setObjectName(u"combo_box_suptask_zel")
        self.combo_box_suptask_zel.setMinimumSize(QSize(0, 25))
        self.combo_box_suptask_zel.setMaximumSize(QSize(16777215, 30))
        self.combo_box_suptask_zel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.combo_box_suptask_zel)

        self.check_box_every_day = QCheckBox(self.frame_17)
        self.check_box_every_day.setObjectName(u"check_box_every_day")
        self.check_box_every_day.setFont(font6)

        self.verticalLayout_9.addWidget(self.check_box_every_day)

        self.text_date_end_sup = QLabel(self.frame_17)
        self.text_date_end_sup.setObjectName(u"text_date_end_sup")
        self.text_date_end_sup.setMaximumSize(QSize(150, 50))
        self.text_date_end_sup.setFont(font4)

        self.verticalLayout_9.addWidget(self.text_date_end_sup)

        self.date_suptask = QDateEdit(self.frame_17)
        self.date_suptask.setObjectName(u"date_suptask")
        self.date_suptask.setMaximumSize(QSize(200, 16777215))
        self.date_suptask.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))

        self.verticalLayout_9.addWidget(self.date_suptask)

        self.button_add_podzadacha = QPushButton(self.frame_17)
        self.button_add_podzadacha.setObjectName(u"button_add_podzadacha")
        self.button_add_podzadacha.setMinimumSize(QSize(32, 32))
        self.button_add_podzadacha.setMaximumSize(QSize(32, 32))
        icon8 = QIcon()
        icon8.addFile(u":/Icons/image/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_add_podzadacha.setIcon(icon8)
        self.button_add_podzadacha.setIconSize(QSize(32, 32))

        self.verticalLayout_9.addWidget(self.button_add_podzadacha, 0, Qt.AlignLeft)


        self.horizontalLayout_15.addWidget(self.frame_17, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_16 = QFrame(self.add_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setSpacing(11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 16777215))
        self.label_6.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_6)

        self.text_name_pur = QLineEdit(self.frame_16)
        self.text_name_pur.setObjectName(u"text_name_pur")
        self.text_name_pur.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_8.addWidget(self.text_name_pur)

        self.text_date_end_sup_2 = QLabel(self.frame_16)
        self.text_date_end_sup_2.setObjectName(u"text_date_end_sup_2")
        self.text_date_end_sup_2.setMaximumSize(QSize(200, 50))
        self.text_date_end_sup_2.setFont(font4)

        self.verticalLayout_8.addWidget(self.text_date_end_sup_2)

        self.date_pur = QDateEdit(self.frame_16)
        self.date_pur.setObjectName(u"date_pur")
        self.date_pur.setMaximumSize(QSize(200, 16777215))
        self.date_pur.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))

        self.verticalLayout_8.addWidget(self.date_pur)

        self.label_11 = QLabel(self.frame_16)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(200, 16777215))
        self.label_11.setFont(font7)

        self.verticalLayout_8.addWidget(self.label_11)

        self.comboBox_pur_impo = QComboBox(self.frame_16)
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.addItem("")
        self.comboBox_pur_impo.setObjectName(u"comboBox_pur_impo")
        self.comboBox_pur_impo.setMinimumSize(QSize(0, 25))
        self.comboBox_pur_impo.setMaximumSize(QSize(150, 16777215))
        self.comboBox_pur_impo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.comboBox_pur_impo)

        self.label_12 = QLabel(self.frame_16)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(200, 16777215))
        self.label_12.setFont(font7)

        self.verticalLayout_8.addWidget(self.label_12)

        self.plain_text_for_pur = QPlainTextEdit(self.frame_16)
        self.plain_text_for_pur.setObjectName(u"plain_text_for_pur")
        self.plain_text_for_pur.setMaximumSize(QSize(170, 100))
        self.plain_text_for_pur.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.plain_text_for_pur)

        self.butt_add_purpouse = QPushButton(self.frame_16)
        self.butt_add_purpouse.setObjectName(u"butt_add_purpouse")
        self.butt_add_purpouse.setMinimumSize(QSize(32, 32))
        self.butt_add_purpouse.setMaximumSize(QSize(32, 32))
        self.butt_add_purpouse.setIcon(icon8)
        self.butt_add_purpouse.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.butt_add_purpouse)


        self.horizontalLayout_15.addWidget(self.frame_16, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_15 = QFrame(self.add_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setSpacing(11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(200, 50))
        self.label_3.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_3)

        self.text_name_task = QLineEdit(self.frame_15)
        self.text_name_task.setObjectName(u"text_name_task")
        self.text_name_task.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_7.addWidget(self.text_name_task)

        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(200, 50))
        self.label_5.setFont(font7)

        self.verticalLayout_7.addWidget(self.label_5)

        self.combo_box_task = QComboBox(self.frame_15)
        self.combo_box_task.setObjectName(u"combo_box_task")
        self.combo_box_task.setMinimumSize(QSize(0, 25))
        self.combo_box_task.setMaximumSize(QSize(16777215, 30))
        self.combo_box_task.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.combo_box_task)

        self.text_date_end_sup_3 = QLabel(self.frame_15)
        self.text_date_end_sup_3.setObjectName(u"text_date_end_sup_3")
        self.text_date_end_sup_3.setMaximumSize(QSize(200, 50))
        self.text_date_end_sup_3.setFont(font6)

        self.verticalLayout_7.addWidget(self.text_date_end_sup_3)

        self.datetime_task = QDateTimeEdit(self.frame_15)
        self.datetime_task.setObjectName(u"datetime_task")
        self.datetime_task.setDate(QDate(2021, 1, 1))
        self.datetime_task.setTime(QTime(15, 0, 0))

        self.verticalLayout_7.addWidget(self.datetime_task)

        self.button_add_task = QPushButton(self.frame_15)
        self.button_add_task.setObjectName(u"button_add_task")
        self.button_add_task.setMinimumSize(QSize(32, 32))
        self.button_add_task.setMaximumSize(QSize(32, 32))
        self.button_add_task.setIcon(icon8)
        self.button_add_task.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.button_add_task)


        self.horizontalLayout_15.addWidget(self.frame_15, 0, Qt.AlignRight|Qt.AlignTop)

        self.stackedWidget.addWidget(self.add_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.header_body)

        self.right_body = QFrame(self.header)
        self.right_body.setObjectName(u"right_body")
        self.right_body.setStyleSheet(u"background:rgb(255, 255, 243)")
        self.right_body.setFrameShape(QFrame.StyledPanel)
        self.right_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.right_body)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.right_body)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.url_yandex = QLabel(self.frame_6)
        self.url_yandex.setObjectName(u"url_yandex")
        self.url_yandex.setStyleSheet(u"color: rgb(88, 212, 156)")

        self.verticalLayout_3.addWidget(self.url_yandex)


        self.horizontalLayout_8.addWidget(self.frame_6, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.right_body)


        self.verticalLayout.addWidget(self.header)

        self.bottom_widget = QFrame(self.centralwidget)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.bottom_widget.setStyleSheet(u"background:rgb(221, 255, 255);")
        self.bottom_widget.setFrameShape(QFrame.NoFrame)
        self.bottom_widget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.bottom_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.text_version = QLabel(self.frame_2)
        self.text_version.setObjectName(u"text_version")
        self.text_version.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_6.addWidget(self.text_version)

        self.text_console = QLabel(self.frame_2)
        self.text_console.setObjectName(u"text_console")
        self.text_console.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.text_console, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.checkBox_drak_tem = QCheckBox(self.bottom_widget)
        self.checkBox_drak_tem.setObjectName(u"checkBox_drak_tem")
        self.checkBox_drak_tem.setMinimumSize(QSize(50, 50))
        self.checkBox_drak_tem.setMaximumSize(QSize(200, 200))
        self.checkBox_drak_tem.setStyleSheet(u"QCheckBox::indicator{\n"
"widht: 100px;\n"
"height: 100px;\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
" image: url(image/enable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"     image: url(image/disable.png);\n"
" }")
        self.checkBox_drak_tem.setIconSize(QSize(48, 48))

        self.horizontalLayout_5.addWidget(self.checkBox_drak_tem, 0, Qt.AlignRight)

        self.frame_5 = QFrame(self.bottom_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(10, 10))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.bottom_widget, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 867, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.but_home.setText("")
        self.text_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_2.setText("")
        self.text_label_name.setText(QCoreApplication.translate("MainWindow", u"Time Manager", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.close_button.setText("")
        self.button_task.setText("")
        self.button_Add.setText("")
        self.text_purpose.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043b\u0438", None))
        self.button_deal.setText("")
        self.text_progress.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441", None))
        self.text_deal.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043b\u0430", None))
        self.button_purpose.setText("")
        self.text_page_purpose.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043b\u0438", None))
        self.sort_name.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.sort_importanse.setText(QCoreApplication.translate("MainWindow", u"importace", None))
        self.sort_date_start.setText(QCoreApplication.translate("MainWindow", u"date_start", None))
        self.sor_date_end.setText(QCoreApplication.translate("MainWindow", u"date_end", None))
        self.sort_complet.setText(QCoreApplication.translate("MainWindow", u"complet", None))
        ___qtablewidgetitem = self.table_purpouse.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.table_purpouse.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem2 = self.table_purpouse.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"importance", None));
        ___qtablewidgetitem3 = self.table_purpouse.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"date_start", None));
        ___qtablewidgetitem4 = self.table_purpouse.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"date_end", None));
        ___qtablewidgetitem5 = self.table_purpouse.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"for_what", None));
        ___qtablewidgetitem6 = self.table_purpouse.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"complet", None));
        self.button_completed_pur.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.text_complet.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0438\u0433\u043d\u0443\u0442\u043e", None))
        self.text_proces.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.text_not_complet.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        ___qtablewidgetitem7 = self.table_task.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem8 = self.table_task.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem9 = self.table_task.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"for subtask", None));
        ___qtablewidgetitem10 = self.table_task.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem11 = self.table_task.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"time", None));
        ___qtablewidgetitem12 = self.table_task.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"done", None));
        self.button_complet_task.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0437\u0430\u0434\u0430\u0447\u0438", None))
        ___qtablewidgetitem13 = self.table_subtask.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem14 = self.table_subtask.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem15 = self.table_subtask.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem16 = self.table_subtask.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"every day", None));
        ___qtablewidgetitem17 = self.table_subtask.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem18 = self.table_subtask.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"done", None));
        self.button_complet_subtask.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438 \u043d\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None))
        ___qtablewidgetitem19 = self.table_task_deal.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem20 = self.table_task_deal.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem21 = self.table_task_deal.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"for subtask", None));
        ___qtablewidgetitem22 = self.table_task_deal.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem23 = self.table_task_deal.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"time", None));
        ___qtablewidgetitem24 = self.table_task_deal.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"done", None));
        self.text_complet_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.text_proces_2.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.text_not_complet_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043f\u043e\u0434\u0437\u0430\u0434\u0430\u0447\u0430", None))
        self.text_name_suptask.setInputMask("")
        self.text_name_suptask.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043b\u044c", None))
        self.check_box_every_day.setText(QCoreApplication.translate("MainWindow", u"Every Day", None))
        self.text_date_end_sup.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.button_add_podzadacha.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0446\u0435\u043b\u044c", None))
        self.text_name_pur.setInputMask("")
        self.text_name_pur.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.text_date_end_sup_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.comboBox_pur_impo.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_pur_impo.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_pur_impo.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_pur_impo.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_pur_impo.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_pur_impo.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_pur_impo.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_pur_impo.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_pur_impo.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_pur_impo.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0446\u0435\u043b\u0438", None))
        self.plain_text_for_pur.setPlainText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u043d\u0430\u043f\u0438\u0441\u0430\u0442\u044c: \u0434\u043b\u044f \u0447\u0435\u0433\u043e \u0412\u044b \u0441\u0442\u0430\u0432\u0438\u0442\u0435 \u044d\u0442\u0443 \u0446\u0435\u043b\u044c", None))
        self.butt_add_purpouse.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430", None))
        self.text_name_task.setInputMask("")
        self.text_name_task.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0437\u0430\u0434\u0430\u0447\u0430", None))
        self.text_date_end_sup_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.button_add_task.setText("")
        self.url_yandex.setText(QCoreApplication.translate("MainWindow", u"for Yandex Lyceum", None))
        self.text_version.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Drakon", None))
        self.text_console.setText("")
        self.checkBox_drak_tem.setText("")
    # retranslateUi

