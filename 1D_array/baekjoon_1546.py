"""
세준이 점수 조작 자기점수 최댓값(M) 고르고
모든 점수를 점수/M*100으로 고침

"""

M = int(input())
score = list(map(int,input().split()))
max_score = max(score)
score_list = [score[i]/max_score*100 for i in range(M)]

print(sum(score_list)/ M)
