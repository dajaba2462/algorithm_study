t = int(input())
arr = []

for _ in range(t):
    text = list(input())
    arr.append(text[0] + text[-1])

for result in arr:
    print(result)
