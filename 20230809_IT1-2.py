# def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# value = input("값 : ")
# n = int(input("값 : "))

# print_n_times(value, n)

###가변 매개변수

# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print(" ")
# print_n_times(10, "안녕", "하세요", "잘자")

# def print_n_times(value, n=2):
#     for i in range(n):
#         print(value)

# print_n_times("안녕")

###키워드 매개변수
# while True:
#     print("안녕",end="")

# def print_n_times(*values, n=2):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times("안녕하세요", "드럽게 어려운", "파이썬 프로그래밍", n=3)

