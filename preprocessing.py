# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 10:38:08 2018

@author: Sharmin
"""

import re
list1 = ["It       is       what????????","&dkfjk*     r*   I am","Lion is an animal  &  beast",
         " HI!!!!!!!!!! ","it is that "]
for i in range(len(list1)):
    list1[i] = re.sub(r"\W"," ",list1[i])
    list1[i] = re.sub(r"\d"," ",list1[i])
    list1[i] = re.sub(r"\s+[a-z]\s+"," ",list1[i],flags=re.I)
    list1[i] = re.sub(r"\s+"," ",list1[i])
    list1[i] = re.sub(r"^\s+","",list1[i])
    list1[i] = re.sub(r"\s+$","",list1[i])