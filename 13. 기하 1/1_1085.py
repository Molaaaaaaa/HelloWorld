import sys
x, y, w, h = map(int, sys.stdin.readline().split())

ls = [w-x, h-y, x, y]

print(min(ls))