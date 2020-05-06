# -*- coding: utf-8 -*-
"""
Created on 20200506

@author: %AbhinavGuptaCode
"""



def split_and_join(line):
    # split the input line
    
    line=line.split(" ")
    #now line is list
    
    #joining elements of list with "-"
    line="-".join(line)
    #now line is string
    
    return line
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)