from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
import mainwindow
import setting
import m_serial
import sys

class InterFace(QMainWindow):
    def __init__(self):
        super(InterFace, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ser = m_serial.MySerial()
        self.ids = [6,1,2,3,4,5]
        self.pos = [900,900,900,900,900,900]
        self.cnt = 6
        self.time_move = 0
        self.ui_init()
    def ui_init(self):
        '''
        窗口组件初始化
        '''
        #串口下拉选单初始化
        for i in range(len(self.ser.port_list)):
            self.ui.com_comboBox.addItem(self.ser.port_list[i][0])
        #波特率下拉选单初始化
        bps_list = [str(i) for i in setting.bps_list]
        self.ui.bps_comboBox.addItems(bps_list)
        self.ser.bps = setting.bps_list[self.ui.bps_comboBox.currentIndex()]

        #上下限初始化
        self.ui.time_spinBox.setMinimum(0)
        self.ui.time_spinBox.setMaximum(2000)

        #滑动条和spinbox标签命名
        self.ui.slider_spin_0.label.setText("手掌")
        self.ui.slider_spin_1.label.setText("拇指")
        self.ui.slider_spin_2.label.setText("食指")
        self.ui.slider_spin_3.label.setText("中指")
        self.ui.slider_spin_4.label.setText("无名指")
        self.ui.slider_spin_5.label.setText("小指")
        '''
        槽函数与信号连接
        '''
        #串口选择改变
        self.ui.com_comboBox.currentIndexChanged.connect(self.com_switch)
        #波特率选择改变
        self.ui.bps_comboBox.currentIndexChanged.connect(self.bps_switch)
        #串口控制按钮按下
        self.ui.com_connect_pushButton.clicked.connect(self.com_connect)
        self.ui.com_close_pushButton.clicked.connect(self.com_close)

        #移动用时spinbox改变
        self.ui.time_spinBox.valueChanged.connect(self.time_move_set)
        #手势pos改变
        self.ui.slider_spin_0.horizontalSlider.valueChanged.connect(self.pos_update_slider_spin_0)
        self.ui.slider_spin_1.horizontalSlider.valueChanged.connect(self.pos_update_slider_spin_1)
        self.ui.slider_spin_2.horizontalSlider.valueChanged.connect(self.pos_update_slider_spin_2)
        self.ui.slider_spin_3.horizontalSlider.valueChanged.connect(self.pos_update_slider_spin_3)
        self.ui.slider_spin_4.horizontalSlider.valueChanged.connect(self.pos_update_slider_spin_4)
        self.ui.slider_spin_5.horizontalSlider.valueChanged.connect(self.pos_update_slider_spin_5)
        #切换到预设姿势
        self.ui.gesture_0_pushButton.clicked.connect(self.default_gesture_0_set)
        self.ui.gesture_1_pushButton.clicked.connect(self.default_gesture_1_set)
        self.ui.gesture_2_pushButton.clicked.connect(self.default_gesture_2_set)
        self.ui.gesture_3_pushButton.clicked.connect(self.default_gesture_3_set)
        self.ui.gesture_4_pushButton.clicked.connect(self.default_gesture_4_set)
        self.ui.gesture_5_pushButton.clicked.connect(self.default_gesture_5_set)
    #用于切换串口
    def com_switch(self):
        self.ser.port = self.ser.port_list[self.ui.com_comboBox.currentIndex()][0]
    #用于切换波特率
    def bps_switch(self):
        self.ser.bps = setting.bps_list[self.ui.bps_comboBox.currentIndex()]
    def com_connect(self):
        self.ser.port_connect()
        self.ui.com_connect_pushButton.setEnabled(False)
    def com_close(self):
        self.ser.port_close()
        self.ui.com_connect_pushButton.setEnabled(True)

    #用于修改移动用时
    def time_move_set(self):
        self.time_move = self.ui.time_spinBox.value()

    #用于直接设定手势
    def gesture_set(self):
        self.ser.gesture_set(self.cnt,self.time_move,self.ids,self.pos)
    #改变slider_spin值时更新对应手的值
    def pos_update_slider_spin_0(self):
        self.pos[0] = self.ui.slider_spin_0.horizontalSlider.value()
        self.gesture_set()
    def pos_update_slider_spin_1(self):
        self.pos[1] = self.ui.slider_spin_1.horizontalSlider.value()
        self.gesture_set()
    def pos_update_slider_spin_2(self):
        self.pos[2] = self.ui.slider_spin_2.horizontalSlider.value()
        self.gesture_set()
    def pos_update_slider_spin_3(self):
        self.pos[3] = self.ui.slider_spin_3.horizontalSlider.value()
        self.gesture_set()
    def pos_update_slider_spin_4(self):
        self.pos[4] = self.ui.slider_spin_4.horizontalSlider.value()
        self.gesture_set()
    def pos_update_slider_spin_5(self):
        self.pos[5] = self.ui.slider_spin_5.horizontalSlider.value()
        self.gesture_set()
    #用于改变slider值时更新各个手的pos值

    def pos_update_default(self):
        self.ui.slider_spin_0.horizontalSlider.setValue(self.pos[0])
        self.ui.slider_spin_1.horizontalSlider.setValue(self.pos[1])
        self.ui.slider_spin_2.horizontalSlider.setValue(self.pos[2])
        self.ui.slider_spin_3.horizontalSlider.setValue(self.pos[3])
        self.ui.slider_spin_4.horizontalSlider.setValue(self.pos[4])
        self.ui.slider_spin_5.horizontalSlider.setValue(self.pos[5])

    #用于将手切换到预设手势
    def default_gesture_0_set(self):
        self.pos = setting.default_pos[0]
        self.pos_update_default()
    def default_gesture_1_set(self):
        self.pos = setting.default_pos[1]
        self.pos_update_default()
    def default_gesture_2_set(self):
        self.pos = setting.default_pos[2]
        self.pos_update_default()
    def default_gesture_3_set(self):
        self.pos = setting.default_pos[3]
        self.pos_update_default()
    def default_gesture_4_set(self):
        self.pos = setting.default_pos[4]
        self.pos_update_default()
    def default_gesture_5_set(self):
        self.pos = setting.default_pos[5]
        self.pos_update_default()


if __name__ == "__main__":
    app = QApplication([])
    main = InterFace()
    main.show()
    sys.exit(app.exec_())