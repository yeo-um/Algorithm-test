#45분 일찍 알람 설정하기

'''
1. 주어진 시각이 45분 이상인 경우
2-1. 주어진 시각이 45분 미만인 경우
2-2. 시간이 00시인경우
'''

hour , minute = input().split()
hour = int(hour)
minute = int(minute)

if minute>=45:
    print(str(hour)+' '+str(minute-45))
else:
    if hour==0:
        print('23'+' '+str(minute+15))
    else:
        print(str(hour-1)+' '+str(minute+15))