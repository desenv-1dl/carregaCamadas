# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def __init__(self, Dialog, iface):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.estilo = None
        self.iface = iface
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        
        
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
        "font: 63 italic 14pt \"Ubuntu\";\n"
        "color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 63 italic 14pt \"Ubuntu\";"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 255, 255);\n"
        "font: 63 italic 14pt \"Ubuntu\";"))
        self.label_4.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.comboBox_4 = QtGui.QComboBox(Dialog)
        self.comboBox_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 63 italic 14pt \"Ubuntu\";"))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        
        self.verticalLayout_4.addWidget(self.comboBox_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 255, 255);\n"
        "font: 63 italic 14pt \"Ubuntu\";"))
        self.label_5.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 255, 255);\n"
        "font: 63 italic 14pt \"Ubuntu\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);\n"
        "font: 63 italic 14pt \"Ubuntu\";"))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
        "font: 63 italic 14pt \"Ubuntu\";\n"
        "\n"
        ""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Carrega Camadas", None))
        self.label.setText(_translate("Dialog", "Selecione a conexão:", None))
        self.comboBox.setItemText(0, _translate("Dialog", "Selecione ...", None))
        self.label_2.setText(_translate("Dialog", "Selecione a forma de carregamento:", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Selecione ...", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Carregar camadas com geometria", None))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Carregar todas as camadas", None))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Carregar Classes da Cobertura Terrestre", None))
        self.label_4.setText(_translate("Dialog", "Selecione o tipo de estilo:", None))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Selecione ...", None))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Estilo de Aquisição", None))
        self.comboBox_4.setItemText(2, _translate("Dialog", "Estilo de Reambulação", None))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Estilo de Revisão", None))
        self.comboBox_4.setItemText(4, _translate("Dialog", "Estilo de Vetorização", None))
        self.pushButton.setText(_translate("Dialog", "Carregar", None))
    
    def selecionarEstilos(self, e):
        if e == 4:
            self.estilo = QtGui.QFileDialog(self.iface.mainWindow()).getExistingDirectory()	   
            self.label_5.setText(self.estilo)




