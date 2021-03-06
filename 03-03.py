# #1이 될 때까지
#
# #n, k을 공백을 기준으로 구분하여 입력 받기
# n, k = map(int, input().split())
#
# result = 0
#
# while True:
#     #n이 k로 나누어 떨어지는 수가 될 떄까지만 1씩 빼기
#     target = (n//k) * k
#     print(target)
#     result += (n-target)
#     n = target
#     #n이 k보다 작을 때(더이상 나눌 수 없을 때) 반복문 탈춣
#     if n < k:
#         break
#     #k로 나누기
#     result += 1
#     n //= k
#
# #마지막으로 남은 수에 대하여 1씩 뺴기
# result += (n - 1)
# print(result)
#
#
#
#
#곱하기 혹은 더하기: 답안예시
# data = input()
#
# #첫 번쨰 문자를 숫자로 변경하여 대입
# result = int(data[0])
#
# for i in range(1, len(data)):
#     #두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
#
# print(result)



# #시각: 문제 설명
#
# #H 입력 받기
#
# count = 0
#
# # H 입력 받기
# h = int(input())
#
# count = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
#
# print(count)





#상하좌우: 답안 예시

# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)


