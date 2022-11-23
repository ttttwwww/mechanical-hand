from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow
import mainwindow
import setting
import m_serial

class InterFace:
    def __init__(self):
        super(InterFace, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ser = m_serial.MySerial()
        self.ids = [0,1,2,3,4,5]
        self.pos = [900,900,900,900,900,900]
        self.cnt = 6
        self.time_move = 0
    def ui_init(self):
        self.ui.setupUi(QMainWindow())
        #串口下拉选单初始化
        for i in range(len(self.ser.port_list)):
            self.ui.com_comboBox.addItem(self.ser.port_list[i][0])
        #波特率下拉选单初始化
        self.ui.bps_comboBox.addItems(setting.bps_list)
        #槽函数与信号连接
        #串口选择改变
        self.ui.com_comboBox.currentIndexChanged.connect(self.com_switch)
        #波特率选择改变
        self.ui.bps_comboBox.currentIndexChanged.connect(self.bps_switch)
        #手势调整按钮按下
        self.ui.finger_set_pushbutton.click(self.gesture_set)
        #手势pos改变
        self.ui.finger_0_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_1_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_2_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_3_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_4_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_5_horizontalSlider.valueChanged.connect(self.pos_update_slider)

        self.ui.finger_0_spinbox.valueChanged.connect(self.pos_update_spinbox)
        self.ui.finger_1_spinbox.valueChanged.connect(self.pos_update_spinbox)
        self.ui.finger_2_spinbox.valueChanged.connect(self.pos_update_spinbox)
        self.ui.finger_3_spinbox.valueChanged.connect(self.pos_update_spinbox)
        self.ui.finger_4_spinbox.valueChanged.connect(self.pos_update_spinbox)
        self.ui.finger_5_spinbox.valueChanged.connect(self.pos_update_spinbox)

    #用于切换端口
    def com_switch(self):
        self.ser.port = self.ser.port_list[self.ui.com_comboBox.currentIndex()][0]
    #用于切换波特率
    def bps_switch(self):
        self.ser.bps = setting.bps_list[self.ui.bps_comboBox.currentIndex()]
    #用于直接设定手势
    def gesture_set(self):
        self.ser.gesture_set(self.cnt,self.time_move,self.ids,self.pos)
    #用于改变slider值时更新各个手的pos值
    def pos_update_slider(self):
        self.pos = [
                    self.ui.finger_0_horizontalSlider.value(),
                    self.ui.finger_1_horizontalSlider.value(),
                    self.ui.finger_2_horizontalSlider.value(),
                    self.ui.finger_3_horizontalSlider.value(),
                    self.ui.finger_4_horizontalSlider.value(),
                    self.ui.finger_5_horizontalSlider.value()
                    ]
        self.ui.
    #用于改变spinbox值时更新手的pos值
    def pos_update_spinbox(self):


