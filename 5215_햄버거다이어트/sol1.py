# sol2.py 에서 개선
# 0-1 Knapsack 알고리즘과 관련있음.
import sys

sys.stdin = open("input.txt")


# 햄버거 조합 함수 hamburger
def hamburger(n, k, point, calorie):
    global max_point
    # 칼로리가 제한을 넘었다면 백트래킹
    if calorie > L:
        return
    # 마지막 재료까지 확인했다면 점수 확인 후 max_point 갱신
    if n == k:
        if point > max_point:
            max_point = point
            return
    else:
        # 재료 넣고 다음 재료 확인
        hamburger(n+1, k, point + Ts[n], calorie + Ks[n])
        # 재료 넣지 않고 다음 재료 확인
        hamburger(n+1, k, point, calorie)

T = int(input())
for tc in range(1, T + 1):
    # 재료의 수 N, 칼로리 제한 L
    N, L = map(int, input().split())
    # 재료의 맛점수 T 의 리스트 Ts, 칼로리 K의 리스트 Ks
    Ts = []
    Ks = []
    for _ in range(N):
        T, K = map(int, input().split())
        Ts.append(T)
        Ks.append(K)
    max_point = 0
    # 햄버거 만들기
    point = 0
    calorie = 0
    hamburger(0, N, point, calorie)
    print("#{} {}".format(tc, max_point))

