from PySide6.QtWidgets import QTableWidgetItem

def fill_settings_table(data_dict : dict, table):
    """
        Feels the table in dialog window with data given
    """
    for key, value in data_dict.items():
        row = table.rowCount()
        table.insertRow(row)
            
        key_item = QTableWidgetItem(str(key))
        value_item = QTableWidgetItem(str(value))
            
        table.setItem(row, 0, key_item)
        table.setItem(row, 1, value_item)
            
def fill_settings_list(data_list: list, list_object):
    """
        Feels a list in dialog window with data given
    """

    for line in data_list:
            
        row = list_object.rowCount()
        list_object.insertRow(row)
            
        line_item = QTableWidgetItem(str(line))
            
        list_object.setItem(row, 0, line_item)