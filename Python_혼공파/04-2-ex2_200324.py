# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:22:00 2020

@author: llkg1
"""

pets=[
     {"name": "구름", "age":"5"},
     {"name": "초코", "age":"3"},
     {"name": "아지", "age":"1"},
     {"name": "호랑이", "age":"1"}
     ]

print("#Pets in my neighbors")
for index in pets:
    print(index["name"], str(index["age"])+"살")
      
