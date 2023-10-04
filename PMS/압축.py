'''
프로그래머스 Level2
문제: 압축
링크: https://school.programmers.co.kr/learn/courses/30/lessons/17684
'''
def solution(msg):
    answer = []
    dictionary = {}
    for i in range(ord('A'), ord('Z')+1):
        dictionary[chr(i)]=i-ord('A')+1
    
    msg += '!'
    i = 0
    while i<len(msg)-1:
        for j in range(i+1, len(msg)):
            if not msg[i:j+1] in dictionary:
                dictionary[msg[i:j+1]]=len(dictionary)+1
                answer.append(dictionary[msg[i:j]])
                i = j
                break
        
    return answer
