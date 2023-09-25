'''
프로그래머스 Level2
문제: 혼자 놀기의 달인
링크: https://school.programmers.co.kr/learn/courses/30/lessons/131130?language=python3
접근 방식: 모든 그룹이 순환 고리 형태일 수 밖에 없기 때문에, DFS처럼 접근하여 순환 고리의 최대 길이를 구하면 된다.
'''

def solution(cards):
    group = [0] # 그룹별 길이
    visited = [False for _ in range(len(cards))]  # 방문 여부
    
    for i in range(len(cards)):
        idx = i
        length = 0
        while (not visited[idx]):
            visited[idx] = True
            length += 1
            idx = cards[idx]-1
        group.append(length)
    
    group.sort(reverse=True)
    return group[0]*group[1]
