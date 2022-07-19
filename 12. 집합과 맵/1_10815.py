import sys
N = int(sys.stdin.readline().rstrip())
A_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
B_list = list(map(int, sys.stdin.readline().split()))

for i in B_list:
  if i in A_list:
    print(1, end = " ")
  else:
    print(0, end = " ")