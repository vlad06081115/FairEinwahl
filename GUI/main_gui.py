import sys
import os
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QFileDialog
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt

from recources import recources
from ui_py.MainWindow import Ui_MainWindow

#page controllers import
from page_controllers.plan_controller import PlanController
from page_controllers.processing_controler import ProcessingController

#controllers import
from controllers.plan_list_controller import PlanListController

#models import
from models.models import PlanConfigModel, PlanListModel



def app_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

DB_NAME = os.path.join(app_dir(), r'app_data/fair_einwahl.db')

def connect_to_db():
    if QSqlDatabase.contains("main_connection"):
        return QSqlDatabase().database("main_connection")
    
    db = QSqlDatabase().addDatabase('QSQLITE', 'main_connection')
    db.setDatabaseName(DB_NAME)
    
    if not db.open():
        raise RuntimeError("Cannot open database")
    
    query = QSqlQuery(db)
    query.exec("PRAGMA foreign_keys = ON;")
    
    return db


class MainWindow(QMainWindow, Ui_MainWindow):
    
    NAVIGATION_LIST_WIDGET_BUTTONS = {
        "Pläne" : 1,
        "Verarbeitung" : 2,
        "Ergebnisse" : 3
    }
    
    HOMEPAGE_INDEX = 0
    
    def __init__(self, db):
        super().__init__()
        self.setupUi(self)
        
        #setting the logo to self.logoLabel
        pix = QPixmap(":/icons/images/FairEinwahlLogomini.png")
        self.logoLabel.setPixmap(pix)
        
        #setting up toolbar
        self.actionhome_page.triggered.connect(self.switch_to_homepage)
        
        self.actionadd_plan.setIcon(QIcon(":/icons/images/icons/blue-document--plus.png"))
        self.actiondelete_plan.setIcon(QIcon(":/icons/images/icons/blue-document--minus.png"))
        self.actionedit_plan.setIcon(QIcon(":/icons/images/icons/blue-document--pencil.png"))
        
        self.toolBarPageSections = {
            self.NAVIGATION_LIST_WIDGET_BUTTONS['Pläne'] : [self.actionadd_plan, self. actiondelete_plan, self.actionedit_plan],
            self.NAVIGATION_LIST_WIDGET_BUTTONS['Verarbeitung'] : [],
            self.NAVIGATION_LIST_WIDGET_BUTTONS['Ergebnisse'] : []
        }
        
        #setting the default page
        self.mainStackedWidget.setCurrentIndex(self.HOMEPAGE_INDEX)
        self.toggle_toolbar_actions(self.HOMEPAGE_INDEX)
        
        # setting up the self.navigationalListWidget
        for plan_name, page_index in self.NAVIGATION_LIST_WIDGET_BUTTONS.items():
            item = QListWidgetItem(plan_name)
            item.setData(Qt.UserRole, page_index)
            self.navigationListWidget.addItem(item)
            
        self.navigationListWidget.itemSelectionChanged.connect(self.navi_listwidget_triggered)
        
        #creating a model for writing data into plan_config database
        self.planConfigModel = PlanConfigModel(db)
        
        #setting up the model for self.planListWidget
        self.planListModel = PlanListModel(db)
        self.planListController = PlanListController(self.planListModel, self.planConfigModel)
        self.planListView.setModel(self.planListModel)
        self.planListView.setModelColumn(1)
        
        # connectig and setting up controllers

        self.plan_controller = PlanController(
            planListView= self.planListView,
            planListController = self.planListController,
            infoSportsTableWidget= self.infoSportsTableWidget,
            infoSemestrsTableWidget= self.infoSemestrsTableWidget,
            infoSlotsTableWidget= self.infoSlotsTableWidget,
            infoPlanNameLabel= self.infoPlanNameLabel,
            infoMaxCapLabel= self.infoMaxCapLabel,
            infoMinCapLabel= self.infoMinCapLabel
        )
        
        #planListView trigerred change planInfo
        self.planListView.clicked.connect(self.plan_controller.plan_info_fill)
        
        #toolbar actions for plan section
        self.actionadd_plan.triggered.connect(self.action_addplan_triggered)
        self.actiondelete_plan.triggered.connect(self.action_deleteplan_triggered)
        self.actionedit_plan.triggered.connect(self.action_editplan_triggered)
        self.planListView.clicked.connect(self.check_planTool_valid)
        
        #setting up processing page (Verarbeitung) / adding self.excel_file_path
        
        self.processing_controler = ProcessingController(
            fileNameLabel= self.fileNameLabel,
            planListController= self.planListController,
            selectPlanComboBox= self.selectPlanComboBox,
            startProcessingPushButton= self.startProcessingPushButton
        )
        
        self.processing_controler.requestFileSearch.connect(self.file_search_open)
        self.processing_controler.file_selected.connect(self.processing_controler.process_file_path)
        
        self.fileSearchPushButton.clicked.connect(self.processing_controler.file_search)
        self.processing_controler.setup_plan_comboBox()
        
        self.selectPlanComboBox.currentIndexChanged.connect(self.processing_controler.check_processingButton_valid)
        
        self.startProcessingPushButton.clicked.connect(self.processing_controler.process)
    
    def file_search_open(self):
        
        excel_file_path, _ = QFileDialog.getOpenFileName(self, "Open excel file", "", "Excel file(*.xlsx)")

        if excel_file_path:
            self.processing_controler.file_selected.emit(excel_file_path)
        
        return True
    
    def switch_to_homepage(self):
        self.mainStackedWidget.setCurrentIndex(self.HOMEPAGE_INDEX)
        self.navigationListWidget.clearSelection()
        
        self.toggle_toolbar_actions(self.HOMEPAGE_INDEX)
        
    def navi_listwidget_triggered(self):
        
        item = self.navigationListWidget.currentItem()
        
        if not item:
            return
        
        selected_index = item.data(Qt.UserRole)
        self.mainStackedWidget.setCurrentIndex(selected_index)
        
        self.toggle_toolbar_actions(selected_index)
    
    def toggle_toolbar_actions(self, current_page_index : int = 0):
        
        for page_index, action_list in self.toolBarPageSections.items():
            
            if page_index == current_page_index:
                for action in action_list:
                    action.setEnabled(True)    
            else:
                for action in action_list:
                    action.setDisabled(True)
        
        self.page_changed()
                    
    def action_addplan_triggered(self):
        self.planListController.add_plan()
        
    def action_deleteplan_triggered(self):
        plan_index = self.planListView.currentIndex()
        plan_id = plan_index.siblingAtColumn(0).data()
        self.planListController.delete_plan(plan_id)
        self.check_planTool_valid()
        
    def action_editplan_triggered(self):
        plan_index = self.planListView.currentIndex()
        plan_id = plan_index.siblingAtColumn(0).data()
        self.planListController.edit_plan(plan_id)
    
    def page_changed(self):
        
        for page_index, action_list in self.toolBarPageSections.items():
            if page_index == 1:
                self.actiondelete_plan.setEnabled(False)
                self.actionedit_plan.setEnabled(False)
            elif page_index == 2:
                # add something as soon as i add this page
                pass
            elif page_index == 3:
                # add something as soon as i add this page
                pass
    
    def check_planTool_valid(self):
        validate = True
        
        if not self.planListView.selectedIndexes():
            validate = False
            
        self.actiondelete_plan.setEnabled(validate)
        self.actionedit_plan.setEnabled(validate)
        
        return validate
        
#creating an app        
app = QApplication()

db = connect_to_db()

window = MainWindow(db)
window.show()
app.exec()