# nums = list(range(1,9+1,1)) # 1부터 9까지 1씩
# print(nums)

# list_a = ["가", "나", "다", "라", "마"]
# for out_list_a in list_a[0:5+1]: # list_a 첫번째부터 다섯번째까지
  # print(out_list_a)

# list_a = [0,1,2,3]
# list_a.append("안녕") # list_a에 추가하기
# print(list_a)

# list_a = [10,20,30,40,50]
# list_a.clear() # 클리어
# print(list_a)

# list_a = [1]
# list_b = [2]
# for list_a_o in list_a: # list_a_o 안에 list_a
  # for list_b_o in list_b: # list_b_o 안에 list_b
    # print(list_a_o)
    # print(list_b_o)
    # print(list_a_o, list_b_o)

# import math
# from math import * # * = 모든
# pi = 3.14152
# print(round(pi,1))

# name_dic = {"name1":"남궁민", "name2":"안은진", "name3":"김동균"}
# for key in name_dic:
  # print(name_dic[key])

# list_a = [0,1,2,3,4,5]
# sum = 0
# for i in range(len(list_a)):
  # sum = sum+i
# print(sum)

# def fn(a, b, c, d, e):
  # print(a, b, c, d, e)
# fn(1,2,3,4,5)

# def hello(msg="안녕하세요"):
  # print(msg + "!")
# hello()

# def fn(a, b=[]):
  # b.append(a)
  # print(b)
# fn(3)

# def sum(*numbers):
  # sum_value = 0
  # for number in numbers:
    # sum_value = sum_value + number
  # return sum_value
# result = sum(1,3)
# print("1 + 3 =", result)
# print("1 + 3 + 5 + 7 =", sum(1,3,5,7))

# with open("basic.txt","w") as file:
  # file.write("Hello")
# with open("basic.txt", "r") as file:
  # contents = file.read()
# print(contents)

# arr = [1, 2, 3]
# try:
  # print(arr[3])
# except:
#  print("리스트의 요소에 접근하지 못했습니다.")