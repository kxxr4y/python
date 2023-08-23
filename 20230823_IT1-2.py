# tuple_test = (10, 20, 30)

# print(tuple_test[0])
# print(tuple_test[1])
# print(tuple_test[2])

# [a, b] = [10, 20]
# (c, d) = (10, 20)

# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("d:", d)

# # 괄호가 없는 튜플
# tuple_test = 10, 20, 30, 40
# print("# 괄호가 없는 튜플의 값과 자료형 출력")
# print("tuple_test:", tuple_test)
# print("type(tupletest:)", type(tuple_test))
# print()

# # 괄호가 없는 튜플 활용
# a, b, c = 10, 20, 30
# print("# 괄호가 없는 튜플을 활용한 할당")
# print("a:", a)
# print("b:", b)
# print("c:", c)

# ### 활용 예시 - 변수의 값을 교환하는 튜플
# a,b = 10, 20
# print("# 교환 전 값")
# print("a:", a)
# print("b:", b)
# print()

# # 값을 교환합니다.
# a, b = b, a

# print("# 교환 후 값")
# print("a:", a)
# print("b:", b)
# print()

# ### 튜플과 함수
# # 함수 선언
# def test():
#     return (10, 20)

# #여러 개의 값을 리턴받습니다.
# a, b = test()

# # 출력
# print("a:", a)
# print("b:", b)

# ### 람다(lamda)
# def call_10_times(func):
#     for i in range(10):
#         func()

# def print_hello():
#     print("안녕하세요")

# call_10_times(print_hello)

# numbers= [1, 2, 3, 4, 5, 6]
# print("::".join(map(str,numbers)))

numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x%2, numbers)))

print("# 3 이상, 7미만 추출하기")
print(list(filter(lambda x: 3<=x<7, numbers)))

print("# 제곱")
print(list(filter(lambda x:x**2, numbers)))