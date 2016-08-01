#!/usr/bin/env python
import os, sys

def question1():
    math_pass={'Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy'}
    eng_pass={'John', 'Mary' , 'Tony', 'Bob' , 'Pony', 'Tom' , 'Alice'}
    show_qu1_mass_pass_eng_failed(math_pass,eng_pass)
    show_qu1_eng_pass_math_failed(math_pass,eng_pass)
    show_qu1_all_pass(math_pass,eng_pass)


def show_qu1_mass_pass_eng_failed(math_pass,eng_pass):
    math_pass_eng_failed=set()
    for student in math_pass:
        if (student not in eng_pass): 
            math_pass_eng_failed.add(student)
    print ("\n math pass but eng failed")
    for p in math_pass_eng_failed: print (p)

def show_qu1_eng_pass_math_failed(math_pass,eng_pass):
    eng_pass_math_failed=set()
    for student in eng_pass:
        if (student not in math_pass): 
            eng_pass_math_failed.add(student)
    print ("\n eng pass but math failed")
    for p in eng_pass_math_failed: print (p)

def show_qu1_all_pass(math_pass,eng_pass):
    all_pass=set()
    for student in eng_pass:
        if (student in math_pass): 
            all_pass.add(student)
    print ("\n all pass math and eng ")
    for p in all_pass: print (p)

def question2():
    test_result={"Tom":[80, 100, 90, 95],"John":[100,93,75,80]}
    show_qu2_students_average_score(test_result)


def show_qu2_students_average_score(test_result):
    for student in list(test_result.keys()):
        total_score=test_result[student]
        print ("\n"+student+ "   average score be /n")
        print (sum(total_score)/len(total_score))

if __name__ == '__main__':
    question1()
    question2()