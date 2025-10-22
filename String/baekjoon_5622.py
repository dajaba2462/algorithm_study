arr = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
txt = input()
cnt = 0
for i in range(len(arr)):
    for j in txt:
        if j in arr[i]:
            cnt += i + 3
print(cnt)
