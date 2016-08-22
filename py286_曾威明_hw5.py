class student:
    def __init__(self,name,gender):
        self.name   = name
        self.gender = gender
        self.grades =[]

    def add(self,grade):
        self.grades.append(grade)
        return True

    def avg(self):
        grades=self.grades
        avg_score=sum(grades) / len(grades)
        return avg_score

    def fcount(self,fail_score):
        grades=self.grades
        fail_score=cord=[i for i in grades if i < fail_score]
        return len(fail_score)
    
    def name(self):
        return  self.name

    def gender(gender):
        return  self.gender    

def top(*student):
    stud=[]
    avg=[]
    for n in student:
        stud.append(n)
        #print(str(n.avg()))
        avg.append(n.avg())

    print("The Top score student :"+stud[avg.index(max(avg))].name+"  gender:"+stud[avg.index(max(avg))].gender +' top average Score:'+str(stud[avg.index(max(avg))].avg()))

def list_all_avg_failrecord(*student):
    for n in student:print('name:'+n.name+ ' gender:'+n.gender+'  avg :'+str(n.avg())+' fail count:'+str(n.fcount(60)))



if __name__ == '__main__':
    s1 = student("Tom","M")
    s2 = student("Jane","F")
    s3 = student("John","M")
    s4 = student("Ann","F")
    s5 = student("Peter","M")
    s1.add(80)
    s1.add(90)
    s1.add(55)
    s1.add(77)
    s1.add(40)
    s2.add(58)
    s2.add(87)
    s3.add(100)
    s3.add(80)
    s4.add(40)
    s4.add(55)
    s5.add(60)
    s5.add(60)
    list_all_avg_failrecord(s1,s2,s3,s4,s5)
    top(s1,s2,s3,s4,s5)

