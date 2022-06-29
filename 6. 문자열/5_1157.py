S = input()
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
cnt = []

for i in range(len(upper)):
    cnt.append(0)

for i in S:
    if i in upper:
        u = upper.index(i)
        cnt[u] += 1
    if i in lower:
        l = lower.index(i)
        cnt[l] += 1

tmp = max(cnt)
index = cnt.index(tmp)
answer = upper[index]
cnt_max = 0

for i in range(26):
    if cnt[i] == tmp:
        cnt_max += 1
        if cnt_max > 1:
            answer = "?"

print(answer)