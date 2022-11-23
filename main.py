from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
import mainwindow
import setting
import m_serial


class InterFace(QMainWindow):
    def __init__(self):
        super(InterFace, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ser = m_serial.MySerial()
        self.ids = [0,1,2,3,4,5]
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
        #滑动条和spinbox上下限初始化
        self.ui.finger_0_horizontalSlider.setMinimum(900)
        self.ui.finger_1_horizontalSlider.setMinimum(900)
        self.ui.finger_2_horizontalSlider.setMinimum(900)
        self.ui.finger_3_horizontalSlider.setMinimum(900)
        self.ui.finger_4_horizontalSlider.setMinimum(900)
        self.ui.finger_5_horizontalSlider.setMinimum(900)

        self.ui.finger_0_horizontalSlider.setMaximum(2000)
        self.ui.finger_1_horizontalSlider.setMaximum(2000)
        self.ui.finger_2_horizontalSlider.setMaximum(2000)
        self.ui.finger_3_horizontalSlider.setMaximum(2000)
        self.ui.finger_4_horizontalSlider.setMaximum(2000)
        self.ui.finger_5_horizontalSlider.setMaximum(2000)

        self.ui.finger_0_spinbox.setMinimum(900)
        self.ui.finger_1_spinbox.setMinimum(900)
        self.ui.finger_2_spinbox.setMinimum(900)
        self.ui.finger_3_spinbox.setMinimum(900)
        self.ui.finger_4_spinbox.setMinimum(900)
        self.ui.finger_5_spinbox.setMinimum(900)

        self.ui.finger_0_spinbox.setMaximum(2000)
        self.ui.finger_1_spinbox.setMaximum(2000)
        self.ui.finger_2_spinbox.setMaximum(2000)
        self.ui.finger_3_spinbox.setMaximum(2000)
        self.ui.finger_4_spinbox.setMaximum(2000)
        self.ui.finger_5_spinbox.setMaximum(2000)

        '''
        槽函数与信号连接
        '''
        #串口选择改变
        self.ui.com_comboBox.currentIndexChanged.connect(self.com_switch)
        #波特率选择改变
        self.ui.bps_comboBox.currentIndexChanged.connect(self.bps_switch)
        #手势调整按钮按下
        self.ui.finger_set_pushbutton.clicked.connect(self.gesture_set)
        #串口控制按钮按下
        self.ui.com_connect_pushButton.clicked.connect(self.com_connect)
        self.ui.com_close_pushButton.clicked.connect(self.com_close)


        #手势pos改变
        self.ui.finger_0_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_1_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_2_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_3_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_4_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        self.ui.finger_5_horizontalSlider.valueChanged.connect(self.pos_update_slider)
        #
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
    def com_connect(self):
        self.ser.port_connect()
        self.ui.com_connect_pushButton.setEnabled(False)
    def com_close(self):
        self.ser.port_close()
        self.ui.com_connect_pushButton.setEnabled(True)
    #用于直接设定手势
    def gesture_set(self):
        print(self.pos)
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
        self.ui.finger_0_spinbox.setValue(self.pos[0])
        self.ui.finger_1_spinbox.setValue(self.pos[1])
        self.ui.finger_2_spinbox.setValue(self.pos[2])
        self.ui.finger_3_spinbox.setValue(self.pos[3])
        self.ui.finger_4_spinbox.setValue(self.pos[4])
        self.ui.finger_5_spinbox.setValue(self.pos[5])

        self.gesture_set()
    #用于改变spinbox值时更新手的pos值
    def pos_update_spinbox(self):
        self.pos = [
            self.ui.finger_0_spinbox.value(),
            self.ui.finger_1_spinbox.value(),
            self.ui.finger_2_spinbox.value(),
            self.ui.finger_3_spinbox.value(),
            self.ui.finger_4_spinbox.value(),
            self.ui.finger_5_spinbox.value()
        ]
        self.ui.finger_0_horizontalSlider.setValue(self.pos[0])
        self.ui.finger_1_horizontalSlider.setValue(self.pos[1])
        self.ui.finger_2_horizontalSlider.setValue(self.pos[2])
        self.ui.finger_3_horizontalSlider.setValue(self.pos[3])
        self.ui.finger_4_horizontalSlider.setValue(self.pos[4])
        self.ui.finger_5_horizontalSlider.setValue(self.pos[5])

if __name__ == "__main__":
    app = QApplication([])
    main = InterFace()
    main.show()
    sys.exit(app.exec_())