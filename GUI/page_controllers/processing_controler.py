import os
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QFileDialog, QWidget
# from main import main

class ProcessingController(QObject):
    
    """
    controller for processing page
    """
    
    requestFileSearch = Signal()
    file_selected = Signal(str)
    
    def __init__(self, fileNameLabel, planListController, selectPlanComboBox, startProcessingPushButton, parent = None):
        super().__init__(parent)
        
        self.excel_file_path = None
        self.fileNameLabel = fileNameLabel
        self.planListController = planListController
        self.selectPlanComboBox = selectPlanComboBox
        self.startProcessingPushButton = startProcessingPushButton
    
    def process_file_path(self, file_path : str):
            
        file_name = os.path.basename(file_path)
        self.excel_file_path = file_path
        self.fileNameLabel.setText(file_name)
        self.check_processingButton_valid()
    
    def file_search(self):
        """
        send a request to mainwindow to look up an excel file
        """
        # excel_file_path = QFileDialog.getOpenFileName(self, "Open excel file", "", "Excel file(*.xlsx)")
        self.requestFileSearch.emit()
        
            
    def setup_plan_comboBox(self):
        """
        set up self.selectPlanComboBox with available plans
        """
        #look up the names and ids of plans with self.planListController
        id_name_dict = self.planListController.get_plans_ids_names()
        
        for plan_id, plan_name in id_name_dict.items():
            self.selectPlanComboBox.addItem(f"{plan_name}", plan_id)
        
        self.selectPlanComboBox.setCurrentIndex(-1)
        
        # current_index = self.selectPlanComboBox.currentIndex()
        # print(self.selectPlanComboBox.itemData(current_index, Qt.UserRole))
        
    def check_processingButton_valid(self):
        
        valid = True
        
        if self.selectPlanComboBox.currentIndex() == -1:
            valid = False
        if not self.excel_file_path:
            valid = False
        
        self.startProcessingPushButton.setEnabled(valid)
        return valid
    
    def process(self):
        """
        starts the main function and process the distribution
        """
        # main() # it is beeing reworked