import sys
from time import sleep

from PyQt5 import QtCore, QtWidgets

#Cambia el nombre de Video2_base_SQL por el de tu archivo convertido
from asnew2 import Ui_MainWindow
from PyQt5 import QtSql

import sqlite3
from pprint import pprint
                                    

class MainWindow_EXEC():
   
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)   
        #-------------------------- 
        self.create_DB()
        #Cambia el button_SQL_view_data por el nombre que le pongas al boton de ver
        self.ui.b1.clicked.connect(self.print_data)
        self.model = None
        #Cambia el button_SQL_view_data por el nombre que le pongas al boton de ver
        self.ui.b1.clicked.connect(self.sql_tableview_model)
        #Cambia el button_SQL_add por el nombre que le pongas al boton de agregar
        self.ui.b2.clicked.connect(self.sql_add_row)
        #Cambia el button_SQL_delete por el nombre que le pongas al boton de eliminar
        self.ui.b3.clicked.connect(self.sql_delete_row)
        
        
        #-------------------------- 
        
        self.MainWindow.show()
        sys.exit(app.exec_()) 
        
    #----------------------------------------------------------
    def sql_delete_row(self):
        if self.model:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
        else:
            self.sql_tableview_model()       
                
    #----------------------------------------------------------
    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.sql_tableview_model()

    #----------------------------------------------------------
    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        #Cambias este nombre
        db.setDatabaseName('dbasnew2.db')
        
        tableview = self.ui.tableView
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        
        self.model.setTable('asnew2')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "asset_id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "creator_id")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "event_id")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "format_type_code")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "date_creation")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "asset_title")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "location")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "description")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "playing_title")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "other_detalis")
        

    #----------------------------------------------------------
    def print_data(self):
        sqlite_file = 'dbasnew2.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'asnew2' ORDER BY asset_id ")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       # not needed when only selecting data
        conn.close()        
        
    #----------------------------------------------------------
    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('dbasnew2.db')
        db.open()
        
        query = QtSql.QSqlQuery()
          
        query.exec_("create table asnew2(asset_id int primary key, "
                    "creator_id int, event_id int,"
                    "format_type_code int, date_creation varchar(20),"
                    "asset_title varchar(20) , location varchar(20),"
                    "description varchar(20) , playing_title varchar(20),"
                    "other_detalis varchar(20))")
        
        #query.exec_("insert into contacts values(1, 'Leonel', 'Messi','messi@joto.com','4181167906')")
        #query.exec_("insert into contacts values(1, 'jorge', 'ponce','ponce@joto.com','4181167906')")
        
if __name__ == "__main__":
    MainWindow_EXEC()














