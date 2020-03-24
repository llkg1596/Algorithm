# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:38:44 2020

@author: llkg1
"""

character={
        "name":"기사",
        "level":"12",
        "items":{
                "sword":"불꽃의 검",
                "armor":"풀플레이트"
                },
        "skill":["베기", "세게 베기", "아주 세게 베기"]         
        }

for key in character:
    #dictation 은 key
    if type(character[key]) is dict:
        for dict_key in character[key]:
            print(dict_key, ":", character[key][dict_key])
    
    #list 는 item
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else: 
        print(key,":",character[key])
        
        
