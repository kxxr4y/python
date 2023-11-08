# import math # 수학 모듈(함수)를 로드
# from math import sin, cos, tan
# import math as m
# import random as r
import sys
import os

def main():
    # print(math.sin(1))
    # print(math.cos(2))
    # print(math.tan(1))

    # print(math.floor(2.5))
    # print(math.ceil(2.5))

    # s = 2.5

    # if 2.5 >= s:
    #     print(2)
    # else:
    #     print(3)


    # print(sin(1))
    # print(cos(1))
    # print(tan(1))

    # print(m.sin(1))
    # print(m.cos(1))
    # print(m.tan(1))

    # print(r.random()) # 0.0 ~ 1.0 임이의 수를 생성 float
    # print(r.uniform(10,15)) # 10.0 ~ 15.0 사이의 임의의 수를 float
    # print(r.randgrange(10)) # 0 ~ 10 사이의 정수를 반환
    # print(r,randgrange(5,10)) # 5 ~ 9 사이의 정수를 반환
    # print(r.choice([1,2,3,4,5]))

    # abc = ['1','2','3','4','5']
    # r.shuffle(abc)
    # print(abc)

    # print(r.sample([1,2,3,4,5], k=3))

    # print(sys.argv) # 경로를 보는 시스템 함수
    # print(sys.copyright) # 저작권
    # print(sys.version) # 시스템 버전(실행환경 파이썬 포함)

    ### 프로그램 실행중 임의로 강제로 종료 때 쓰는 함수
    # sys.exit() # 임의의 상황에서 프로그램을 강제로 종료 시키는 함수

    # print(os.name)
    # print(os.getcwd()) # 현재 실행 경로
    # print(os.listdir()) # 디렉토리(폴더)내에 있는 파일들을 보는 함수

    # with open("test.txt" , "w") as file: # 파일 생성
    #    file.write("hello")
    # os.rename("test.txr", "new.txt") # 파일 이름변경
    # os.remove("test.txt") # 파일 삭제
    # os.system("dir") # 시스템 명령어 실행
    pass


if __name__ == "__main__":
    main()