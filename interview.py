#!/usr/bin/python3

n = 6
#count1 = 0
for number1 in range(1,n):
    n = number1 - 1
    for number2 in range(1,number1):
        #print(number2)
        print(n,end="")
        n = n - 1
    print(" ")     
        

