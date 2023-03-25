# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:21:14 2023

@author: Admin
"""

##a-

def revword(word:str) -> str: 
    word = word.lower()
    word = word[::-1]
    return word


##b
def countword()->int:
    with open('text.txt') as f:
        lines = f.readlines()
        is_first_line = True
        counter = 1
        for line in lines:
            if is_first_line:
                word = line.lower().replace('\n','')
                is_first_line = False
                continue
            line = line.split()
            for tempword in line:
                if word == revword(tempword):
                    counter += 1
    return counter
                
        
    
x = countword()
print(x)

        


         