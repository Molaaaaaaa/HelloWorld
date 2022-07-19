import sys
N, M = map(int, sys.stdin.readline().split())

A_list = []
B_list = []
A_list= sys.stdin.readline().split()
B_list=sys.stdin.readline().split()

A_set = set(A_list)
B_set = set(B_list)

print(len(A_set ^ B_set))