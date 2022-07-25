import sys

ls = []

while True:
  ls.append(list(map(int, sys.stdin.readline().split())))
  if ls[-1][0] == 0:
    ls.pop(-1)
    break

for i in range(len(ls)):
  Heru = max(ls[i])
  ls[i].remove(Heru)
  x = (ls[i][0]) * (ls[i][0])
  y = (ls[i][1]) * (ls[i][1])
  
  if x + y == Heru * Heru:
    print("right")
  else:
    print("wrong")