# Task 6

from itertools import count, cycle

# COUNT
for el in count(1):
    if el == 15:
        break
    else:
        print(el)

# CYCLE
c = 0
for el in cycle("zero"):
    if c > 7:
        break
    print(el)
    c += 1
