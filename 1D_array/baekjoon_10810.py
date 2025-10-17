N, M = map(int, input().split())

arr = [0] * (N+1)


for _ in range(M):
    i, j, k = map(int,input().split())
    for idx in range(i-1, j):
        arr[idx] = k

for i in range(N):
    print(arr[i], end= " ")