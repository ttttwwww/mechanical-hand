# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sliderandspin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_SliderAndSpin(QWiget):
    def __init__(self, SliderAndSpin):
        super(QWidget, self).__init__()
    def setupUi(self, SliderAndSpin):
        SliderAndSpin.setObjectName("SliderAndSpin")
        SliderAndSpin.resize(400, 300)
        SliderAndSpin.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(SliderAndSpin)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(SliderAndSpin)
        self.spinBox.setMinimumSize(QtCore.QSize(100, 30))
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.horizontalSlider = QtWidgets.QSlider(SliderAndSpin)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(100, 30))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)

        self.horizontalSlider.valueChanged.connect(self.spinbox_set)
        self.spinBox.valueChanged.connect(self.slider_set)


        self.retranslateUi(SliderAndSpin)
        QtCore.QMetaObject.connectSlotsByName(SliderAndSpin)

    def spinbox_set(self):
        self.spinBox.setValue(self.horizontalSlider.value())

    def slider_set(self):
        self.horizontalSlider.setValue(self.spinBox.value())

    def retranslateUi(self, SliderAndSpin):
        _translate = QtCore.QCoreApplication.translate
        SliderAndSpin.setWindowTitle(_translate("SliderAndSpin", "Form"))

