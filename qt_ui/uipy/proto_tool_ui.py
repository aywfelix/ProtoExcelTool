# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/proto_tool.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProtoWindow(object):
    def setupUi(self, ProtoWindow):
        ProtoWindow.setObjectName("ProtoWindow")
        ProtoWindow.resize(904, 797)
        self.centralwidget = QtWidgets.QWidget(ProtoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 881, 741))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.label_2.setObjectName("label_2")
        self.lEtProtoSearch = QtWidgets.QLineEdit(self.tab)
        self.lEtProtoSearch.setGeometry(QtCore.QRect(50, 10, 261, 21))
        self.lEtProtoSearch.setObjectName("lEtProtoSearch")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(320, 40, 541, 671))
        self.groupBox.setObjectName("groupBox")
        self.lEtProtoId = QtWidgets.QLineEdit(self.groupBox)
        self.lEtProtoId.setEnabled(True)
        self.lEtProtoId.setGeometry(QtCore.QRect(90, 30, 431, 20))
        self.lEtProtoId.setReadOnly(True)
        self.lEtProtoId.setObjectName("lEtProtoId")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label_3.setObjectName("label_3")
        self.lEtProtoName = QtWidgets.QLineEdit(self.groupBox)
        self.lEtProtoName.setGeometry(QtCore.QRect(90, 70, 431, 20))
        self.lEtProtoName.setReadOnly(True)
        self.lEtProtoName.setObjectName("lEtProtoName")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.label_6.setObjectName("label_6")
        self.tEtProtoContent = QtWidgets.QTextEdit(self.groupBox)
        self.tEtProtoContent.setGeometry(QtCore.QRect(90, 170, 431, 431))
        self.tEtProtoContent.setReadOnly(True)
        self.tEtProtoContent.setObjectName("tEtProtoContent")
        self.bTnProtoModify = QtWidgets.QPushButton(self.groupBox)
        self.bTnProtoModify.setGeometry(QtCore.QRect(290, 630, 75, 23))
        self.bTnProtoModify.setObjectName("bTnProtoModify")
        self.tEtProtoDesc = QtWidgets.QTextEdit(self.groupBox)
        self.tEtProtoDesc.setGeometry(QtCore.QRect(90, 110, 431, 41))
        self.tEtProtoDesc.setReadOnly(True)
        self.tEtProtoDesc.setObjectName("tEtProtoDesc")
        self.cBxProtocol = QtWidgets.QCheckBox(self.groupBox)
        self.cBxProtocol.setGeometry(QtCore.QRect(90, 630, 121, 16))
        self.cBxProtocol.setMouseTracking(True)
        self.cBxProtocol.setCheckable(True)
        self.cBxProtocol.setObjectName("cBxProtocol")
        self.tRvProtocol = QtWidgets.QTreeWidget(self.tab)
        self.tRvProtocol.setGeometry(QtCore.QRect(10, 40, 301, 671))
        self.tRvProtocol.setRootIsDecorated(True)
        self.tRvProtocol.setHeaderHidden(True)
        self.tRvProtocol.setObjectName("tRvProtocol")
        self.tRvProtocol.headerItem().setText(0, "1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.label.setObjectName("label")
        self.lEtEnumSearch = QtWidgets.QLineEdit(self.tab_2)
        self.lEtEnumSearch.setGeometry(QtCore.QRect(50, 10, 261, 21))
        self.lEtEnumSearch.setObjectName("lEtEnumSearch")
        self.tRvEnum = QtWidgets.QTreeView(self.tab_2)
        self.tRvEnum.setGeometry(QtCore.QRect(10, 40, 301, 671))
        self.tRvEnum.setObjectName("tRvEnum")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 40, 541, 671))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lEtEnumName = QtWidgets.QLineEdit(self.groupBox_2)
        self.lEtEnumName.setGeometry(QtCore.QRect(90, 30, 431, 20))
        self.lEtEnumName.setObjectName("lEtEnumName")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label_7.setObjectName("label_7")
        self.lEtEnumDesc = QtWidgets.QLineEdit(self.groupBox_2)
        self.lEtEnumDesc.setGeometry(QtCore.QRect(90, 70, 431, 20))
        self.lEtEnumDesc.setObjectName("lEtEnumDesc")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.label_10.setObjectName("label_10")
        self.bTnEnumUpdate = QtWidgets.QPushButton(self.groupBox_2)
        self.bTnEnumUpdate.setGeometry(QtCore.QRect(290, 630, 75, 23))
        self.bTnEnumUpdate.setObjectName("bTnEnumUpdate")
        self.cBxEnum = QtWidgets.QCheckBox(self.groupBox_2)
        self.cBxEnum.setGeometry(QtCore.QRect(90, 630, 121, 16))
        self.cBxEnum.setObjectName("cBxEnum")
        self.tBvEnum = QtWidgets.QTableView(self.groupBox_2)
        self.tBvEnum.setGeometry(QtCore.QRect(90, 110, 431, 491))
        self.tBvEnum.setObjectName("tBvEnum")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.toolButton = QtWidgets.QToolButton(self.tab_3)
        self.toolButton.setGeometry(QtCore.QRect(10, 10, 151, 51))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_2.setGeometry(QtCore.QRect(340, 10, 151, 51))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.tab_3)
        self.toolButton_3.setGeometry(QtCore.QRect(640, 20, 151, 51))
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(420, 90, 54, 12))
        self.label_11.setObjectName("label_11")
        self.spinBox = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox.setGeometry(QtCore.QRect(490, 81, 161, 31))
        self.spinBox.setAutoFillBackground(False)
        self.spinBox.setAccelerated(True)
        self.spinBox.setMaximum(65535)
        self.spinBox.setObjectName("spinBox")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 120, 641, 231))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 360, 861, 351))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(700, 220, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(90, 80, 241, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(680, 160, 181, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(680, 130, 141, 16))
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab_3, "")
        ProtoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProtoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        ProtoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProtoWindow)
        self.statusbar.setObjectName("statusbar")
        ProtoWindow.setStatusBar(self.statusbar)
        self.menuExportExcel = QtWidgets.QAction(ProtoWindow)
        self.menuExportExcel.setObjectName("menuExportExcel")
        self.menuExportServerPb = QtWidgets.QAction(ProtoWindow)
        self.menuExportServerPb.setObjectName("menuExportServerPb")
        self.menuExportClientPb = QtWidgets.QAction(ProtoWindow)
        self.menuExportClientPb.setObjectName("menuExportClientPb")
        self.menuSave = QtWidgets.QAction(ProtoWindow)
        self.menuSave.setObjectName("menuSave")
        self.menuExit = QtWidgets.QAction(ProtoWindow)
        self.menuExit.setObjectName("menuExit")
        self.menuOpenSetting = QtWidgets.QAction(ProtoWindow)
        self.menuOpenSetting.setObjectName("menuOpenSetting")
        self.menuExportProto = QtWidgets.QAction(ProtoWindow)
        self.menuExportProto.setObjectName("menuExportProto")
        self.menuFile.addAction(self.menuSave)
        self.menuFile.addAction(self.menuExit)
        self.menuSetting.addAction(self.menuOpenSetting)
        self.menuExport.addAction(self.menuExportExcel)
        self.menuExport.addSeparator()
        self.menuExport.addAction(self.menuExportServerPb)
        self.menuExport.addAction(self.menuExportClientPb)
        self.menuExport.addSeparator()
        self.menuExport.addAction(self.menuExportProto)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(ProtoWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(ProtoWindow)

    def retranslateUi(self, ProtoWindow):
        _translate = QtCore.QCoreApplication.translate
        ProtoWindow.setWindowTitle(_translate("ProtoWindow", "游戏协议工具"))
        self.label_2.setText(_translate("ProtoWindow", "搜索："))
        self.groupBox.setTitle(_translate("ProtoWindow", "详细信息"))
        self.label_3.setText(_translate("ProtoWindow", "协议编号："))
        self.label_4.setText(_translate("ProtoWindow", "协议名称："))
        self.label_5.setText(_translate("ProtoWindow", "协议说明："))
        self.label_6.setText(_translate("ProtoWindow", "协议内容："))
        self.bTnProtoModify.setText(_translate("ProtoWindow", "修改"))
        self.cBxProtocol.setText(_translate("ProtoWindow", "仅导出服务器"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ProtoWindow", "协议管理器"))
        self.label.setText(_translate("ProtoWindow", "搜索："))
        self.groupBox_2.setTitle(_translate("ProtoWindow", "详细信息"))
        self.label_7.setText(_translate("ProtoWindow", "枚举名称："))
        self.label_8.setText(_translate("ProtoWindow", "枚举说明："))
        self.label_10.setText(_translate("ProtoWindow", "枚举字段："))
        self.bTnEnumUpdate.setText(_translate("ProtoWindow", "修改"))
        self.cBxEnum.setText(_translate("ProtoWindow", "仅导出服务器"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ProtoWindow", "枚举管理器"))
        self.toolButton.setText(_translate("ProtoWindow", "连接到服务器"))
        self.toolButton_2.setText(_translate("ProtoWindow", "断开连接"))
        self.toolButton_3.setText(_translate("ProtoWindow", "清空文本框"))
        self.label_9.setText(_translate("ProtoWindow", "服务器地址："))
        self.label_11.setText(_translate("ProtoWindow", "端口："))
        self.pushButton.setText(_translate("ProtoWindow", "发送消息"))
        self.comboBox.setItemText(0, _translate("ProtoWindow", "127.0.0.1"))
        self.comboBox_2.setItemText(0, _translate("ProtoWindow", "1101"))
        self.comboBox_2.setItemText(1, _translate("ProtoWindow", "1102"))
        self.label_12.setText(_translate("ProtoWindow", "选择发送协议号："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("ProtoWindow", "协议测试"))
        self.menuFile.setTitle(_translate("ProtoWindow", "文件"))
        self.menuSetting.setTitle(_translate("ProtoWindow", "设置"))
        self.menuExport.setTitle(_translate("ProtoWindow", "导出"))
        self.menuExportExcel.setText(_translate("ProtoWindow", "导出配置表[excel]"))
        self.menuExportServerPb.setText(_translate("ProtoWindow", "导出服务器[pb]"))
        self.menuExportClientPb.setText(_translate("ProtoWindow", "导出客户端[pb]"))
        self.menuSave.setText(_translate("ProtoWindow", "保存"))
        self.menuExit.setText(_translate("ProtoWindow", "关闭"))
        self.menuOpenSetting.setText(_translate("ProtoWindow", "打开设置"))
        self.menuExportProto.setText(_translate("ProtoWindow", "导出proto"))
