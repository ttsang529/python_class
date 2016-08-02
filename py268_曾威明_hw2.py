
class Multiplication:
        def __init__(self,num):
            self.num = num
        
        def table(self):
            print '\n'.join(['\t'.join(['%d*%d=%d' % (j,i,i*j) for i in range(1,self.num)]) for j in range(1,self.num)]) 

def get_multi_num():        
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            multi_num = int(input("Please enter number built up your Multiplication table: "))
        except ValueError:
            print("Sorry, I didn't integer num.")
            #better try again... Return to the start of the loop
            continue
        else:
            #age was successfully parsed!
            #we're ready to exit the loop.
            break
#print (multi_num)
    multi_num=multi_num+1
    return multi_num

if __name__ == '__main__':
    Multiplication(get_multi_num()).table()
  
