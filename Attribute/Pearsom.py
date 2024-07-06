# import numpy as np
# from math import sqrt

# lst1 = []
# lst2 = []

# def Pearson(lst1, lst2):
#     x_bar = (1/n)*sum(a for a in zip (lst1))
#     y_bar = (1/n)*sum(b for b in zip (lst2))
#     Sx = sqrt((1/(n-1))*sum((a - x_bar)**2)for a in zip (lst1))
#     Sy = sqrt((1/(n-1))*sum((b - y_bar)**2)for b in zip (lst2))
#     Sxy = (1/(n-1)*sum((a-x_bar)*(b-y_bar)for a, b in zip(lst1, lst2)))
#     cor_xy = Sxy / (Sx*Sy)
#     return cor_xy
    
# n = int(input('Enter count of elements : '))

# print(f'Enter X first')
# for i in range(0, n):
#     x = float(input(f'Enter x{i+1} : '))
#     lst1.append(x)
# print(lst1)

# print(f'Now enter Y')
# for j in range(0, n):
#     y = float(input(f'Enter y{j+1} : '))
#     lst2.append(y)
# print(lst2)

# result = Pearson(lst1, lst2)
# print(f'Result is {result}')
import numpy as np

def Pearson(lst1, lst2):
    n = len(lst1)
    x_bar = sum(lst1) / n
    y_bar = sum(lst2) / n
    Sx = np.sqrt((1/(n-1))*sum((a - x_bar)**2 for a in lst1))
    Sy = np.sqrt((1/(n-1))*sum((b - y_bar)**2 for b in lst2))
    Sxy = (1/(n-1))*sum((a-x_bar)*(b-y_bar) for a, b in zip(lst1, lst2))
    cor_xy = Sxy / (Sx*Sy)
    return cor_xy
    
n = int(input('Enter count of elements : '))

print('Enter X first:')
lst1 = [float(input(f'Enter x{i+1} : ')) for i in range(n)]
print(lst1)

print('Now enter Y:')
lst2 = [float(input(f'Enter y{i+1} : ')) for i in range(n)]
print(lst2)

result = Pearson(lst1, lst2)
print(f'Result is {result}')
