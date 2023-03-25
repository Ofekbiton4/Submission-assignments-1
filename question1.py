# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:05:21 2023

@author: Admin
"""

def my_func(x1,x2,x3):
    if isinstance(x1,int) or isinstance(x2,int) or isinstance(x3,int):
        print('Error: Parameters shold be float.')
    elif not isinstance(x1,float) or not isinstance(x2,float) or not isinstance(x3,float):
        return None
    elif x1+x2+x3 == 0:
        print('Not a number - denominator is equals to zero')
    else:
        return ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)




    
    


        