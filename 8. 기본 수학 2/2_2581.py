import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

ls = []
prime = [2, 3, 5, 7 , 11, 13, 17, 19, 23, 29, 31,
            37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
            79, 83, 89, 91, 97]

for i in range(M, N + 1):
    for j in range(2, i + 1):
        if j == i:
            ls.append(i)
        if i % j == 0:
            break


if len(ls) == 0:
    print(-1)
else:
    print(sum(ls))
    print(ls[0])