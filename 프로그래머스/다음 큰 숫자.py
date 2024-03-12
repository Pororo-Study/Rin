def check(x):
    binary = bin(x)
    one = binary.count('1')
    return one 

def solution(n):
    ans = n
    binary_n = check(n)
    while True:
        ans += 1
        if check(ans) == binary_n:
            return ans