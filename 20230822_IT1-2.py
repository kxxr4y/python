# # def fact(n): # 함수명 fact, 임력 값 n
# #     #모든 수에 0을 곱하면 답은 0
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * fact(n-1) # 5! 5x4x3x2x1
    
# # print(fact(5))

# counter = 0

# def fibo(n):
#     print("fibo({})".format(n))
#     global counter # 함수 외부에 선언한 변수에 접근하기 위한 사용
#     counter+=1 # counter = counter + 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# fibo(10)
# print("---경계선---")
# print("피보나치수열 계산에 활용된 덧셈 횟수는 ({})번 입니다.".format(counter))

def flatten(data):
    out = []
    for item in data:
        if type(item) == list: # item 리스트 열때
            out = out+flatten(item) # 재귀함수로 데이터가 계속 입력
        else:
            out.append(item)
    return out

example = [[1, 2, 3], [4, [5, 6]], 7 [8, 9]]
print("원본:", example)
print("변환:", flatten(example))