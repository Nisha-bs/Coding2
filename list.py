def one(): 
     lis = [1,2,3 ,4] 
     return lis 
 
def second(): 
    #access the list of function one 
    lis = one() 
    print(lis) 
 
second() 