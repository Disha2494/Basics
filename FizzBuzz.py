# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:06:01 2022

@author: Disha
"""

def FizzBuzz():
    for i in range(1,21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
FizzBuzz()