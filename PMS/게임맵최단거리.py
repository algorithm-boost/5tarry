'''
프로그래머스 Level2
문제: 게임 맵 최단거리
링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
'''
from collections import deque

def BFS(maps):
    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        if x-1>=0 and maps[y][x-1]==1:
            maps[y][x-1]=maps[y][x]+1
            queue.append((x-1, y))
        if x+1<len(maps[0]) and maps[y][x+1]==1:
            maps[y][x+1]=maps[y][x]+1
            queue.append((x+1, y))
        if y-1>=0 and maps[y-1][x]==1:
            maps[y-1][x]=maps[y][x]+1
            queue.append((x, y-1))
        if y+1<len(maps) and maps[y+1][x]==1:
            maps[y+1][x]=maps[y][x]+1
            queue.append((x, y+1))
def solution(maps):
    BFS(maps)
    answer = maps[-1][-1]
    if answer==1:
        if len(maps)!=1 or len(maps[0])!=1:
                answer=-1
    return answer
