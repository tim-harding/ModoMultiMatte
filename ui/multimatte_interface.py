# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\multimatte_interface.ui'
#
# Created: Fri Jan 22 08:18:32 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 373)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(57, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mmValRadio = QtGui.QRadioButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mmValRadio.sizePolicy().hasHeightForWidth())
        self.mmValRadio.setSizePolicy(sizePolicy)
        self.mmValRadio.setObjectName("mmValRadio")
        self.horizontalLayout.addWidget(self.mmValRadio)
        self.matRadio = QtGui.QRadioButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matRadio.sizePolicy().hasHeightForWidth())
        self.matRadio.setSizePolicy(sizePolicy)
        self.matRadio.setChecked(True)
        self.matRadio.setObjectName("matRadio")
        self.horizontalLayout.addWidget(self.matRadio)
        self.animCheckBox = QtGui.QCheckBox(Form)
        self.animCheckBox.setObjectName("animCheckBox")
        self.horizontalLayout.addWidget(self.animCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mmValBox = QtGui.QSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mmValBox.sizePolicy().hasHeightForWidth())
        self.mmValBox.setSizePolicy(sizePolicy)
        self.mmValBox.setObjectName("mmValBox")
        self.horizontalLayout_3.addWidget(self.mmValBox)
        self.mmValButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mmValButton.sizePolicy().hasHeightForWidth())
        self.mmValButton.setSizePolicy(sizePolicy)
        self.mmValButton.setObjectName("mmValButton")
        self.horizontalLayout_3.addWidget(self.mmValButton)
        self.randButton = QtGui.QPushButton(Form)
        self.randButton.setObjectName("randButton")
        self.horizontalLayout_3.addWidget(self.randButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem3 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.renderButton = QtGui.QPushButton(Form)
        self.renderButton.setObjectName("renderButton")
        self.horizontalLayout_2.addWidget(self.renderButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem7 = QtGui.QSpacerItem(57, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.mmValRadio.setText(QtGui.QApplication.translate("Form", "mmVal", None, QtGui.QApplication.UnicodeUTF8))
        self.matRadio.setText(QtGui.QApplication.translate("Form", "Material", None, QtGui.QApplication.UnicodeUTF8))
        self.animCheckBox.setText(QtGui.QApplication.translate("Form", "Animation", None, QtGui.QApplication.UnicodeUTF8))
        self.mmValButton.setText(QtGui.QApplication.translate("Form", "Set mmVal", None, QtGui.QApplication.UnicodeUTF8))
        self.randButton.setText(QtGui.QApplication.translate("Form", "Randomize", None, QtGui.QApplication.UnicodeUTF8))
        self.renderButton.setText(QtGui.QApplication.translate("Form", "Render", None, QtGui.QApplication.UnicodeUTF8))
