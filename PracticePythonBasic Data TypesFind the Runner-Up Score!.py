# -*- coding: utf-8 -*-
"""
Created on 20200506

@author: AbhinavGuptaCode
"""

if __name__ == '__main__':
    #number of integers
    n = int(input())
    #list of those integers
    arr=input().split()
    #defining empty list for storing int version of list arr
    arr_int=[]
    #converting all elements in arr list to int type
    for j in range(n):
        arr_int.append(int(arr[j]))
    #defining max and runner up integers
    max_score=0
    runner_up=0
    
    for i in range(n):
        if arr_int[i]>max_score:
            max_score=arr_int[i]
            
    for k in range(n):
        if arr_int[k]>runner_up and arr_int[k]!=max_score:
            runner_up=arr_int[k]
        
    print(runner_up)
    

    