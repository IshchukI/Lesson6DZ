#Сравнение идет со следующим элементом и длинна второго цикла на 1 меньше длинны списка

import random

def bubke_sort(l):
    t = l.copy()
    for n in range(0, len(t)):
        for i in range(0, len(t) - n - 1):
            a = t[i]
            b = t[i + 1]
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
    return t

nums = [random.randint(0, 30) for x in range(0, 20)]
sorted = bubke_sort(nums)
print(sorted)
