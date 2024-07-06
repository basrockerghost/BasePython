from collections import Counter
import numpy as np


lst1 = []
lst2 = []

# def Simi_coe(lst1, lst2):
#     l1 = Counter(lst1)
#     l2 = Counter(lst2)
#     intersection = sum((l1 & l2).values())
#     union = sum((l1 | l2).values())
    
#     print(f'intersection : {intersection}')
#     print(f'union : {union}')
#     jaccard = intersection / union
#     return jaccard

# n = int(input('Enter count of elements in X : '))

# for i in range(0, n):
#     x = (input(f'Enter x{i+1} : '))
#     lst1.append(x)
# print(lst1)

# m = int(input('Enter count of elements in Y : '))

# for j in range(0, m):
#     y = (input(f'Enter y{j+1} : '))
#     lst2.append(y)
# print(lst2)

# result = Simi_coe(lst1, lst2)
# print(f'Result is {result}')

def simicoe(lst1, lst2):
    cosine_similarities = []
    for a, b in zip(lst1, lst2):
        cosine_similarity = np.dot(a, b) / (np.norm(a) * np.norm(b))
        cosine_similarities.append(cosine_similarity)
    return cosine_similarities

n = int(input('Enter count of elements : '))

print('Enter X first:')
lst1 = [np.array([float(input(f'Enter x{i+1} : ')) for i in range(n)])]

print('Now enter Y:')
lst2 = [np.array([float(input(f'Enter y{i+1} : ')) for i in range(n)])]

result = simicoe(lst1, lst2)
print(f'Result is {result}')