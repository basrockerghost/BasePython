from math import sqrt
import numpy as np

lst1 = []
lst2 = []

def Eucidean(lst1, lst2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(lst1, lst2)))

n = int(input('Enter count of elements : '))

print(f'Enter X first')
for i in range(0, n):
    x = (float(input(f'Enter x{i+1} : ')))
    lst1.append(x)
print(lst1)

print(f'Now enter Y')
for j in range(0, n):
    y = (float(input(f'Enter y{j+1} : ')))
    lst2.append(y)
print(lst2)

result = Eucidean(lst1, lst2)
print(f'Result is {result}')