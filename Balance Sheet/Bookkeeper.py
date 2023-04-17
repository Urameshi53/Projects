# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 21:06:16 2023

@author: User
"""

from datetime import datetime
from datetime import date

accounts = []

class Entry:
    def __init__(self, date: date, details: str, amount: int) -> None:
        self.date = date
        self.details = details
        self.amount = amount 
        
    def __str__(self) -> str:
        return f'Date: {self.date.strftime("%A %d %B %Y")}\nDetails: {self.details}\nAmount: {self.amount}'


class Transaction:
    def __init__(self, a_date: str, dr: str, cr: str, amount: int) -> None:
        # self.date = datetime.now().date()
        self.a_date = date.fromisoformat(a_date)
        self.amount = amount 
        self.dr = dr
        self.cr = cr
    
    def __str__(self) -> str:
        return f'Debited Account: {self.dr}\nCredited Account: {self.cr}\nDate: {self.a_date.strftime("%A %d %B %Y")}\nAmount: {self.amount}'


class Account:
    def __init__(self, name: str) -> None:
        self.name = name 
        self.dr = []
        self.cr = [] 
        
    def debit(self, dr: Entry) -> None:
        self.dr.append(dr)
        
    def getDr(self) -> None:
        for i in self.dr:
            print(i)
    
    def credit(self, cr: Entry) -> None:
        self.cr.append(cr)
        
    def getCr(self) -> None:
        for i in self.cr:
            print(i)
    
    def printAccount(self) -> None:
        print(f'Name: {self.name} Account')
        
        print()
        print('Dr')
        print('-'*15)
        self.getDr()
        
        print()
        print('Cr')
        print('-'*15)
        self.getCr()
        
def client(t: Transaction):
    dr = Entry(t.a_date, t.dr, t.amount)
    cr = Entry(t.a_date, t.cr, t.amount)
    
    def getAccount(name: str) -> Account:
        for i in accounts:
            if i.name == name:
                return i
        else:
            a = Account(name)
            return a
    
    # def enter()
    def setAccounts(dr: Entry, cr: Entry) -> None: 
        a = getAccount(dr.details)
        a.debit(cr)
        
        if a not in accounts:
            accounts.append(a)
            
        b = getAccount(cr.details)
        b.credit(dr)
        
        if b not in accounts:
            accounts.append(b)
            
    setAccounts(dr, cr)
    
    
if __name__=='__main__':
    stoppage = 'yes'
    while stoppage=='yes':
        
        dr = input('Enter account to be debited: ')
        cr = input('Enter account to be credited: ')
        n_date = input('Enter the date: ')
        amount = input('Enter amount: ')
        
        t = Transaction(n_date, dr, cr, amount)
        stoppage = input('Continue?: ')
    
        client(t)
        for i in accounts:
            i.printAccount()
            print('\n')
    
    print(len(accounts))