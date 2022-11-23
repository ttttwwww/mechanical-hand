from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow
import mainwindow
import setting
import m_serial

class InterFace:
    def __init__(self):
        self.ui = mainwindow.Ui_MainWindow()
        self.ser = m_serial.MySerial()
        super(InterFace, self).__init__()
    def ui_init(self):
        self.ui.setupUi(QMainWindow())
        #串口下拉选单初始化
        for i in range(len(self.ser.port_list)):
            self.ui.com_comboBox.addItem(self.ser.port_list[i][0])
        #波特率下拉选单初始化
        self.ui.bps_comboBox.addItems(setting.bps_list)
        #槽函数与信号连接
        self.ui.com_comboBox.currentIndexChanged.connect(self.com_switch)
        self.ui.bps_comboBox.currentIndexChanged.connect(self.bps_switch)
        self.ui.finger_set_pushbutton.click(self.gesture_set)
    #用于切换端口
    def com_switch(self):
        self.ser.port = self.ser.port_list[self.ui.com_comboBox.currentIndex()][0]
    #用于切换波特率
    def bps_switch(self):
        self.ser.bps = setting.bps_list[self.ui.bps_comboBox.currentIndex()]
    #用于直接设定手势
    def gesture_set(self):
        time = 0
        cnt = 6
        ids = [0,1,2,3,4,5]
        pos = [
            self
        ]

