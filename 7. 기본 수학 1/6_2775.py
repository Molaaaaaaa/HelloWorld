import sys
T = int(sys.stdin.readline().rstrip())
kn = []

for i in range(T):
  k = int(sys.stdin.readline().rstrip())
  n = int(sys.stdin.readline().rstrip())
  kn.append(k)
  kn.append(n)

k = [kn[i*2] for i in range(T)]
n = [kn[(i*2) +1] for i in range(T)]
max_k = max(k)
max_n = max(n)

fir_floor = [i for i in range(1, max_n + 1)]
k_n = [fir_floor]

for i in range(max_k):
  k_n.append([1])

for i in range(1, max_k + 1):
  for j in range(1, max_n):
    s = k_n[i][j-1] + k_n[i-1][j]
    k_n[i].append(s)

for i in range(T):
    a = k[i]
    b = n[i]
    print(k_n[a][b-1])