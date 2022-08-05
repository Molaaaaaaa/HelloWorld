import sys

while True:
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0:
        break
    
    if x > y:
        for i in range(10000):
            if x == y * i:
                print("multiple")
                break
        else:
            print("neither")

    elif x < y:
        for i in range(10000):
            if y == x * i:
                print("factor")
                break
        else:
            print("neither")
            