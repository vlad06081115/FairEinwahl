import json
from dialogs.plan_dialog_window import PlanDialogWindow
from models.models import PlanConfigModel, PlanListModel
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QTableWidget
from utils.json_to_python import json_to_python

class PlanListController(QObject):
    
    SPORTS_TABLE_WIDGET_COLCOUNT = 2
    SEMESTRS_TABLE_WIDGET_COLCOUNT = 1
    SLOTS_TABLE_WIDGET_COLCOUNT = 1
    
    def __init__(self, planListModel : PlanListModel, planConfigModel : PlanConfigModel):
        super().__init__()
        self._planListModel = planListModel
        self._planConfigModel = planConfigModel
    
    def get_data_from_dlg(self, dlg : PlanDialogWindow):
        
        plan_name = dlg.planNameLineEdit.text()
        max_capacity = dlg.planMaxCapSpinbox.value()
        min_capacity = dlg.planMinCapSpinbox.value()
        sports_dict_json = self.to_json(self.get_sports_dict(dlg))
        semestrs_list_json = self.to_json(self.get_data_list(dlg, dlg.semestrsListWidget))
        slots_list_json = self.to_json(self.get_data_list(dlg, dlg.slotsListWidget))
        
        dlg_data_dict = {
            'plan_name' : plan_name,
            'max_capacity' : max_capacity,
            'min_capacity' : min_capacity,
            'sports_dict_json' : sports_dict_json,
            'semestrs_list_json' : semestrs_list_json,
            'slots_list_json' : slots_list_json
        }
        
        return dlg_data_dict
    
    def add_plan(self):
    
        dlg = PlanDialogWindow()
        result = dlg.exec() 
        
        if result:
            #gathering data
            data_dict = self.get_data_from_dlg(dlg)
            
            #adding data to a database
            row = self._planListModel.rowCount()
            self._planListModel.insertRow(row)
            self._planListModel.setData(self._planListModel.index(row, 1), data_dict['plan_name'])
            self._planListModel.submitAll()
            plan_id = self._planListModel.index(row, 0).data()
            
            row = self._planConfigModel.rowCount()
            self._planConfigModel.insertRow(row)
            self._planConfigModel.setData(self._planConfigModel.index(row, 1), plan_id)
            self._planConfigModel.setData(self._planConfigModel.index(row, 2), data_dict['max_capacity'])
            self._planConfigModel.setData(self._planConfigModel.index(row, 3), data_dict['min_capacity'])
            self._planConfigModel.setData(self._planConfigModel.index(row, 4), data_dict['sports_dict_json'])
            self._planConfigModel.setData(self._planConfigModel.index(row, 5), data_dict['semestrs_list_json'])
            self._planConfigModel.setData(self._planConfigModel.index(row, 6), data_dict['slots_list_json'])
            self._planConfigModel.submitAll()

    def get_sports_dict(self, dlg : PlanDialogWindow):
        
        row_count = dlg.sportsTableWidget.rowCount()
        
        data_dict = {}
        for row in range(row_count):
            row_data = []
            for col in range(self.SPORTS_TABLE_WIDGET_COLCOUNT):
                item = dlg.sportsTableWidget.item(row, col).data(0)
                row_data.append(item)
            data_dict[row_data[0]] = row_data[1]

        return data_dict
    
    def get_data_list(self, dlg : PlanDialogWindow, widget : QTableWidget):
        
        row_count = widget.rowCount()
        
        data_list = []
        for row in range(row_count):
            for col in range(self.SEMESTRS_TABLE_WIDGET_COLCOUNT):
                item = widget.item(row, col).data(0)
                data_list.append(item)
                
        return data_list
    
    def to_json(self, data):
        return json.dumps(data, ensure_ascii= False)

    def delete_plan(self, plan_id):
        for row in range(self._planListModel.rowCount()):
            if self._planListModel.index(row, 0).data() == plan_id:
                self._planListModel.removeRow(row)
                self._planListModel.submitAll()
                self._planListModel.select()
                return

    def edit_plan(self, plan_id):
        
        settings = {}
        for row in range(self._planConfigModel.rowCount()):
            if self._planConfigModel.index(row, 1).data() == plan_id:
                settings["max_cap"] = self._planConfigModel.index(row, 2).data()
                settings["min_cap"] = self._planConfigModel.index(row, 3).data()
                settings["sports_json"] = self._planConfigModel.index(row, 4).data()
                settings["semestrs_json"] = self._planConfigModel.index(row, 5).data()
                settings["slots_json"] = self._planConfigModel.index(row, 6).data()  
                planConfigModelRow = row   
                break
            
        for row in range(self._planListModel.rowCount()):
            if self._planListModel.index(row, 0).data() == plan_id:
                settings["plan_name"] = self._planListModel.index(row, 1).data() 
                planListModelRow = row 
        
        dlg = PlanDialogWindow(settings= settings)
        result = dlg.exec()
        
        if result:
            
            data_dict = self.get_data_from_dlg(dlg)
            
            self._planConfigModel.setData(self._planConfigModel.index(planConfigModelRow, 2), data_dict['max_capacity'])
            self._planConfigModel.setData(self._planConfigModel.index(planConfigModelRow, 3), data_dict['min_capacity'])
            self._planConfigModel.setData(self._planConfigModel.index(planConfigModelRow, 4), data_dict['sports_dict_json'])
            self._planConfigModel.setData(self._planConfigModel.index(planConfigModelRow, 5), data_dict['semestrs_list_json'])
            self._planConfigModel.setData(self._planConfigModel.index(planConfigModelRow, 6), data_dict['slots_list_json'])
            self._planConfigModel.submitAll()
            
            self._planListModel.setData(self._planListModel.index(planListModelRow, 1), data_dict['plan_name'])
            self._planListModel.submitAll()
            
    def get_plan_info(self, current_selection_index):
        
        row = current_selection_index.row()
        plan_id = self._planListModel.index(row, 0).data()
        
        plan_info_dict = {}

        plan_info_dict['plan_name'] = self._planListModel.index(row, 1).data()
        
        for row in range(self._planConfigModel.rowCount()):
            if self._planConfigModel.index(row, 1).data() == plan_id:
                plan_info_dict["max_cap"] = self._planConfigModel.index(row, 2).data()
                plan_info_dict["min_cap"] = self._planConfigModel.index(row, 3).data()
                plan_info_dict["sports"] = json_to_python(self._planConfigModel.index(row, 4).data())
                plan_info_dict["semestrs"] = json_to_python(self._planConfigModel.index(row, 5).data())
                plan_info_dict["slots"] = json_to_python(self._planConfigModel.index(row, 6).data())  
                
                break
        
        return plan_info_dict

    def get_plans_ids_names(self) -> dict:
        """
        get all the names and ids from self._planListModel
        """
        
        id_name_dict = {}
        for row in range(self._planListModel.rowCount()):
            plan_id = self._planListModel.index(row, 0).data()
            plan_name = self._planListModel.index(row, 1).data()

            id_name_dict[plan_id] = plan_name
        
        return id_name_dict  