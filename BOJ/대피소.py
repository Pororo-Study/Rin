from itertools import combinations

N, K = map(int, input().split())

grid = []
for _ in range(N):
    x, y = map(int, input().split())
    grid.append((x, y))


# 대피소를 설치하는 모든 방법 중
# 가장 가까운 대피소와 집 사이의 거리 중
# 가장 큰 값이 가장 작을 때의 거리
ans = []
for orders in list(combinations(grid, K)):
    turn = []
    for x, y in grid:
        tmp = []
        for nx, ny in orders:
            tmp.append(abs(x-nx) + abs(y-ny))
        turn.append(min(tmp))
    ans.append(max(turn))

print(min(ans))