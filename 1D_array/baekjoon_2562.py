
n = 1
Max = 0
tot = 0

while True:
    if n > 9:
        break
    num = int(input())
    if Max <= num:
        Max = num
        tot = n
    n += 1

print(Max)
print(tot)