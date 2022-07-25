import sys

ls = []

for i in range(3):
  ls.append(list(map(int, sys.stdin.readline().split())))

ls_x = []
ls_y = []
for i in range(3):
  ls_x.append(ls[i][0])
  ls_y.append(ls[i][1])

for i in range(3):
  x_num = ls_x.count(ls[i][0])
  y_num = ls_y.count(ls[i][1])
  if x_num == 1:
    x = ls[i][0]
  if y_num == 1:
    y = ls[i][1]

print(x, y)