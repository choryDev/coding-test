# a = [7, 3, 3, 7, 8, 9, 12]
#
# print(a)
#
# a[2] = 4
# print(a)
#



# #리스트 컴프리헨
# a = [i for i in range(50) if i % 2 == 1]
#
# print(a)



# #리스트에서 특정 값을 가지는 원소를 모두 제거하기
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# remove_set = {3, 5}
#
# #remove_list에 포함되지 않은 값만을 저장
# result = [i for i in a if i not in remove_set]
# print(result)


# #딕셔너리
# a = dict()
# a['홍길동'] = 97
# a['이순신'] = 97
#
# print(a)
#
# b = {
#     '홍길동': 97,
#     '이순신': 98,
# }
#
# print(b)



# #집합 자료형의 연산
# #합집합, 교집합, 차집합
#
# data = set([1, 2, 3])
#
# #새로운 원소 추가
# data.add(4)
# print(data)
#
# #새로운 원소 여러개 추가
# data.update([5, 6])
# print(data)
#
# #특정한 값을 갖는 원소 삭제
# data.remove(3)
# print(data)




# #기본 입출력
# # 공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용
# list(map(int, input().split()))
# #공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용합니다.
# a, b, c = map(int, input().split())
#
# #입력을 위한 전형적인 소스코드
# #데이터의 개수 입력
# n = int(input())
# data = list(map(int, input().split()))
#
# print(n)
# print(data)




# #빠르게 입력 받기
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)
#
# #출혁할 변수등
# a = 1
# b = 2
# print(a, b)
# print(7, end=" ")
# print(8, end=" ")
#
# #출력할 변수
# answer = 7
# print("정답은 " + str(answer) + "입니다.")
#




#람다 표현식 예시: 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 70)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

#람다 표현식 예시: 여러개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))


