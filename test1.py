from itertools import permutations
from operator import itemgetter, attrgetter

a = [(1,2), (2, 2), (2, 1)]
test = [1, 3, 2]
a.sort(key = itemgetter(0, 1))
print(a)


result = sorted(a, key= lambda a : (a[0], a[1]))
print(result)

class User:
    
    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd

user_list = [
 	User('id2', '1234'),
    User('id1', '2345')
    ]
 
 # iterable 객체이기 때문에 sorted 사용
 
result = sorted(user_list, key = attrgetter('id'))
 
for u in result:
    print(u.id)
 
# print(list(permutations(a, 3)))
# commit


dict = {1 : 1, 3 : 2, 2 : 2}
result = sorted(dict.items(), key=lambda a:(a[1], a[0]))
print(result)


A = [list() for _ in range(3)]
print(A)

new_A = [[1,2], [3, 4]]
A = new_A
print(A)