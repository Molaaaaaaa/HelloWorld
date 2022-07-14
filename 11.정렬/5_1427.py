from audioop import reverse
import sys
N = sys.stdin.readline().rstrip()
ls = [int(i) for i in N]

ls.sort(reverse=True)
# print(* ls, end="")
for i in ls:
    print(i, end = "")