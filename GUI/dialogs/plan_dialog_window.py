from PySide6.QtWidgets import QDialog, QDialogButtonBox
from ui_py.PlanDialog import Ui_Dialog
from utils.fill_settings import fill_settings_list, fill_settings_table
from utils.json_to_python import json_to_python

class PlanDialogWindow(QDialog, Ui_Dialog):
    """
        Dialog window for adding and setting up a selected plan
    """
    def __init__(self, settings : list = []):
        super().__init__()
        self.setupUi(self) 
        
        if settings:
            self.settings = settings
            self.apply_settings()
        
        self.setFocus()
        
        # appointing function to add a sport in self.sportsTableWidget
        self.sportsAddPushButton.clicked.connect(self.insert_sports_row)
        self.semestrAddPushButton.clicked.connect(self.insert_semestrs_row)
        self.slotAddPushButton.clicked.connect(self.insert_slots_row)
        
        # validating data on every signal
        self.ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        self.check_valid()
        self.planNameLineEdit.textChanged.connect(self.check_valid)
        self.planMaxCapSpinbox.valueChanged.connect(self.check_valid)
        self.planMinCapSpinbox.valueChanged.connect(self.check_valid)
        self.sportsTableWidget.itemChanged.connect(self.check_valid) # need to add validation for empty values in table
        self.semestrsListWidget.itemChanged.connect(self.check_valid)
        self.slotsListWidget.itemChanged.connect(self.check_valid)
    
    def accept(self):
        if not self.ok_button.isEnabled():
            return
        return super().accept()
    
    def insert_sports_row(self):
        row_count = self.sportsTableWidget.rowCount()
        self.sportsTableWidget.insertRow(row_count)
        
    def insert_semestrs_row(self):
        row_count = self.semestrsListWidget.rowCount()
        self.semestrsListWidget.insertRow(row_count)
        
    def insert_slots_row(self):
        row_count = self.slotsListWidget.rowCount()
        self.slotsListWidget.insertRow(row_count)
        
    def check_valid(self):
        
        validate = True
        
        if not self.planNameLineEdit.text().strip():
            validate = False
        
        if self.planMaxCapSpinbox.value() <= 0:
            validate = False
            
        if self.planMinCapSpinbox.value() < 0:
            validate = False
        
        if self.sportsTableWidget.rowCount() <= 0:
            validate = False
        if self.semestrsListWidget.rowCount() <= 0:
            validate = False
        if self.slotsListWidget.rowCount() <= 0:
            validate = False
        
        self.ok_button.setEnabled(validate)
        return validate
    
    def apply_settings(self):
        """ 
        apply given settings on a dialog window while editing a plan
        """
        
        self.planNameLineEdit.setText(self.settings['plan_name'])
        self.planMaxCapSpinbox.setValue(self.settings['max_cap'])
        self.planMinCapSpinbox.setValue(self.settings['min_cap'])        
        
        # self.sportsTableWidget.insertRow(self.sportsTableWidget.rowCount())
        
        sports_dict = json_to_python(self.settings['sports_json'])
        fill_settings_table(sports_dict, self.sportsTableWidget)
        
        semestr_list = json_to_python(self.settings['semestrs_json'])
        fill_settings_list(semestr_list, self.semestrsListWidget)
        
        slots_list = json_to_python(self.settings['slots_json'])
        fill_settings_list(slots_list, self.slotsListWidget)