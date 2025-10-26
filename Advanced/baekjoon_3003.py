arr = list(map(int, input().split()))
piece = [1, 1, 2, 2, 2, 8]
for i in range(len(piece)):
    x = piece[i] - arr[i]
    print(x, end=" ")




