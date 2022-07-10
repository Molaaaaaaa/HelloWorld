import sys

# def quick_sort(li):
#     n = len(li)
#     if n <= 1:
#         return li

#     pivot = li[0]
#     left = []
#     right = []
#     for i in range(1, n):
#         if li[i] < pivot:
#             left.append(li[i])
#         else:
#             right.append(li[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)

# N = int(sys.stdin.readline().rstrip())

# ls = []
# for i in range(N):
#     ls.append(int(sys.stdin.readline().rstrip()))

# ls = quick_sort(ls)
# for i in ls:
#     print(i)

N = int(sys.stdin.readline().rstrip())
ls = [int(sys.stdin.readline().rstrip()) for i in range(N)]
ls = sorted(ls)
for i in ls:
    print(i)