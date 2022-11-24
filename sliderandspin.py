# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sliderandspin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class SliderAndSpin(QtWidgets.QWidget):
    def __init__(self,parent = None):
        super(SliderAndSpin, self).__init__(parent)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QtCore.QSize(50,20))
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setMinimumSize(QtCore.QSize(50, 20))
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.horizontalSlider = QtWidgets.QSlider(self)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(200, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)

        #数值上下限的设置
        self.horizontalSlider.setMinimum(900)
        self.horizontalSlider.setMaximum(2000)
        self.spinBox.setMinimum(900)
        self.spinBox.setMaximum(2000)

        #信号与槽函数的连接
        self.horizontalSlider.valueChanged.connect(self.spinbox_set)
        self.spinBox.valueChanged.connect(self.slider_set)

    def slider_set(self):
        self.horizontalSlider.setValue(self.spinBox.value())
    def spinbox_set(self):
        self.spinBox.setValue(self.horizontalSlider.value())