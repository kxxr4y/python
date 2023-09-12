from random import * # Random 일부 기능만 필요한 기능만 불러와서 점유가 낮음
import random # 전체 Random 함수 기능 다 불러 상대적으로 메모리 접유가 높음

rn = random.randrange(1,100+1,1) # 1~100까지의 랜덤 숫자를 생성
print(rn)
num = int(input)

# 서로 비교