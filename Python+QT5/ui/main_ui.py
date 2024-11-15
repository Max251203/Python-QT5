# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Max\Labs\KSKR\CourseWork\program\ui\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1302, 932)
        MainWindow.setStyleSheet("*{color:rgb(198, 226, 255);}\n"
"#centralwidget{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"}\n"
"#inputFrame,#buttonFrame{\n"
"    border:2px outset rgb(0, 191, 255);\n"
"    border-radius:10px;\n"
"    background-color: rgba(0, 0, 0, 0.6);\n"
"}\n"
"QLabel{\n"
"    padding:2px;\n"
"    min-height:38px;\n"
"    border:none;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QComboBox{\n"
"    padding:2px;\n"
"    min-height:38px;\n"
"    min-width:150px;\n"
"    border:1px solid rgb(0, 191, 255);\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"}\n"
"QComboBox::drop-down{border: 0px;}\n"
"QComboBox::down-arrow{\n"
"     width:12px;\n"
"    height:12px;\n"
"    border:1px solid rgb(0, 191, 255);\n"
"    margin-right:15px;\n"
"}\n"
"QComboBox:on{border:2px solid #c6e2ff;}\n"
"QComboBox QListView{\n"
"    font-size: 12px;\n"
"    border:1px solid rgb(0, 191, 255);\n"
"    padding: 5px;\n"
"    background-color: rgb(75, 0, 130);\n"
"    outline: none;\n"
"}\n"
"QSlider{min-width:150px;}\n"
"QSlider::groove:horizontal{\n"
"    height:1px;\n"
"    border:1px solid rgba(0,0,0,0);\n"
"}\n"
"QSlider::handle:horizontal{\n"
"    background: rgb(0,0,0);\n"
"    width: 20px;\n"
"    margin: -10px -1px;\n"
"    border: 1px solid  rgb(0, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QSlider::handle:horizontal:hover{background:rgb(0, 255, 255);}\n"
"QSlider::add-page:horizontal{background-color: rgb(70, 130, 180);}\n"
"QSlider::sub-page:horizontal{background:rgb(0, 255, 255);}\n"
"QLineEdit{\n"
"    min-height:38px;\n"
"    padding:2px;\n"
"    border:1px solid rgb(0, 191, 255);\n"
"    border-radius: 10px;\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"QLineEdit:focus{border:2px solid #c6e2ff;}\n"
"#step_box{\n"
"    min-width:50px;\n"
"    max-width:100px;\n"
"    border-radius: 10px;\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"QPushButton{\n"
"    min-height:35px;\n"
"    padding:2px;\n"
"    border:2px outset rgb(0, 191, 255);\n"
"    border-radius: 10px;\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0.994, stop:0 rgba(255, 0, 223, 44), stop:1 rgba(0, 0, 255, 49));\n"
"}\n"
"QPushButton:pressed {\n"
" background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0.994, stop:0 rgba(255, 0, 223, 44), stop:1 rgba(0, 0, 255, 49));\n"
"}\n"
"#ansysCheck{\n"
"    min-height:35px;\n"
"    padding:2px;\n"
"    spacing:10px;\n"
"    border-radius: 10px;\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"#ansysCheck::indicator{height:25px;width:25px;}\n"
"QMessageBox{\n"
"    border:2px solid rgb(0, 191, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"}\n"
"QTabWidget::pane{border: 2px solid rgb(0, 191, 255);border-radius: 10px;} \n"
"QTabWidget::tab-bar{left: 20px;}\n"
"QTabBar::tab {\n"
"    min-height:50px;\n"
"    min-width:300px;\n"
"      background: rgba(0, 0, 0, 0.6); \n"
"     border: 2px solid rgb(0, 191, 255);\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"      padding: 2px;\n"
"    font: 12pt \"Bahnschrift Condensed\";\n"
"} \n"
"QTabBar::tab:!selected {margin-top: 5px;}\n"
"QTabWidget QWidget{border-width: 0px;}\n"
"#MplWidget1, #MplWidget2, #MplWidget3{\n"
"    min-width:1274px;\n"
"    min-height:688px;\n"
"    border-radius:10px;\n"
"    background: rgba(0, 0, 0, 0.6); \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.inputFrame = QtWidgets.QFrame(self.centralwidget)
        self.inputFrame.setStyleSheet("")
        self.inputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputFrame.setObjectName("inputFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.inputFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label1 = QtWidgets.QLabel(self.inputFrame)
        self.label1.setMinimumSize(QtCore.QSize(0, 42))
        self.label1.setObjectName("label1")
        self.horizontalLayout_2.addWidget(self.label1)
        self.materialSelect = QtWidgets.QComboBox(self.inputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.materialSelect.sizePolicy().hasHeightForWidth())
        self.materialSelect.setSizePolicy(sizePolicy)
        self.materialSelect.setMinimumSize(QtCore.QSize(156, 44))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.materialSelect.setFont(font)
        self.materialSelect.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.materialSelect.setEditable(False)
        self.materialSelect.setFrame(True)
        self.materialSelect.setObjectName("materialSelect")
        self.horizontalLayout_2.addWidget(self.materialSelect)
        self.label2 = QtWidgets.QLabel(self.inputFrame)
        self.label2.setMinimumSize(QtCore.QSize(0, 42))
        self.label2.setObjectName("label2")
        self.horizontalLayout_2.addWidget(self.label2)
        self.thicknessInput = QtWidgets.QLineEdit(self.inputFrame)
        self.thicknessInput.setMinimumSize(QtCore.QSize(0, 44))
        self.thicknessInput.setObjectName("thicknessInput")
        self.horizontalLayout_2.addWidget(self.thicknessInput)
        self.label3 = QtWidgets.QLabel(self.inputFrame)
        self.label3.setMinimumSize(QtCore.QSize(0, 42))
        self.label3.setObjectName("label3")
        self.horizontalLayout_2.addWidget(self.label3)
        self.forceInput = QtWidgets.QLineEdit(self.inputFrame)
        self.forceInput.setMinimumSize(QtCore.QSize(0, 44))
        self.forceInput.setObjectName("forceInput")
        self.horizontalLayout_2.addWidget(self.forceInput)
        self.label4 = QtWidgets.QLabel(self.inputFrame)
        self.label4.setMinimumSize(QtCore.QSize(0, 42))
        self.label4.setObjectName("label4")
        self.horizontalLayout_2.addWidget(self.label4)
        self.angleInput = QtWidgets.QLineEdit(self.inputFrame)
        self.angleInput.setMinimumSize(QtCore.QSize(0, 44))
        self.angleInput.setObjectName("angleInput")
        self.horizontalLayout_2.addWidget(self.angleInput)
        self.label5 = QtWidgets.QLabel(self.inputFrame)
        self.label5.setMinimumSize(QtCore.QSize(0, 42))
        self.label5.setObjectName("label5")
        self.horizontalLayout_2.addWidget(self.label5)
        self.meshStepSelect = QtWidgets.QSlider(self.inputFrame)
        self.meshStepSelect.setMinimumSize(QtCore.QSize(150, 0))
        self.meshStepSelect.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.meshStepSelect.setOrientation(QtCore.Qt.Horizontal)
        self.meshStepSelect.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.meshStepSelect.setObjectName("meshStepSelect")
        self.horizontalLayout_2.addWidget(self.meshStepSelect)
        self.step_box = QtWidgets.QLabel(self.inputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step_box.sizePolicy().hasHeightForWidth())
        self.step_box.setSizePolicy(sizePolicy)
        self.step_box.setMinimumSize(QtCore.QSize(54, 42))
        self.step_box.setMaximumSize(QtCore.QSize(104, 16777215))
        self.step_box.setText("")
        self.step_box.setObjectName("step_box")
        self.horizontalLayout_2.addWidget(self.step_box)
        self.verticalLayout_5.addWidget(self.inputFrame)
        self.buttonFrame = QtWidgets.QFrame(self.centralwidget)
        self.buttonFrame.setStyleSheet("")
        self.buttonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonFrame.setObjectName("buttonFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttonFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.materialsButton = QtWidgets.QPushButton(self.buttonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.materialsButton.sizePolicy().hasHeightForWidth())
        self.materialsButton.setSizePolicy(sizePolicy)
        self.materialsButton.setMinimumSize(QtCore.QSize(0, 43))
        self.materialsButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.materialsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.materialsButton.setObjectName("materialsButton")
        self.horizontalLayout.addWidget(self.materialsButton)
        self.execButton = QtWidgets.QPushButton(self.buttonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.execButton.sizePolicy().hasHeightForWidth())
        self.execButton.setSizePolicy(sizePolicy)
        self.execButton.setMinimumSize(QtCore.QSize(0, 43))
        self.execButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.execButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.execButton.setObjectName("execButton")
        self.horizontalLayout.addWidget(self.execButton)
        self.ansysButton = QtWidgets.QPushButton(self.buttonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ansysButton.sizePolicy().hasHeightForWidth())
        self.ansysButton.setSizePolicy(sizePolicy)
        self.ansysButton.setMinimumSize(QtCore.QSize(0, 43))
        self.ansysButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ansysButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ansysButton.setObjectName("ansysButton")
        self.horizontalLayout.addWidget(self.ansysButton)
        self.ansysCheck = QtWidgets.QCheckBox(self.buttonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ansysCheck.sizePolicy().hasHeightForWidth())
        self.ansysCheck.setSizePolicy(sizePolicy)
        self.ansysCheck.setMinimumSize(QtCore.QSize(0, 39))
        self.ansysCheck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ansysCheck.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ansysCheck.setTristate(False)
        self.ansysCheck.setObjectName("ansysCheck")
        self.horizontalLayout.addWidget(self.ansysCheck)
        self.verticalLayout_5.addWidget(self.buttonFrame)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.MplWidget1 = QtWidgets.QWidget()
        self.MplWidget1.setMinimumSize(QtCore.QSize(1274, 688))
        self.MplWidget1.setObjectName("MplWidget1")
        self.companovka_for_mpl1 = QtWidgets.QVBoxLayout(self.MplWidget1)
        self.companovka_for_mpl1.setObjectName("companovka_for_mpl1")
        self.tabWidget.addTab(self.MplWidget1, "")
        self.MplWidget2 = QtWidgets.QWidget()
        self.MplWidget2.setMinimumSize(QtCore.QSize(1274, 688))
        self.MplWidget2.setObjectName("MplWidget2")
        self.companovka_for_mpl2 = QtWidgets.QVBoxLayout(self.MplWidget2)
        self.companovka_for_mpl2.setObjectName("companovka_for_mpl2")
        self.tabWidget.addTab(self.MplWidget2, "")
        self.MplWidget3 = QtWidgets.QWidget()
        self.MplWidget3.setMinimumSize(QtCore.QSize(1274, 688))
        self.MplWidget3.setObjectName("MplWidget3")
        self.companovka_for_mpl3 = QtWidgets.QVBoxLayout(self.MplWidget3)
        self.companovka_for_mpl3.setObjectName("companovka_for_mpl3")
        self.tabWidget.addTab(self.MplWidget3, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ напряжённо-деформированного состояния заклёпочного соединения"))
        self.label1.setText(_translate("MainWindow", "Материал:"))
        self.label2.setText(_translate("MainWindow", "Толщина (см) :"))
        self.label3.setText(_translate("MainWindow", "Сила (Н):"))
        self.label4.setText(_translate("MainWindow", "Угол (°):"))
        self.label5.setText(_translate("MainWindow", "Шаг сетки:"))
        self.materialsButton.setText(_translate("MainWindow", "Редактировать материалы"))
        self.execButton.setText(_translate("MainWindow", "Построить графики"))
        self.ansysButton.setText(_translate("MainWindow", "Загрузить сетку из Ansys"))
        self.ansysCheck.setText(_translate("MainWindow", "Использовать сетку из Ansys"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MplWidget1), _translate("MainWindow", "Модель"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MplWidget2), _translate("MainWindow", "Напряжения и деформации"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MplWidget3), _translate("MainWindow", "Эквивалентное напряжение и деформация"))
