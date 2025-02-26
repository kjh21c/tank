from datetime import datetime

# 현재 시간 가져오기
now = datetime.now()

# 현재 시간을 보기 좋게 출력
print("현재 시간:", now.strftime("%Y-%m-%d %H:%M:%S"))
