# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:59:03 2020

@author: llkg1
"""

numbers=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,6,9,7,2,3,5,4,8]
counter={}

for number in numbers:
    if number in counter:
        counter[number]=counter[number]+1
    else:
        counter[number]=1

print(counter)