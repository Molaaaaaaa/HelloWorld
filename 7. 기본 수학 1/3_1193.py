X = int(input())

line = 0
max = 0

while X > max:
    line += 1
    max += line

d = max - X

if line % 2 == 0:
    top = line - d
    under = d + 1
else:
    top = d + 1
    under = line - d

print(f"{top}/{under}")