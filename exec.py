import sys
import numbers

def getInput():
    while True:
        try:
            input1 = input('input first int number:')
            input1 = int(input1)
            #print(input1)
            if isinstance(input1, int):
                return input1

        except:
            pass 

def divide(num1,num2):
    try:
        result=(num1/num2)
        return result

    except ZeroDivisionError:
        print("Hello world")

    except Exception as e:
         print(e)

if __name__ == '__main__':

    num1=getInput()
    num2=getInput()
    result=divide(num1,num2)
    if (result):
        print(result)