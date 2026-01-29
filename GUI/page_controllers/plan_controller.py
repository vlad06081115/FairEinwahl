from PySide6.QtWidgets import QListView
from PySide6.QtCore import QObject

from utils.fill_settings import fill_settings_list, fill_settings_table

class PlanController(QObject):
    
    def __init__(self, planListView : QListView, planListController, infoSportsTableWidget, infoSemestrsTableWidget, infoSlotsTableWidget, infoPlanNameLabel, infoMaxCapLabel, infoMinCapLabel, parent = None):
        super().__init__(parent)
        
        self.planListView = planListView
        self.planListController = planListController
        self.infoSportsTableWidget = infoSportsTableWidget
        self.infoSemestrsTableWidget = infoSemestrsTableWidget
        self.infoSlotsTableWidget = infoSlotsTableWidget
        self.infoPlanNameLabel = infoPlanNameLabel
        self.infoMaxCapLabel = infoMaxCapLabel
        self.infoMinCapLabel = infoMinCapLabel
        
    def plan_info_fill(self):
        """
        fill the plan info from current planListView selection
        """
        
        current_selection = self.planListView.currentIndex()
        plan_info_dict = self.planListController.get_plan_info(current_selection)
        
        self.infoSportsTableWidget.setRowCount(0)
        self.infoSemestrsTableWidget.setRowCount(0)
        self.infoSlotsTableWidget.setRowCount(0)
        
        self.infoPlanNameLabel.setText(plan_info_dict['plan_name'])
        self.infoMaxCapLabel.setText(str(plan_info_dict['max_cap']))
        self.infoMinCapLabel.setText(str(plan_info_dict['min_cap']))
        fill_settings_table(plan_info_dict['sports'], self.infoSportsTableWidget)
        fill_settings_list(plan_info_dict['semestrs'], self.infoSemestrsTableWidget)
        fill_settings_list(plan_info_dict['slots'], self.infoSlotsTableWidget)