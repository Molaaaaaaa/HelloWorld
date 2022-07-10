import sys
from collections import Counter

def find_m(li_st):
    c = Counter(li_st)
    c = c.most_common()
    lis = []
    result = c[0][0]
    if c[0][1] == c[1][1]:
        for i in range(len(li_st)):
            lis.append(c[i])
            if lis[i] != lis[i-1]:
                result = c[i][0]
                break
    return result

N = int(sys.stdin.readline().rstrip())
ls = [int(sys.stdin.readline().rstrip()) for i in range(N)]
s = sum(ls)
# sorted_ls = sorted(ls)

middle_value = sorted(ls)[(N-1)//2]
ran = max(ls) - min(ls)

print(round(s/N))
print(middle_value)
print(find_m(ls))
print(ran)