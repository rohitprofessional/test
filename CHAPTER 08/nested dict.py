#---------NESTED DICTIONARY--------------- 
# Dictionary keys having another dictionary in them as values.

course = {
'python':{'duration':'3 months','fees':6500},
'php':{'duration':'2 months','fees':5000},
'java':{'duration':'3 months','fees':6500},
'machine learning':{'duration':'2 months','fees':7000},
'artificial intelligence':{'duration':'3 months','fees':8000}
}

print('------------------------------------')
print(course)
print('------------------------------------')
print(course['python'])
print('------------------------------------')
print(course['python']['fees']) # accessing nested dict. values
print('------------------------------------')
course['python']['fees'] = 8000
print('------------------------------------')
print(course)