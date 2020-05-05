# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:38:05 2020

@author: AbhinavGuptaCode
"""

def swap_case(s):
    
    # defining empty list to store characters of input string
    swapped_string_list=[]
    for i in s:
        if i.islower():
            #islower() function returns true or false 
            i=i.upper()
        elif i.isupper():
            i=i.lower()
        else:
            pass
         
        #adding element i to the list swapped_string_list
        swapped_string_list.append(i)
    
    #defining empty string
    swapped_string=''
    #making string from list from elements one by one 
    for k in swapped_string_list:
        swapped_string=swapped_string+k
        
    return swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)