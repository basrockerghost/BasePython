#My first time with python
# user=input('Enter your name : ')
# print('Hello,',user.upper())

import random as r
# x=r.randrange(1,100)
# for i in range(1,6):
#     y=int(input('Enter your number :'))
#     if y < x:
#         print('Your number is low')
#     elif y>x:
#         print('Your number is high')
#     else:
#         print('Correct number',x)
# print('The correct number is',x)

# list=['apple', 'orange', 'banana', 'mango', 'watermelon']
# list.append('corn')
# print(list)
# print(list[1])
# print(len(list))

'''list={'corn', 'watermalon', 'korn'}
list.add('corn')
print(list)
print(len(list))'''

'''mine={'Name':'Yukino', 'Surname':'Kon', 'hobby':'sleep, play game, read book'}
print(mine)
print(mine.keys())
print(mine.values())
mine['age']=20
print(mine.keys())
mine['Name']='Yuki'
print(mine.values())
mine2={'Name':'Sakuno', 'Surname':'Kon', 'hobby':'sleep, play game, read book', 'age':18}

memberlist=[mine, mine2]
print(memberlist)
print(memberlist[0]['Name'])'''

'''x=r.randrange(1,10)
y=r.randrange(1,10)
if x<y:
    print(x, 'is lower than', y)
elif x>y:
    print(x, 'is higher than', y)
else:
    print(x, 'is equal to', y)'''

'''def myfunc(n):
    return lambda a : a*n
mydouble = myfunc(2)
mytriple = myfunc(3)

print(mydouble(11))
print(mytriple(11))'''
