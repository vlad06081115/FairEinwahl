from PySide6.QtSql import QSqlTableModel

class PlanListModel(QSqlTableModel):
    
    def __init__(self, db, parent = None):
        super().__init__(parent, db)
        self.setTable('plans')
        self.select()
        
class PlanConfigModel(QSqlTableModel):
    
    def __init__(self, db, parent = None):
        super().__init__(parent, db)
        self.setTable('plan_config')
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.select()