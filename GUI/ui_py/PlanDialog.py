# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PlanDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(641, 520)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.planNameLabel = QLabel(Dialog)
        self.planNameLabel.setObjectName(u"planNameLabel")

        self.horizontalLayout_6.addWidget(self.planNameLabel)

        self.planNameLineEdit = QLineEdit(Dialog)
        self.planNameLineEdit.setObjectName(u"planNameLineEdit")

        self.horizontalLayout_6.addWidget(self.planNameLineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.planMaxCapLabel = QLabel(Dialog)
        self.planMaxCapLabel.setObjectName(u"planMaxCapLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planMaxCapLabel.sizePolicy().hasHeightForWidth())
        self.planMaxCapLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.planMaxCapLabel)

        self.planMaxCapSpinbox = QSpinBox(Dialog)
        self.planMaxCapSpinbox.setObjectName(u"planMaxCapSpinbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.planMaxCapSpinbox.sizePolicy().hasHeightForWidth())
        self.planMaxCapSpinbox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.planMaxCapSpinbox)

        self.horizontalSpacer_2 = QSpacerItem(400, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.planMinCapLabel = QLabel(Dialog)
        self.planMinCapLabel.setObjectName(u"planMinCapLabel")
        sizePolicy.setHeightForWidth(self.planMinCapLabel.sizePolicy().hasHeightForWidth())
        self.planMinCapLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.planMinCapLabel)

        self.planMinCapSpinbox = QSpinBox(Dialog)
        self.planMinCapSpinbox.setObjectName(u"planMinCapSpinbox")
        sizePolicy1.setHeightForWidth(self.planMinCapSpinbox.sizePolicy().hasHeightForWidth())
        self.planMinCapSpinbox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.planMinCapSpinbox)

        self.horizontalSpacer = QSpacerItem(400, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.planSportsLabel = QLabel(Dialog)
        self.planSportsLabel.setObjectName(u"planSportsLabel")

        self.horizontalLayout_3.addWidget(self.planSportsLabel)

        self.sportsTableWidget = QTableWidget(Dialog)
        if (self.sportsTableWidget.columnCount() < 2):
            self.sportsTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.sportsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.sportsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.sportsTableWidget.setObjectName(u"sportsTableWidget")
        self.sportsTableWidget.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.sportsTableWidget)

        self.sportsAddPushButton = QPushButton(Dialog)
        self.sportsAddPushButton.setObjectName(u"sportsAddPushButton")

        self.horizontalLayout_3.addWidget(self.sportsAddPushButton)

        self.horizontalSpacer_4 = QSpacerItem(300, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.planSemestrsLabel = QLabel(Dialog)
        self.planSemestrsLabel.setObjectName(u"planSemestrsLabel")

        self.horizontalLayout_7.addWidget(self.planSemestrsLabel)

        self.semestrsListWidget = QTableWidget(Dialog)
        if (self.semestrsListWidget.columnCount() < 1):
            self.semestrsListWidget.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.semestrsListWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.semestrsListWidget.setObjectName(u"semestrsListWidget")

        self.horizontalLayout_7.addWidget(self.semestrsListWidget)

        self.semestrAddPushButton = QPushButton(Dialog)
        self.semestrAddPushButton.setObjectName(u"semestrAddPushButton")

        self.horizontalLayout_7.addWidget(self.semestrAddPushButton)

        self.horizontalSpacer_5 = QSpacerItem(500, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.planSlotsLabel = QLabel(Dialog)
        self.planSlotsLabel.setObjectName(u"planSlotsLabel")

        self.horizontalLayout_8.addWidget(self.planSlotsLabel)

        self.slotsListWidget = QTableWidget(Dialog)
        if (self.slotsListWidget.columnCount() < 1):
            self.slotsListWidget.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.slotsListWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        self.slotsListWidget.setObjectName(u"slotsListWidget")

        self.horizontalLayout_8.addWidget(self.slotsListWidget)

        self.slotAddPushButton = QPushButton(Dialog)
        self.slotAddPushButton.setObjectName(u"slotAddPushButton")

        self.horizontalLayout_8.addWidget(self.slotAddPushButton)

        self.horizontalSpacer_6 = QSpacerItem(500, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.planNameLabel.setText(QCoreApplication.translate("Dialog", u"Namel", None))
        self.planMaxCapLabel.setText(QCoreApplication.translate("Dialog", u"max capacityl", None))
        self.planMinCapLabel.setText(QCoreApplication.translate("Dialog", u"min capacity", None))
        self.planSportsLabel.setText(QCoreApplication.translate("Dialog", u"Sports", None))
        ___qtablewidgetitem = self.sportsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Sport Index", None));
        ___qtablewidgetitem1 = self.sportsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Sport Name", None));
        self.sportsAddPushButton.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.planSemestrsLabel.setText(QCoreApplication.translate("Dialog", u"Semestrs", None))
        ___qtablewidgetitem2 = self.semestrsListWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Semestrs name", None));
        self.semestrAddPushButton.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.planSlotsLabel.setText(QCoreApplication.translate("Dialog", u"Slots", None))
        ___qtablewidgetitem3 = self.slotsListWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Slot", None));
        self.slotAddPushButton.setText(QCoreApplication.translate("Dialog", u"+", None))
    # retranslateUi

