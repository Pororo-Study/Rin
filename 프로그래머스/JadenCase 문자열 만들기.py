def solution(s):
    ans = []
    for x in s.split(" "):
        ans.append(x.capitalize())
    return ' '.join(ans)            
            
# capitalize(): 맨 첫글자만 대문자로 변환