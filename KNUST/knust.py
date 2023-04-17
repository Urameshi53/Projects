# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:07:55 2021

@author: User
"""

import pandas as pd
titanic = pd.read_excel("econs.xlsx",usecols=[0,1,2,3])
# user_id = pd.read_excel("econs.xlsx", usecols=[0])
# index = pd.read_excel("econs.xlsx", usecols=[1])
# mid_score = pd.read_excel("econs.xlsx", usecols=[3])
# print(titanic.head(56))
# print(user_id)
# print(index.tail(50))
# print(mid_score)
# print(mid_score.mean())

# class User(object):
#     def __init__(self, id, index_no, mid_score):
#         self.index_no = index_no
#         self.id = id
#         self.mid_score = midscore
        
#     def result(self, mid):
#         for i in mid:
#             if int(i) == self.index_no:
#                 self.mid_score = 
# print(titanic)
print(titanic['mid_score'].describe())
# print(titanic.describe())
