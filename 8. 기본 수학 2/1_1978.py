import sys

N = int(sys.stdin.readline().rstrip())

ls = list(map(int, sys.stdin.readline().split()))

prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
num_ls = [0] * 1000
for i in range(1000):
    num_ls[i] = i+1


for i in prime_number:
    rng = 1000//i
    for j in range(rng):
        n_prime = i * (j+1)
        if n_prime in num_ls:
            num_ls.remove(n_prime)

num_ls.remove(1)

cnt = 0
for i in ls:
    if i in prime_number or i in num_ls:
        cnt += 1

print(cnt)