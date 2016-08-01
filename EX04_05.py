#-*-coding:UTF-8 -*-
#  EX04_05.py
#
#  使用 yield 模擬 range() 
#  

def myrange(n):
    x = 0
    while True:
        yield x
        yield n
        x += 1
        if x == n:
            break 
y=9;
      
print(list(myrange(10)))