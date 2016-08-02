#-*-coding:UTF-8 -*-
#  EX04_05.py
#
#  使用 yield 模擬 range() 
#  

def myrange(n):
    a=[]
    x = 0
    while True:
        yield x
        yield n
        #a.append(x)
        #a.append(n)
        x += 1
        if x == n:
            break
            #return a 
    
      
print(list(myrange(10)))