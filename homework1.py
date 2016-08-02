math_pass=['Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy']
eng_pass=['John', 'Mary' , 'Tony', 'Bob' , 'Pony', 'Tom' , 'Alice']
math_pass_eng_failed=[]
eng_pass_math_failed=[]
all_pass=[]

for student in math_pass:
    if (student not in eng_pass): 
        math_pass_eng_failed.append(student)
print "\n math pass but eng failed"
for p in math_pass_eng_failed: print p

for student in eng_pass:
    if (student not in math_pass): 
        eng_pass_math_failed.append(student)
print "\n eng pass but math failed"
for p in eng_pass_math_failed: print p

for student in eng_pass:
    if (student in math_pass): 
        all_pass.append(student)
print "\n all pass math and eng "
for p in all_pass: print p

