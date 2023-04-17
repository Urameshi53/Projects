# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:29:47 2023

@author: User
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys 
from Bookkeeper import Account, Entry
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

accounts = []
accounts.append(account)
accounts.append(account1)
accounts.append(account2)
accounts.append(account3)
accounts.append(account4)
accounts.append(account5)

class BalanceSheet(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumWidth(1280)
        #self.createUI(accounts)
        
    def createUI(self, accounts):
        #self.setMinimumSize(800,720)    
        self.setWindowTitle('Balance Sheet')

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        #self.createTTable()
        
        for i in accounts:
            self.addTable(i)

    def createTTable(self):
        dr = QLabel('Dr')
        cr = QLabel('Cr')
        name = QLabel('Name')
        date = QLabel('Date')
        detail = QLabel('Detail')
        amount = QLabel('Amount')

        date1 = QLabel('Date')
        detail1 = QLabel('Detail')
        amount1 = QLabel('Amount')

        date2 = QLabel('2023-02-03')
        detail2 = QLabel('Bank')
        amount2 = QLabel('100000')

        date3 = QLabel('2023-02-05')
        detail3 = QLabel('Cash')
        amount3 = QLabel('100000')

        self.layout.addWidget(dr,0,0)
        self.layout.addWidget(name,0,3)
        self.layout.addWidget(cr,0,8)

        self.layout.addWidget(date,1,0)
        self.layout.addWidget(detail,1,1)
        self.layout.addWidget(amount,1,2)
        self.layout.addWidget(date1,1,6)
        self.layout.addWidget(detail1,1,7)
        self.layout.addWidget(amount1,1,8)
        
        self.layout.addWidget(date2,2,0)
        self.layout.addWidget(detail2,2,1)
        self.layout.addWidget(amount2,2,2)
        self.layout.addWidget(date3,2,6)
        self.layout.addWidget(detail3,2,7)
        self.layout.addWidget(amount3,2,8)

    def addTable(self, account):
        global pos
        self.layout.addWidget(QLabel('Dr'),pos,0)
        self.layout.addWidget(QLabel(account.name),pos,3)
        self.layout.addWidget(QLabel('Cr'),pos,8)

        pos += 1

        self.layout.addWidget(QLabel('Date'),pos,0)
        self.layout.addWidget(QLabel('Details'),pos,1)
        self.layout.addWidget(QLabel('Amount'),pos,2)

        pos += 1
        n_pos = pos
        for i in account.dr:
            self.layout.addWidget(QLabel(i.date.strftime("%A %d %B %Y")),pos,0)
            self.layout.addWidget(QLabel(i.details),pos,1)
            self.layout.addWidget(QLabel(str(i.amount)),pos,2)
            pos += 1

        pos = n_pos-1
        self.layout.addWidget(QLabel('Date'),pos,6)
        self.layout.addWidget(QLabel('Details'),pos,7)
        self.layout.addWidget(QLabel('Amount'),pos,8)

        pos += 1 
        for j in account.cr:
            self.layout.addWidget(QLabel(j.date.strftime("%A %d %B %Y")),pos,6)
            self.layout.addWidget(QLabel(j.details),pos,7)
            self.layout.addWidget(QLabel(str(j.amount)),pos,8)
            pos += 1
        pos += 2

#app = QApplication(sys.argv)
#screen = BalanceSheet()
#screen.show()
#sys.exit(app.exec_())