def solution(s):
    s = list(map(int, s.split()))
    s.sort()
    s = list(map(str, s))
    return (s[0]+' '+s[-1])