# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from sliderandspin import SliderAndSpin

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 809)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.default_gesture_widget = QtWidgets.QWidget(self.centralwidget)
        self.default_gesture_widget.setGeometry(QtCore.QRect(630, 126, 99, 181))
        self.default_gesture_widget.setObjectName("default_gesture_widget")
        self.formLayout = QtWidgets.QFormLayout(self.default_gesture_widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.gesture_0_pushButton = QtWidgets.QPushButton(self.default_gesture_widget)
        self.gesture_0_pushButton.setObjectName("gesture_0_pushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.gesture_0_pushButton)
        self.gesture_1_pushButton = QtWidgets.QPushButton(self.default_gesture_widget)
        self.gesture_1_pushButton.setObjectName("gesture_1_pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gesture_1_pushButton)
        self.gesture_2_pushButton = QtWidgets.QPushButton(self.default_gesture_widget)
        self.gesture_2_pushButton.setObjectName("gesture_2_pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gesture_2_pushButton)
        self.gesture_3_pushButton = QtWidgets.QPushButton(self.default_gesture_widget)
        self.gesture_3_pushButton.setObjectName("gesture_3_pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gesture_3_pushButton)
        self.gesture_4_pushButton = QtWidgets.QPushButton(self.default_gesture_widget)
        self.gesture_4_pushButton.setObjectName("gesture_4_pushButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.gesture_4_pushButton)
        self.gesture_5_pushButton = QtWidgets.QPushButton(self.default_gesture_widget)
        self.gesture_5_pushButton.setObjectName("gesture_5_pushButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.gesture_5_pushButton)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 60, 301, 241))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(110, 10, 71, 16))
        self.label.setObjectName("label")
        self.com_widget = QtWidgets.QWidget(self.centralwidget)
        self.com_widget.setGeometry(QtCore.QRect(520, 380, 201, 94))
        self.com_widget.setObjectName("com_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.com_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.com_close_pushButton = QtWidgets.QPushButton(self.com_widget)
        self.com_close_pushButton.setObjectName("com_close_pushButton")
        self.gridLayout_2.addWidget(self.com_close_pushButton, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.com_widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.com_comboBox = QtWidgets.QComboBox(self.com_widget)
        self.com_comboBox.setObjectName("com_comboBox")
        self.gridLayout_2.addWidget(self.com_comboBox, 0, 1, 1, 1)
        self.com_connect_pushButton = QtWidgets.QPushButton(self.com_widget)
        self.com_connect_pushButton.setObjectName("com_connect_pushButton")
        self.gridLayout_2.addWidget(self.com_connect_pushButton, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.com_widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.bps_comboBox = QtWidgets.QComboBox(self.com_widget)
        self.bps_comboBox.setObjectName("bps_comboBox")
        self.gridLayout_2.addWidget(self.bps_comboBox, 3, 1, 1, 1)
        self.finger_state_widget = QtWidgets.QWidget(self.centralwidget)
        self.finger_state_widget.setGeometry(QtCore.QRect(100, 350, 318, 280))
        self.finger_state_widget.setObjectName("finger_state_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.finger_state_widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.finger_label_12 = QtWidgets.QLabel(self.finger_state_widget)
        self.finger_label_12.setObjectName("finger_label_12")
        self.gridLayout_3.addWidget(self.finger_label_12, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.finger_state_widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.time_spinBox = QtWidgets.QSpinBox(self.finger_state_widget)
        self.time_spinBox.setObjectName("time_spinBox")
        self.gridLayout_3.addWidget(self.time_spinBox, 1, 1, 1, 1)
        self.slider_spin_0 = SliderAndSpin(self.finger_state_widget)
        self.slider_spin_0.setMinimumSize(QtCore.QSize(300, 30))
        self.slider_spin_0.setObjectName("slider_spin_0")
        self.gridLayout_3.addWidget(self.slider_spin_0, 2, 0, 1, 2)
        self.slider_spin_1 = SliderAndSpin(self.finger_state_widget)
        self.slider_spin_1.setMinimumSize(QtCore.QSize(250, 30))
        self.slider_spin_1.setObjectName("slider_spin_1")
        self.gridLayout_3.addWidget(self.slider_spin_1, 3, 0, 1, 2)
        self.slider_spin_2 = SliderAndSpin(self.finger_state_widget)
        self.slider_spin_2.setMinimumSize(QtCore.QSize(250, 30))
        self.slider_spin_2.setObjectName("slider_spin_2")
        self.gridLayout_3.addWidget(self.slider_spin_2, 4, 0, 1, 2)
        self.slider_spin_3 = SliderAndSpin(self.finger_state_widget)
        self.slider_spin_3.setMinimumSize(QtCore.QSize(250, 30))
        self.slider_spin_3.setObjectName("slider_spin_3")
        self.gridLayout_3.addWidget(self.slider_spin_3, 5, 0, 1, 2)
        self.slider_spin_4 = SliderAndSpin(self.finger_state_widget)
        self.slider_spin_4.setMinimumSize(QtCore.QSize(250, 30))
        self.slider_spin_4.setObjectName("slider_spin_4")
        self.gridLayout_3.addWidget(self.slider_spin_4, 6, 0, 1, 2)
        self.slider_spin_5 = SliderAndSpin(self.finger_state_widget)
        self.slider_spin_5.setMinimumSize(QtCore.QSize(250, 30))
        self.slider_spin_5.setObjectName("slider_spin_5")
        self.gridLayout_3.addWidget(self.slider_spin_5, 7, 0, 1, 2)
        self.net_widget = QtWidgets.QWidget(self.centralwidget)
        self.net_widget.setGeometry(QtCore.QRect(580, 530, 336, 101))
        self.net_widget.setObjectName("net_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.net_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.net_widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tcp_server_ip_line_Edit = QtWidgets.QLineEdit(self.net_widget)
        self.tcp_server_ip_line_Edit.setObjectName("tcp_server_ip_line_Edit")
        self.gridLayout.addWidget(self.tcp_server_ip_line_Edit, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.net_widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.net_widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.tcp_server_port_line_Edit = QtWidgets.QLineEdit(self.net_widget)
        self.tcp_server_port_line_Edit.setObjectName("tcp_server_port_line_Edit")
        self.gridLayout.addWidget(self.tcp_server_port_line_Edit, 1, 1, 1, 1)
        self.tcp_server_connected_ip_comboBox = QtWidgets.QComboBox(self.net_widget)
        self.tcp_server_connected_ip_comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.tcp_server_connected_ip_comboBox.setObjectName("tcp_server_connected_ip_comboBox")
        self.gridLayout.addWidget(self.tcp_server_connected_ip_comboBox, 1, 2, 1, 1)
        self.tcp_server_setup_pushButton = QtWidgets.QPushButton(self.net_widget)
        self.tcp_server_setup_pushButton.setObjectName("tcp_server_setup_pushButton")
        self.gridLayout.addWidget(self.tcp_server_setup_pushButton, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gesture_0_pushButton.setText(_translate("MainWindow", "手势一"))
        self.gesture_1_pushButton.setText(_translate("MainWindow", "手势二"))
        self.gesture_2_pushButton.setText(_translate("MainWindow", "手势三"))
        self.gesture_3_pushButton.setText(_translate("MainWindow", "手势四"))
        self.gesture_4_pushButton.setText(_translate("MainWindow", "手势五"))
        self.gesture_5_pushButton.setText(_translate("MainWindow", "手势六"))
        self.label.setText(_translate("MainWindow", "手势示意图"))
        self.com_close_pushButton.setText(_translate("MainWindow", "关闭串口"))
        self.label_3.setText(_translate("MainWindow", "选择串口"))
        self.com_connect_pushButton.setText(_translate("MainWindow", "打开串口"))
        self.label_4.setText(_translate("MainWindow", "波特率"))
        self.finger_label_12.setText(_translate("MainWindow", "单次手势调整"))
        self.label_5.setText(_translate("MainWindow", "时间"))
        self.label_2.setText(_translate("MainWindow", "Address"))
        self.label_7.setText(_translate("MainWindow", "已连接设备ip"))
        self.label_6.setText(_translate("MainWindow", "Port"))
        self.tcp_server_setup_pushButton.setText(_translate("MainWindow", "建立tcpserver"))

