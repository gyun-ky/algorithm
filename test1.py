from itertools import permutations

a = [(1,2), (3, 4), (4,5)]

d = []

arr1 = [[0, 1, 2], [3, 4, 5]]
arr2 = [[6, 7, 8], [9, 10, 11]]
print(arr1[0][2])

d.append(arr1)
d.append(arr2)
print(d[0][0][2])
print(d[1][0][2])

p = [i for i in range(3)]
print(p)
# print(list(permutations(a, 3)))
# commit