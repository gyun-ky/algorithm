
array = [100, 3000, 232]
new_array = []

for i in range(len(array)):
    tmp = array[i]
    while True:
        if tmp // 10 < 1:
            new_array.append(tmp)
            break
        else:
            tmp = tmp // 10
            print(tmp)

print(new_array)
