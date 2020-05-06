# -*- coding: utf-8 -*-
"""
Created on 20200506

@author: %AbhinavGuptaCode
"""

if __name__ == '__main__':
    #defining list and making lists of list based on input
    main_list=[]   
    for _ in range(int(input())):
        name = input()
        score = float(input())
        main_list.append([name,score])
    
    #finding lowest marks
    min_score=10000.0
    second_min_score=100000.0
    
    for i in main_list:
        if i[1]<min_score:
            min_score=i[1]
    
    #finding second lowest
    for i in main_list:
        if i[1]<second_min_score and i[1]!=min_score:
            second_min_score=i[1]
    
    #making list for names with second_min_score
    names_second_min=[]
    for i in main_list:
        if i[1]==second_min_score:
            names_second_min.append(i[0])
    
    #soritng the second_min_score list
    names_second_min_sort=sorted(names_second_min)    
    
    #printing line by line alphabetically
    for i in (names_second_min_sort):
        print(i)
        
       