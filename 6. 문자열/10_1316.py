N = int(input())
cnt = 0

for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_words = word[j+1:]
            if word[j] in new_words:
                cnt -= 1
                break
    cnt += 1

print(cnt)