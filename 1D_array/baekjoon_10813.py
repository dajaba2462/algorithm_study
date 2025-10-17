
N,M = map(int, input().split())
temp = 0
arr = [i+1 for i in range(N)]

for idx in range(M):
    i, j = map(int, input().split())

    temp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = temp
print(*arr)
        