#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 13:49:49 2018

@author: karan
"""
# Program to print numbers between 2000 and 3200(both included)divisible by 7
# and not by 5 in a single line separated by comma
output = []
ctr=0
for i in range(2000,3201):
    if i %7 ==0 and i%5!=0:
        output.append(i)
        ctr+=1
print(*output,sep=" , ")
print(ctr)
