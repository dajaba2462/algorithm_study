N = int(input())
Arr = input().split()
target = int(input())
count = 0

for i in range(N):
    if target == int(Arr[i]):
        count += 1

print(count)