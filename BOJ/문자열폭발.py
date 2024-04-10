bomb = input()
ans = input()
length = len(ans)

stack = []
for char in bomb:
    stack.append(char)
    if ''.join(stack[-length:]) == ans:
        del stack[-length:]

result = ''.join(stack)
if result:
    print(result)
else:
    print('FRULA')
