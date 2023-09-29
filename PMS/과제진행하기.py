'''
프로그래머스 Level2
문제: 과제 진행하기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/176962#
접근 방식: 현재 진행 중인 과제의 시간이 부족하면 스택에 추가하고, 시간이 남으면 스택에 있는 (멈춰둔) 과제를 진행한다. 멈춰둔 과제를 진행할 때마다 재귀함수가 호출된다.
'''

import sys
sys.setrecursionlimit(10**6)

def homework(name, diff):
    if (diff>0):  # 시간이 부족
        stack.append([name, diff])
    elif (diff<0):  # 시간이 남음
        answer.append(name)
        if (stack):
            name, playtime = stack.pop()
            homework(name, playtime+diff)
    else:  # 시간이 딱 맞음
        answer.append(name)
        
def solution(plans):
    plans = sorted(map(lambda x:[x[0], int(x[1][:2])*60+int(x[1][3:]), int(x[2])], plans), key=lambda x:x[1])
    
    for i in range(len(plans)-1):
        name, start, playtime = plans[i]
        end = plans[i+1][1]
        diff = int(playtime) - (end-start)
        homework(name, diff)
    homework(plans[-1][0], -100000)
    
    return answer

answer = []
stack = []
