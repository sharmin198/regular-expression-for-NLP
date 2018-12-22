# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 23:11:16 2018

@author: Sharmin
"""
#shorthand characters
import re

sentence = "I love Avengers"
print(re.sub(r"Avengers","Justice League",sentence))
sent = "It is this which is that"
print(re.sub(r"is","was",sent))
print(re.sub(r"[a-z]","0",sent))
print(re.sub(r"[a-z]","0",sent,flags = re.I)) #here I means case insensitive
print(re.sub(r"[a-z]","0",sent,1,flags = re.I))

sentence1 = "I was born in 1996"
sentence2 = "Just $%(@)#   jack. has 'arrived"
sentence3 = "I          love             whatever"  
sentence1_modified = re.sub(r"\d","",sentence1)
sentence2_modified = re.sub(r"[@#$%!&*)(/./']"," ",sentence2)
sentence2_modified = re.sub(r"\w"," ",sentence2)
sentence2_modified = re.sub(r"\W"," ",sentence2)
sentence3_modified = re.sub(r"\s+"," ",sentence3)
sentence4 = "I             love                    you"
sentence4_modified = re.sub(r"\s+love\s+"," hate ",sentence4)