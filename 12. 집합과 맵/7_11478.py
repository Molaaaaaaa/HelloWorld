import sys
S = sys.stdin.readline().rstrip()
rst = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        tmp = S[i : j+1]
        print(tmp)
        rst.add(tmp)

print(len(rst))