N = int(input())
# alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\
#     \\$%*+-./:"
P = ""

for i in range(N):
    R, S = input().split()
    R = int(R)
    for j in S:
        P += (j * R)
    P += "\n"

print(P[:-1])