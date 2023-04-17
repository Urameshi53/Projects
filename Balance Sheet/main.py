# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:32:33 2023

@author: User
"""

#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
import sys
from BalanceSheet import BalanceSheet
from Bookkeeper import Account, Entry, Transaction
from datetime import *

pos = 0

account = Account('Bank')
account.debit(Entry(date.fromisoformat('2023-01-01'),'Bank',100000))
account.debit(Entry(date.fromisoformat('2023-01-02'),'Van',16000))
account.credit(Entry(date.fromisoformat('2023-01-02'),'Cash',16000))
account.credit(Entry(date.fromisoformat('2023-01-02'),'Capital',16000))

account1 = Account('Cash')
account1.debit(Entry(date.fromisoformat('2023-01-01'),'Bank',100000))
account1.debit(Entry(date.fromisoformat('2023-01-02'),'Van',16000))

account2 = Account('Van')
account2.credit(Entry(date.fromisoformat('2023-01-01'),'Melcom',500))
account2.debit(Entry(date.fromisoformat('2023-01-02'),'Bank',3000))

account3 = Account('Melcom')
account3.credit(Entry(date.fromisoformat('2023-01-01'),'Melcom',500))
account3.debit(Entry(date.fromisoformat('2023-01-02'),'Bank',3000))

account4 = Account('Capital')
account4.credit(Entry(date.fromisoformat('2023-01-01'),'Melcom',500))
account4.credit(Entry(date.fromisoformat('2023-01-02'),'Bank',3000))

account5 = Account('KNUST')
account5.debit(Entry(date.fromisoformat('2023-01-01'),'Melcom',500))
account5.credit(Entry(date.fromisoformat('2023-01-02'),'Bank',3000))

_accounts = []
_accounts.append(account)
_accounts.append(account1)
_accounts.append(account2)
_accounts.append(account3)
_accounts.append(account4)
_accounts.append(account5)

class Window(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self)    
        self.createUI()
        self.data = {}
        self.file_path = None
        self.window = []
        self.accounts = []
        
    def createUI(self) -> None:
        self.setMinimumSize(800,720)    
        self.setWindowTitle('Bookkeeper')
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
    
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction('&New').triggered.connect(self.newFile)
        fileMenu.addAction('&Save').triggered.connect(self.save)
        fileMenu.addAction('&Save as').triggered.connect(self.save_as)
        fileMenu.addAction('&Open').triggered.connect(self.open_file)
        fileMenu.addAction('&Print Balance Sheet').triggered.connect(self.printSheet)
        fileMenu.addAction('&Print to console').triggered.connect(self._print)
        fileMenu.addAction('&Close').triggered.connect(self.close)

        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction('&Copy')
        
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction('&About us').triggered.connect(self.about)
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(4)
        layout.addWidget(self.tableWidget, 1, 0)
        
        self.tableWidget.setHorizontalHeaderLabels(['Date', 'Debited Account', 'Credited Account', 'Amount'])

    def transact(self, t: Transaction) -> None:
        dr = Entry(t.a_date, t.dr, t.amount)
        cr = Entry(t.a_date, t.cr, t.amount)
        
        def getAccount(name: str) -> Account:
            for i in self.accounts:
                if i.name == name:
                    return i
            else:
                a = Account(name)
                return a
        
        # def enter()
        def setAccounts(dr: Entry, cr: Entry) -> None: 
            a = getAccount(dr.details)
            a.debit(cr)
            
            if a not in self.accounts:
                self.accounts.append(a)
                
            b = getAccount(cr.details)
            b.credit(dr)
            
            if b not in self.accounts:
                self.accounts.append(b)
                
        setAccounts(dr, cr)

    def printSheet(self) -> None:
        if self.file_path is None:
            self.save_as() 
            self.insertData()
        balanceSheet = BalanceSheet()
        balanceSheet.createUI(self.accounts)
        
        self.window.append(balanceSheet)
        balanceSheet.show()

    def _print(self) -> None:
        for row in range(50):
            for col in range(4):
                item = self.tableWidget.item(row,col)
                if item is not None:
                    print(row, col, item.text())
        print('Ok it worked. Sort of!!!')

    def newFile(self) -> None:
        #newWindow = self
        #self.window.append(newWindow)
        #newWindow.show
        pass

    def open_file(self) -> None:
        path = QFileDialog.getOpenFileName(self, 'Open')[0]
        if path:
            self.file_path = path
        self.data.clear()
        self.accounts = []
        print(self.data.items(), len(self.accounts))
        self.insertData()
        print(self.data.items(), len(self.accounts))
        self.insertTable()
        
    def insertTable(self):
        horHeaders = []
        for n, key in enumerate(self.data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.tableWidget.setItem(m, n, newitem)
        self.tableWidget.setHorizontalHeaderLabels(horHeaders)

    def insertData(self):
        with open(self.file_path, 'r') as f:
            data = f.readlines()
            self.data['Date'] = []
            self.data['Debited'] = []
            self.data['Credite'] = []
            self.data['Amount'] = []
            for i in data:
                if len(i)>1:
                    n = i.split()
                    self.data['Date'].append(n[0])
                    self.data['Debited'].append(n[1])
                    self.data['Credite'].append(n[2])
                    self.data['Amount'].append(n[3])
                    transaction = Transaction(n[0],n[1],n[2],n[3])
                    self.transact(transaction)
        
    def save(self) -> None:
        #self.data = {}
        if self.file_path is None:
            self.save_as() 
        else:
            with open(self.file_path, 'w') as f:
                for row in range(50):
                    for col in range(4):
                        item = self.tableWidget.item(row,col)
                        if item is None:
                            f.write('')
                        else:
                            f.write('{:20s}'.format(item.text()))
                    f.write('\n')
    
    def save_as(self)->None:
        path = QFileDialog.getSaveFileName(self, 'Save as')[0]
        if path:
            self.file_path = path+'.txt'
            self.save()

    def about(self)-> None:
        text = "<center>" \
           "<h1>Text Editor</h1>" \
           "&#8291;" \
           "<img src=icon.svg>" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
        QMessageBox.about(self, 'About Bookkeeper', text)




app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())