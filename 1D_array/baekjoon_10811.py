""" 바구니 총 N개 , 1번부터 N번까지 순서대로 번호

M번 바구니의 순서 역순 바꿀려함. 순서를 역순으로 만들 범위를 정함
그 범위에 들어있는 바구니의 순서를 역순으로 만듬
"""


N, M = map(int, input().split())
arr = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int,input().split())
    arr[i-1:j] = reversed(arr[i-1: j])

print(*arr)



