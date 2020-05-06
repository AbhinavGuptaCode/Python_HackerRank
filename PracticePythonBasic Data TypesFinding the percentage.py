# -*- coding: utf-8 -*-
"""
Created on 20200506

@author: %AbhinavGuptaCode
"""

if __name__ == '__main__':
    #making dictionary from the inputs
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #inputting whose average needs to be found out
    query_name = input()
    
    #initializing new variables
    total=0
    n=0
    
    #calculating average
    for i in student_marks[query_name]:
        total=total+i
        n=n+1
    
    
    print('%.2f'%(total/n))
        
                
            
    
    
    
