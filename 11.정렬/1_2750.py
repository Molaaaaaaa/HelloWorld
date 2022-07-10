import sys
sys.setrecursionlimit(99999)
def quick_sort(li):
    if len(li) <= 1:
        return li

    pivot = li[0]
    left = [i for i in li[1:] if i < pivot]
    right = [i for i in li[1:] if i >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

N = int(sys.stdin.readline().rstrip())

ls = []
for i in range(N):
    ls.append(int(sys.stdin.readline().rstrip()))

ls = quick_sort(ls)

for i in ls:
    print(i)

# N = int(sys.stdin.readline().rstrip())
# ls = [int(sys.stdin.readline().rstrip()) for i in range(N)]
# ls = sorted(ls)
# for i in ls:
#     print(i)