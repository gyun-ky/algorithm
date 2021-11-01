import sys
import copy
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

max_energy = 0

def search(array, energy):
    global max_energy
    n = len(array)

    if n == 2:
        max_energy = max(energy, max_energy)
        return

    for i in range(1, n-1):
        new_array = copy.deepcopy(array)
        new_add_energy = new_array[i-1] * new_array[i+1]
        del new_array[i]
        search(new_array, energy+new_add_energy)

search(data, 0)
print(max_energy)


