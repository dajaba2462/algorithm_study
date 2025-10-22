T = int(input())

txt =""
for _ in range(T):
    R, S = map(str, input().split())
    for s in S:
        txt += (s * int(R))
    txt += "\n"
print(txt)
