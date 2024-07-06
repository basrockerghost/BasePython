# import numpy as np
# from math import sqrt
# from numpy.linalg import norm
# from numpy import dot

# lst1 = []
# lst2 = []

# def cosine(lst1, lst2):
#     for a, b in zip(lst1, lst2):
#         return dot(a, b)/(norm(a)*norm(b))

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

# result = cosine(lst1, lst2)
# print(f'Result is {result}')
import numpy as np
from numpy.linalg import norm
from numpy import dot

def cosine(lst1, lst2):
    cosine_similarities = []
    for a, b in zip(lst1, lst2):
        cosine_similarity = dot(a, b) / (norm(a) * norm(b))
        cosine_similarities.append(cosine_similarity)
        print(f'{dot(a, b)}')
    return cosine_similarities

n = int(input('Enter count of elements : '))

print('Enter X first:')
lst1 = [np.array([float(input(f'Enter x{i+1} : ')) for i in range(n)])]

print('Now enter Y:')
lst2 = [np.array([float(input(f'Enter y{i+1} : ')) for i in range(n)])]

result = cosine(lst1, lst2)
print(f'Result is {result}')