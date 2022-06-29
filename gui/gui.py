# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\felipe.ribeiro\Desktop\felipe\ldv\ldv_3D_positioning\gui\gui_ldv.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):

    ##################################################
    #                    Functions                   #
    ##################################################

    def file_explorer(self):
        f = QFileDialog.getOpenFileName()
        print(f)
        pass

    ##################################################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setMinimumSize(QtCore.QSize(16777215, 100))
        self.top_frame.setStyleSheet("background-color: rgb(15, 118, 151);")
        self.top_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu_frame = QtWidgets.QWidget(self.top_frame)
        self.menu_frame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.menu_frame.setStyleSheet("background-color: rgb(186, 217, 74);")
        self.menu_frame.setObjectName("menu_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.top_menu_button = QtWidgets.QFrame(self.menu_frame)
        self.top_menu_button.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_menu_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_menu_button.setObjectName("top_menu_button")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.top_menu_button)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.m_btn_expand = QtWidgets.QPushButton(self.top_menu_button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_btn_expand.sizePolicy().hasHeightForWidth())
        self.m_btn_expand.setSizePolicy(sizePolicy)
        self.m_btn_expand.setMinimumSize(QtCore.QSize(100, 100))
        self.m_btn_expand.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(186, 217, 74);\n"
"    border: 0px solid\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(127, 127, 127);\n"
"}")
        self.m_btn_expand.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\felipe.ribeiro\\Desktop\\felipe\\ldv\\ldv_3D_positioning\\gui\\imgs/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_btn_expand.setIcon(icon)
        self.m_btn_expand.setIconSize(QtCore.QSize(50, 50))
        self.m_btn_expand.setObjectName("m_btn_expand")
        self.verticalLayout_5.addWidget(self.m_btn_expand)
        self.verticalLayout_4.addWidget(self.top_menu_button)
        self.horizontalLayout_2.addWidget(self.menu_frame)
        self.top_frame_2 = QtWidgets.QFrame(self.top_frame)
        self.top_frame_2.setMinimumSize(QtCore.QSize(0, 100))
        self.top_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame_2.setObjectName("top_frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.top_frame_2)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2.addWidget(self.top_frame_2)
        self.verticalLayout.addWidget(self.top_frame)
        self.central_frame = QtWidgets.QFrame(self.centralwidget)
        self.central_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.central_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.central_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central_frame.setObjectName("central_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QWidget(self.central_frame)
        self.side_menu.setMinimumSize(QtCore.QSize(100, 0))
        self.side_menu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.side_menu.setStyleSheet("background-color: rgb(186, 217, 74);")
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu_buttons = QtWidgets.QFrame(self.side_menu)
        self.menu_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_buttons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.menu_buttons.setObjectName("menu_buttons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_buttons)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.m_btn_home = QtWidgets.QPushButton(self.menu_buttons)
        self.m_btn_home.setMinimumSize(QtCore.QSize(0, 100))
        self.m_btn_home.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m_btn_home.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(186, 217, 74);\n"
"    padding: 25px;\n"
"    border: 0px solid;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(127, 127, 127);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\felipe.ribeiro\\Desktop\\felipe\\ldv\\ldv_3D_positioning\\gui\\imgs/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_btn_home.setIcon(icon1)
        self.m_btn_home.setIconSize(QtCore.QSize(50, 50))
        self.m_btn_home.setObjectName("m_btn_home")
        self.verticalLayout_3.addWidget(self.m_btn_home)
        self.m_btn_data = QtWidgets.QPushButton(self.menu_buttons)
        self.m_btn_data.setMinimumSize(QtCore.QSize(0, 100))
        self.m_btn_data.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m_btn_data.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(186, 217, 74);\n"
"    padding: 25px;\n"
"    border: 0px solid;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(127, 127, 127);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\felipe.ribeiro\\Desktop\\felipe\\ldv\\ldv_3D_positioning\\gui\\imgs/data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_btn_data.setIcon(icon2)
        self.m_btn_data.setIconSize(QtCore.QSize(50, 50))
        self.m_btn_data.setObjectName("m_btn_data")
        self.verticalLayout_3.addWidget(self.m_btn_data)
        self.m_btn_settings = QtWidgets.QPushButton(self.menu_buttons)
        self.m_btn_settings.setMinimumSize(QtCore.QSize(0, 100))
        self.m_btn_settings.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m_btn_settings.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(186, 217, 74);\n"
"    padding: 25px;\n"
"    border: 0px solid;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(127, 127, 127);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\felipe.ribeiro\\Desktop\\felipe\\ldv\\ldv_3D_positioning\\gui\\imgs/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_btn_settings.setIcon(icon3)
        self.m_btn_settings.setIconSize(QtCore.QSize(50, 50))
        self.m_btn_settings.setObjectName("m_btn_settings")
        self.verticalLayout_3.addWidget(self.m_btn_settings)
        self.verticalLayout_2.addWidget(self.menu_buttons, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.side_menu)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.m_btn_info = QtWidgets.QPushButton(self.frame)
        self.m_btn_info.setMinimumSize(QtCore.QSize(100, 100))
        self.m_btn_info.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(186, 217, 74);\n"
"    padding: 25px;\n"
"    border: 0px solid;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(127, 127, 127);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\felipe.ribeiro\\Desktop\\felipe\\ldv\\ldv_3D_positioning\\gui\\imgs/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_btn_info.setIcon(icon4)
        self.m_btn_info.setIconSize(QtCore.QSize(50, 50))
        self.m_btn_info.setObjectName("m_btn_info")
        self.verticalLayout_8.addWidget(self.m_btn_info)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.side_menu)
        self.widget_2 = QtWidgets.QWidget(self.central_frame)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.main_frame = QtWidgets.QFrame(self.widget_2)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stacked_pages = QtWidgets.QStackedWidget(self.main_frame)
        self.stacked_pages.setMinimumSize(QtCore.QSize(0, 100))
        self.stacked_pages.setObjectName("stacked_pages")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stacked_pages.addWidget(self.page_1)


        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stacked_pages.addWidget(self.page_2)
        self.verticalLayout_7.addWidget(self.stacked_pages)
        self.verticalLayout_6.addWidget(self.main_frame)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.central_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        ##################################################
        #                    Functions                   #
        ##################################################

        self.m_btn_home.clicked.connect(self.file_explorer)

        ##################################################

        self.retranslateUi(MainWindow)
        self.stacked_pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.m_btn_home.setText(_translate("MainWindow", "m_btn_1"))
        self.m_btn_data.setText(_translate("MainWindow", "m_btn_2"))
        self.m_btn_settings.setText(_translate("MainWindow", "m_btn_3"))
        self.m_btn_info.setText(_translate("MainWindow", "PushButton"))
#import rsc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
