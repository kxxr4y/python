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

print_n_times("안녕")