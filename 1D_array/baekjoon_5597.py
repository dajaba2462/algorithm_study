"""
학생 30명 각 학생별 1번부터 30번까지 번호 부여
28명 제출했는데 제출 안한 2명의 출석 번호를 구하는 프로그램

입력 : 총 28줄로 출석번호 n(1 <= n <= 30) 한줄에 하나씩 주어짐 중복은 없다.

출력 : 2줄 1번째 줄 제출 안한 학생 출석번호 중 가장 작은 것
2번째 줄 그 다음 출석번호
"""

n = 30
arr = []
target_cnt = 28
arr = [i+1 for i in range(n)]
for i in range(target_cnt):
    target = int(input())
    arr.remove(target)

print(min(arr))
print(max(arr))