from itertools import combinations

num=[int(n) for n in input("Enter numbers-").split()]
summ=int(input("Enter summation-"))

cnt=0
for i in range(1, len(num)+1):
    for j in combinations(num, i):
        if sum(j)==summ:
            cnt=cnt+1
print(cnt)
