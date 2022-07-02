n = int(input())
p_0 = 0
p_1 = 1
p_n = 0

for i in range(n-1):
    p_n = p_1 + p_0
    p_0 = p_1
    p_1 = p_n

if n == 1:
    p_n = 1

print(p_n)