'''
프로그래머스 Level2
문제: 숫자 블록
링크: https://school.programmers.co.kr/learn/courses/30/lessons/12923
접근 방식: 자신을 제외한 약수 중에 제일 큰 수를 찾으면 된다. 이때 도로의 길이와 블록의 개수가 다르기 때문에 유의해야 한다.
'''
def maxdivisor(num):
    if num == 1:
        return 0
    
    result = [1]
    
    for i in range(2, min(int(num**(1/2)) + 1, 1e7)):
        if (num%i):
            continue
        result.append(i)
        if num//i <= 1e7:
            result.append((num // i))
                
    return max(result)

def solution(begin, end):
    answer = []
    for num in range(begin, end+1):
        answer.append(maxdivisor(num))
    return answer
