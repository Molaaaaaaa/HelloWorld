import sys
sys.setrecursionlimit(10 ** 6)

def recursion(n):
    if n == 3:
        return ["***", "* *", "***"]
    
    arr = recursion(n//3)
    stars = []

    for i in arr:
        stars.append(i * 3)
    for i in arr:
        stars.append(i + " "*(n//3) + i)
    for i in arr:
        stars.append(i*3)

    return stars

N = int(input())

print("\n".join(recursion(N)))