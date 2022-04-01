import signal
import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainForm import *
from plants import *
from members import *
from products import *
from data import *
from newProduct import *
from newPlant import *
from newMember import *
from newData import *
from signin import *
import os

class Signin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.signin.clicked.connect(self.openDialog)  # Открыть новую форму

    def openDialog(self):
        self.close()
        dialog = MainForm(self)
        dialog.exec_()





class MainForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = Ui_FormMain()
        self.ui.setupUi(self)
        self.ui.Plants.clicked.connect(self.openPlants)
        self.ui.Members.clicked.connect(self.openMembers)
        self.ui.Actual_data.clicked.connect(self.openData)
        self.ui.Products.clicked.connect(self.openProducts)

    def openPlants(self):
        dialog = Plants(self)
        dialog.exec_()

    def openMembers(self):
        dialog = Members(self)
        dialog.exec_()

    def openProducts(self):
        dialog = Products(self)
        dialog.exec_()

    def openData(self):
        dialog = Data(self)
        dialog.exec_()


class Plants(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Plants, self).__init__(parent)
        self.ui = Ui_FormPlants()
        self.ui.setupUi(self)
        self.loaddate()
        self.ui.add.clicked.connect(self.add)
        self.ui.dell.clicked.connect(self.delete)

    def delete(self):
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        id = self.ui.id.text()
        cur.execute(f"delete from plants where PK_PlantID={id}")
        con.commit()

    def add(self):
        dialog = NewPlant(self)
        dialog.exec_()

    def loaddate(self):
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        sqlquary = "select * from plants"
        self.ui.tableWidget.setRowCount(50)
        tableIndex = 0
        for row in cur.execute(sqlquary):
            self.ui.tableWidget.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(tableIndex, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(tableIndex, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget.setItem(tableIndex, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget.setItem(tableIndex, 7, QtWidgets.QTableWidgetItem(row[7]))
            tableIndex += 1

class NewPlant(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(NewPlant, self).__init__(parent)
        self.ui = Ui_FormNewPlant()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.insert)


    def insert(self):
        IndexPlant = self.ui.IndexPlant.text()
        NamePlant = self.ui.NamePlant.text()
        Region = self.ui.Region.text()
        City = self.ui.City.text()
        Street = self.ui.Street.text()
        Building = self.ui.Building.text()
        Phone = self.ui.Phone.text()
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        cur.execute(f"insert into plants(IndexPlant, NamePlant, Region, City, Street, Building, Phone) "
                    f"values('{IndexPlant}', '{str(NamePlant)}', '{str(Region)}', '{str(City)}', '{str(Street)}', "
                    f"'{Building}', '{Phone}');")
        con.commit()
        self.close()

class Members(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Members, self).__init__(parent)
        self.ui = Ui_FormMembers()
        self.ui.setupUi(self)
        self.loaddate()
        self.ui.add.clicked.connect(self.add)
        self.ui.dell.clicked.connect(self.delete)

    def delete(self):
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        id = self.ui.id.text()
        cur.execute(f"delete from members where PK_MemberID={id}")
        con.commit()

    def add(self):
        dialog = NewMember(self)
        dialog.exec_()


    def loaddate(self):
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        sqlquary = "select * from members"
        self.ui.tableWidget.setRowCount(50)
        tableIndex = 0
        for row in cur.execute(sqlquary):
            self.ui.tableWidget.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(tableIndex, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(tableIndex, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            tableIndex += 1


class NewMember(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(NewMember, self).__init__(parent)
        self.ui = Ui_FormNewMember()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.insert)

    def insert(self):
        Second_name = self.ui.Second_name.text()
        First_name = self.ui.First_name.text()
        Surname = self.ui.Surname.text()
        Post = self.ui.Post.text()
        FK_PlantID = self.ui.FK_PlantID.text()
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        cur.execute(f"insert into members(Second_name, First_name, Surname, Post, FK_PlantID) "
                    f"values('{Second_name}', '{str(First_name)}', '{str(Surname)}', '{str(Post)}',"
                    f"'{str(FK_PlantID)}');")
        con.commit()
        self.close()


class Products(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Products, self).__init__(parent)
        self.ui = Ui_FormProducts()
        self.ui.setupUi(self)
        self.loaddate()
        self.ui.add.clicked.connect(self.add)
        self.ui.dell.clicked.connect(self.delete)

    def delete(self):
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        id = self.ui.id.text()
        cur.execute(f"delete from products where PK_ProductID ={id}")
        con.commit()

    def add(self):
        dialog = NewProducts(self)
        dialog.exec_()


    def loaddate(self):
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        sqlquary = "select * from products"
        self.ui.tableWidget.setRowCount(50)
        tableIndex = 0
        for row in cur.execute(sqlquary):
            self.ui.tableWidget.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(tableIndex, 4, QtWidgets.QTableWidgetItem(row[4]))
            tableIndex += 1

class NewProducts(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(NewProducts, self).__init__(parent)
        self.ui = Ui_FormNewProduct()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.insert)

    def insert(self):
        IndexProduct = self.ui.IndexProduct.text()
        NameProduct = self.ui.NameProduct.text()
        Sort = self.ui.Sort.text()
        GroupProduct = self.ui.GroupProduct.text()
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        cur.execute(f"insert into products(IndexProduct, NameProduct, Sort, GroupProduct) "
                    f"values('{IndexProduct}', '{str(NameProduct)}', '{str(Sort)}', '{str(GroupProduct)}');")
        con.commit()
        self.close()


class Data(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Data, self).__init__(parent)
        self.ui = Ui_FormData()
        self.ui.setupUi(self)
        self.loaddate()
        self.ui.add.clicked.connect(self.add)
        self.ui.dell.clicked.connect(self.delete)

    def delete(self):
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        id = self.ui.id.text()
        cur.execute(f"delete from actual_data where PK_DataID  ={id}")
        con.commit()

    def add(self):
        dialog = NewData(self)
        dialog.exec_()

    def loaddate(self):
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        sqlquary = "select * from actual_data"
        self.ui.tableWidget.setRowCount(50)
        tableIndex = 0
        for row in cur.execute(sqlquary):
            self.ui.tableWidget.setItem(tableIndex, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(tableIndex, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(tableIndex, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget.setItem(tableIndex, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(tableIndex, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget.setItem(tableIndex, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            tableIndex += 1


class NewData(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(NewData, self).__init__(parent)
        self.ui = Ui_FormNewData()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.insert)

    def insert(self):
        FK_MemberID = self.ui.FK_MemberID.text()
        FK_ProductID = self.ui.FK_ProductID.text()
        CurrentDate = self.ui.CurrentDate.text()
        Purchase_price = self.ui.Purchase_price.text()
        Selling_price = self.ui.Selling_price.text()
        con = sqlite3.connect("sausage.db")
        cur = con.cursor()
        cur.execute(f"insert into actual_data(FK_MemberID, FK_ProductID, CurrentDate, Purchase_price, Selling_price) "
                    f"values('{FK_MemberID}', '{str(FK_ProductID)}', '{str(CurrentDate)}', '{str(Purchase_price)}',"
                    f"'{str(Selling_price)}');")
        con.commit()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWindow = Signin()
    myWindow.show()
    sys.exit(app.exec_())
