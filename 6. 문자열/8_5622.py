S = input()
alpha = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0

for i in S:
    for j in range(len(alpha)):
        if i in alpha[j]:
            time += (j + 1 + 2)

print(time)