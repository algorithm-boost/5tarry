'''
프로그래머스 Level3
문제: 네트워크
링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162
'''
def BFS(start, n, computers):
    global check
    queue = deque()
    queue.append(start)
    check[start]=True
    while queue:
        i = queue.pop()
        for j in range(n):
            if check[j]==False and computers[i][j]==1:
                check[j]=True
                queue.append(j)

def solution(n, computers):
    global check
    answer = 0
    check = [False]*n
    for i in range(n):
        if not check[i]:
            BFS(i, n, computers)
            answer += 1
    return answer
