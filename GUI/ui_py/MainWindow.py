# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 627)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.action1_page = QAction(MainWindow)
        self.action1_page.setObjectName(u"action1_page")
        self.action2_page = QAction(MainWindow)
        self.action2_page.setObjectName(u"action2_page")
        self.actionhome_page = QAction(MainWindow)
        self.actionhome_page.setObjectName(u"actionhome_page")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.actionhome_page.setIcon(icon)
        self.actionhome_page.setMenuRole(QAction.MenuRole.NoRole)
        self.actionadd_plan = QAction(MainWindow)
        self.actionadd_plan.setObjectName(u"actionadd_plan")
        icon1 = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.ListAdd):
            icon1 = QIcon.fromTheme(QIcon.ThemeIcon.ListAdd)
        else:
            icon1.addFile(u"../recources/images/icons/blue-document--plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionadd_plan.setIcon(icon1)
        self.actionadd_plan.setMenuRole(QAction.MenuRole.NoRole)
        self.actiondelete_plan = QAction(MainWindow)
        self.actiondelete_plan.setObjectName(u"actiondelete_plan")
        icon2 = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.ListRemove):
            icon2 = QIcon.fromTheme(QIcon.ThemeIcon.ListRemove)
        else:
            icon2.addFile(u"../recources/images/icons/blue-document--minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actiondelete_plan.setIcon(icon2)
        self.actiondelete_plan.setMenuRole(QAction.MenuRole.NoRole)
        self.actionedit_plan = QAction(MainWindow)
        self.actionedit_plan.setObjectName(u"actionedit_plan")
        icon3 = QIcon()
        icon3.addFile(u"../recources/images/icons/blue-document--pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionedit_plan.setIcon(icon3)
        self.actionedit_plan.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.mainStackedWidget = QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.navigationPage = QWidget()
        self.navigationPage.setObjectName(u"navigationPage")
        self.horizontalLayout_3 = QHBoxLayout(self.navigationPage)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.navigationPage)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QWidget(self.widget)
        self.leftPanel.setObjectName(u"leftPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy1)
        self.leftPanel.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.leftPanel)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logoContainer = QWidget(self.leftPanel)
        self.logoContainer.setObjectName(u"logoContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logoContainer.sizePolicy().hasHeightForWidth())
        self.logoContainer.setSizePolicy(sizePolicy2)
        self.logoContainer.setMaximumSize(QSize(16777215, 120))
        self.logoContainer.setBaseSize(QSize(0, 64))
        self.horizontalLayout_4 = QHBoxLayout(self.logoContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logoLabel = QLabel(self.logoContainer)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setPixmap(QPixmap(u"../recources/images/FairEinwahlLogo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.logoLabel)


        self.verticalLayout.addWidget(self.logoContainer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.navigationListWidget = QListWidget(self.leftPanel)
        self.navigationListWidget.setObjectName(u"navigationListWidget")

        self.horizontalLayout_5.addWidget(self.navigationListWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_2.addWidget(self.leftPanel)

        self.infoStackedWidget = QStackedWidget(self.widget)
        self.infoStackedWidget.setObjectName(u"infoStackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.infoStackedWidget.sizePolicy().hasHeightForWidth())
        self.infoStackedWidget.setSizePolicy(sizePolicy3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.infoStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.infoStackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.infoStackedWidget)


        self.horizontalLayout_3.addWidget(self.widget)

        self.mainStackedWidget.addWidget(self.navigationPage)
        self.planListPage = QWidget()
        self.planListPage.setObjectName(u"planListPage")
        self.horizontalLayout_7 = QHBoxLayout(self.planListPage)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.planLeftPanel = QWidget(self.planListPage)
        self.planLeftPanel.setObjectName(u"planLeftPanel")
        sizePolicy1.setHeightForWidth(self.planLeftPanel.sizePolicy().hasHeightForWidth())
        self.planLeftPanel.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.planLeftPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.planLeftPanel)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.planListView = QListView(self.planLeftPanel)
        self.planListView.setObjectName(u"planListView")

        self.horizontalLayout.addWidget(self.planListView)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_7.addWidget(self.planLeftPanel)

        self.verticalWidget = QWidget(self.planListPage)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy4)
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.verticalWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 106, 223))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.generalPlanInfo = QWidget(self.scrollAreaWidgetContents_2)
        self.generalPlanInfo.setObjectName(u"generalPlanInfo")
        self.verticalLayout_5 = QVBoxLayout(self.generalPlanInfo)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 5)
        self.label_3 = QLabel(self.generalPlanInfo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_3)

        self.infoPlanNameLabel = QLabel(self.generalPlanInfo)
        self.infoPlanNameLabel.setObjectName(u"infoPlanNameLabel")
        self.infoPlanNameLabel.setMaximumSize(QSize(16777215, 20))
        self.infoPlanNameLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.infoPlanNameLabel.setMargin(0)

        self.verticalLayout_5.addWidget(self.infoPlanNameLabel)


        self.verticalLayout_4.addWidget(self.generalPlanInfo)

        self.MinMaxCapacityInfo = QWidget(self.scrollAreaWidgetContents_2)
        self.MinMaxCapacityInfo.setObjectName(u"MinMaxCapacityInfo")
        self.verticalLayout_10 = QVBoxLayout(self.MinMaxCapacityInfo)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.MinMaxCapacityInfo)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_11)

        self.infoMinCapLabel = QLabel(self.MinMaxCapacityInfo)
        self.infoMinCapLabel.setObjectName(u"infoMinCapLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(7)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.infoMinCapLabel.sizePolicy().hasHeightForWidth())
        self.infoMinCapLabel.setSizePolicy(sizePolicy5)
        self.infoMinCapLabel.setMaximumSize(QSize(16777215, 20))
        self.infoMinCapLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.infoMinCapLabel.setMargin(0)

        self.horizontalLayout_13.addWidget(self.infoMinCapLabel)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.MinMaxCapacityInfo)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_13)

        self.infoMaxCapLabel = QLabel(self.MinMaxCapacityInfo)
        self.infoMaxCapLabel.setObjectName(u"infoMaxCapLabel")
        sizePolicy5.setHeightForWidth(self.infoMaxCapLabel.sizePolicy().hasHeightForWidth())
        self.infoMaxCapLabel.setSizePolicy(sizePolicy5)

        self.horizontalLayout_14.addWidget(self.infoMaxCapLabel)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)


        self.verticalLayout_4.addWidget(self.MinMaxCapacityInfo)

        self.sportTypesInfo = QWidget(self.scrollAreaWidgetContents_2)
        self.sportTypesInfo.setObjectName(u"sportTypesInfo")
        self.verticalLayout_6 = QVBoxLayout(self.sportTypesInfo)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.sportTypesInfo)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setMargin(0)

        self.verticalLayout_6.addWidget(self.label_4)

        self.horizontalWidget_3 = QWidget(self.sportTypesInfo)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(2)
        sizePolicy7.setHeightForWidth(self.horizontalWidget_3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_3.setSizePolicy(sizePolicy7)
        self.horizontalWidget_3.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.infoSportsTableWidget = QTableWidget(self.horizontalWidget_3)
        if (self.infoSportsTableWidget.columnCount() < 2):
            self.infoSportsTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.infoSportsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.infoSportsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.infoSportsTableWidget.setObjectName(u"infoSportsTableWidget")
        self.infoSportsTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)

        self.horizontalLayout_8.addWidget(self.infoSportsTableWidget)


        self.verticalLayout_6.addWidget(self.horizontalWidget_3)


        self.verticalLayout_4.addWidget(self.sportTypesInfo)

        self.SemestrsInfo = QWidget(self.scrollAreaWidgetContents_2)
        self.SemestrsInfo.setObjectName(u"SemestrsInfo")
        self.verticalLayout_7 = QVBoxLayout(self.SemestrsInfo)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.SemestrsInfo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setMargin(0)

        self.verticalLayout_7.addWidget(self.label_7)

        self.horizontalWidget_6 = QWidget(self.SemestrsInfo)
        self.horizontalWidget_6.setObjectName(u"horizontalWidget_6")
        self.horizontalWidget_6.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.infoSemestrsTableWidget = QTableWidget(self.horizontalWidget_6)
        if (self.infoSemestrsTableWidget.columnCount() < 1):
            self.infoSemestrsTableWidget.setColumnCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.infoSemestrsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        self.infoSemestrsTableWidget.setObjectName(u"infoSemestrsTableWidget")
        self.infoSemestrsTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)

        self.horizontalLayout_11.addWidget(self.infoSemestrsTableWidget)


        self.verticalLayout_7.addWidget(self.horizontalWidget_6)


        self.verticalLayout_4.addWidget(self.SemestrsInfo)

        self.SlotsInfo = QWidget(self.scrollAreaWidgetContents_2)
        self.SlotsInfo.setObjectName(u"SlotsInfo")
        self.verticalLayout_8 = QVBoxLayout(self.SlotsInfo)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.SlotsInfo)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setMargin(0)

        self.verticalLayout_8.addWidget(self.label_8)

        self.horizontalWidget_7 = QWidget(self.SlotsInfo)
        self.horizontalWidget_7.setObjectName(u"horizontalWidget_7")
        self.horizontalWidget_7.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalWidget_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.infoSlotsTableWidget = QTableWidget(self.horizontalWidget_7)
        if (self.infoSlotsTableWidget.columnCount() < 1):
            self.infoSlotsTableWidget.setColumnCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.infoSlotsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        self.infoSlotsTableWidget.setObjectName(u"infoSlotsTableWidget")
        self.infoSlotsTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)

        self.horizontalLayout_12.addWidget(self.infoSlotsTableWidget)


        self.verticalLayout_8.addWidget(self.horizontalWidget_7)


        self.verticalLayout_4.addWidget(self.SlotsInfo)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout_7.addWidget(self.verticalWidget)

        self.mainStackedWidget.addWidget(self.planListPage)
        self.processingPage = QWidget()
        self.processingPage.setObjectName(u"processingPage")
        self.label_2 = QLabel(self.processingPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 0, 81, 41))
        self.groupBox = QGroupBox(self.processingPage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(180, 40, 461, 241))
        self.verticalLayout_12 = QVBoxLayout(self.groupBox)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.selectPlanComboBox = QComboBox(self.groupBox)
        self.selectPlanComboBox.setObjectName(u"selectPlanComboBox")
        sizePolicy2.setHeightForWidth(self.selectPlanComboBox.sizePolicy().hasHeightForWidth())
        self.selectPlanComboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.selectPlanComboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy8)

        self.verticalLayout_11.addWidget(self.label_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.fileNameLabel = QLabel(self.groupBox)
        self.fileNameLabel.setObjectName(u"fileNameLabel")

        self.horizontalLayout_9.addWidget(self.fileNameLabel)

        self.fileSearchPushButton = QPushButton(self.groupBox)
        self.fileSearchPushButton.setObjectName(u"fileSearchPushButton")

        self.horizontalLayout_9.addWidget(self.fileSearchPushButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.horizontalLayoutWidget = QWidget(self.processingPage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(190, 290, 411, 101))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.startProcessingPushButton = QPushButton(self.horizontalLayoutWidget)
        self.startProcessingPushButton.setObjectName(u"startProcessingPushButton")
        self.startProcessingPushButton.setEnabled(False)

        self.horizontalLayout_15.addWidget(self.startProcessingPushButton)

        self.mainStackedWidget.addWidget(self.processingPage)

        self.horizontalLayout_6.addWidget(self.mainStackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 22))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuEinstellungen = QMenu(self.menubar)
        self.menuEinstellungen.setObjectName(u"menuEinstellungen")
        self.menuHilfe = QMenu(self.menubar)
        self.menuHilfe.setObjectName(u"menuHilfe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuEinstellungen.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())
        self.menuHilfe.addAction(self.action1_page)
        self.menuHilfe.addAction(self.action2_page)
        self.toolBar.addAction(self.actionhome_page)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionadd_plan)
        self.toolBar.addAction(self.actiondelete_plan)
        self.toolBar.addAction(self.actionedit_plan)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.mainStackedWidget.setCurrentIndex(2)
        self.infoStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fair Einwahl", None))
        self.action1_page.setText(QCoreApplication.translate("MainWindow", u"1 page", None))
        self.action2_page.setText(QCoreApplication.translate("MainWindow", u"2 page", None))
        self.actionhome_page.setText(QCoreApplication.translate("MainWindow", u"home page", None))
#if QT_CONFIG(tooltip)
        self.actionhome_page.setToolTip(QCoreApplication.translate("MainWindow", u"go to home page", None))
#endif // QT_CONFIG(tooltip)
        self.actionadd_plan.setText(QCoreApplication.translate("MainWindow", u"add plan", None))
#if QT_CONFIG(tooltip)
        self.actionadd_plan.setToolTip(QCoreApplication.translate("MainWindow", u"add plan", None))
#endif // QT_CONFIG(tooltip)
        self.actiondelete_plan.setText(QCoreApplication.translate("MainWindow", u"delete plan", None))
#if QT_CONFIG(tooltip)
        self.actiondelete_plan.setToolTip(QCoreApplication.translate("MainWindow", u"delete selected plan", None))
#endif // QT_CONFIG(tooltip)
        self.actionedit_plan.setText(QCoreApplication.translate("MainWindow", u"edit plan", None))
#if QT_CONFIG(tooltip)
        self.actionedit_plan.setToolTip(QCoreApplication.translate("MainWindow", u"edit selected plan", None))
#endif // QT_CONFIG(tooltip)
        self.logoLabel.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pl\u00e4ne", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Plan Name", None))
        self.infoPlanNameLabel.setText(QCoreApplication.translate("MainWindow", u"Plan Name Example", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Min Capacity:", None))
        self.infoMinCapLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Max Capacity:", None))
        self.infoMaxCapLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sportarten", None))
        ___qtablewidgetitem = self.infoSportsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Sport Index", None));
        ___qtablewidgetitem1 = self.infoSportsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Sport Name", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Semestrs", None))
        ___qtablewidgetitem2 = self.infoSemestrsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Semestr", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Slots", None))
        ___qtablewidgetitem3 = self.infoSlotsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Slot", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Verarbeitung", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Auswahl", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Activer Plan:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Excel Datei:", None))
        self.fileNameLabel.setText(QCoreApplication.translate("MainWindow", u"Excel Datei", None))
        self.fileSearchPushButton.setText(QCoreApplication.translate("MainWindow", u"Durchsuchen", None))
        self.startProcessingPushButton.setText(QCoreApplication.translate("MainWindow", u"Verarbeitung starten", None))
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
        self.menuEinstellungen.setTitle(QCoreApplication.translate("MainWindow", u"Einstellungen", None))
        self.menuHilfe.setTitle(QCoreApplication.translate("MainWindow", u"Hilfe", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

