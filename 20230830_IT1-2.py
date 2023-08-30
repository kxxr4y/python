### 구분오류 - 프로그램 실행 전에 발생하는 오류

# 프로그램 시작
# print("# 프로그램이 시작되었습니다!")
# 구분 오류 발생 코드
# print("#예외를 강제로 발생시켜 볼게요!") # 닫은 따음표로 문자열을 닫지않으면 발생

# ## 런타임오류 - 실행중에 발생하는 오류
# print("#프로그램이 시작되었습니다!") # 프로그램 시작ㄴ
# list_a[1] # 예외 발생 코드

# ## 해결방법
# print("#프로그램이 시작되었습니다!") # 프로그램 시작
# list_a = [1, 2, 3, 4, 5] 
# list_a[1] # 에러 메세지에서 정의하지 않았다고 하니 정의해 줍니다.

# ## 기본 예외 처리 - 조건문으로 예외 처리하기
# # 위 슬라이드의 경우 isdigit() 함수 사용하여 숫자로만 구성된 글자인지 확인
#user_input_a = int("정수입력> ") # 숫자를 입력합니다.

#if user_input_a.isdigit(): # 사용자 입력이 숫자로만 구성되어 있을 때
    #number_input_a = int(user_input_a) # 숫자로 변환합니다.

   # print("원의 반지름:", number_input_a) # 출력합니다.
  #  print("원의 둘레:", 2 * 3.14 * number_input_a)
  #  print("원의 넓이:", 3.14 * number_input_a * number_input_a)
#else:/
 #   print/("정수를 입력하지 않았습니다.")

### try except 구문

# try except 구문으로 예외를 처리합니다.
# try:
    # 숫자로 변환
    # number_input_a = int(input("정수 입력> ")) # 예외가 발생할 가능성이 있는 구문
    # 출력
    # print("원의 반지름:", number_input_a)
    # print("원의 둘레:", 2 * 3.14 * number_input_a)
    # print("원의 넓이:", 3.14 * number_input_a *number_input_a)
# except:
    # print("무언가 잘못되었습니다.") # 예외가 발생했을 떄 실행할 구문