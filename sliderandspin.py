# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sliderandspin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

# class Ui_SliderAndSpin(QWiget):
#     def __init__(self, SliderAndSpin):
#         super(QWidget, self).__init__()
#     def setupUi(self, SliderAndSpin):
#         SliderAndSpin.setObjectName("SliderAndSpin")
#         SliderAndSpin.resize(400, 300)
#         SliderAndSpin.setMinimumSize(QtCore.QSize(0, 0))
#         self.horizontalLayout = QtWidgets.QHBoxLayout(SliderAndSpin)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.spinBox = QtWidgets.QSpinBox(SliderAndSpin)
#         self.spinBox.setMinimumSize(QtCore.QSize(100, 30))
#         self.spinBox.setObjectName("spinBox")
#         self.horizontalLayout.addWidget(self.spinBox)
#         self.horizontalSlider = QtWidgets.QSlider(SliderAndSpin)
#         self.horizontalSlider.setMinimumSize(QtCore.QSize(100, 30))
#         self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
#         self.horizontalSlider.setObjectName("horizontalSlider")
#         self.horizontalLayout.addWidget(self.horizontalSlider)
#
#         self.horizontalSlider.valueChanged.connect(self.spinbox_set)
#         self.spinBox.valueChanged.connect(self.slider_set)
#
#
#         self.retranslateUi(SliderAndSpin)
#         QtCore.QMetaObject.connectSlotsByName(SliderAndSpin)
#
#     def spinbox_set(self):
#         self.spinBox.setValue(self.horizontalSlider.value())
#
#     def slider_set(self):
#         self.horizontalSlider.setValue(self.spinBox.value())
#
#     def retranslateUi(self, SliderAndSpin):
#         _translate = QtCore.QCoreApplication.translate
#         SliderAndSpin.setWindowTitle(_translate("SliderAndSpin", "Form"))

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