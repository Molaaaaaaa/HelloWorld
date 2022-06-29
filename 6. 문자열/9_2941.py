S = input()
ls  = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in ls:
    S = S.replace(i, " ")
    print(S)

print(len(S))