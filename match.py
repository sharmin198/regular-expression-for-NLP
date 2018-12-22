import re

sentence = "I was born in 1996"

re.match(r".*",sentence)
re.match(r".+",sentence)
re.match(r"[a-zA-Z]*",sentence)
re.match(r"[a-zA-Z]+",sentence)
sen = "a"
re.match(r"ab?",sen)

sent = "1996 is the year when i was born"
re.match(r"[a-zA-Z]+",sent)

re.search(r"[a-zA-Z]+",sent)

#starts with (^)
if(re.match(r"^1996",sent)):
    print("matched")
else:
    print("not matched")
    
#ends with ($)
if(re.search(r"born$",sent)):
    print("matched")
else:
    print("not matched")

