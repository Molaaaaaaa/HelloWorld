import sys

N = int(sys.stdin.readline().rstrip())
ls = [sys.stdin.readline().rstrip() for i in range(N)]
ls.sort()
ls = set(ls)
# ls = list(set(ls))
# TypeError: unhashable type: 'list'
ls = list(ls)
ls.sort()
ls.sort(key = lambda x : len(x))
print(ls)
# def function(x):
#   return len(x)

for i in ls:
    print(i)