'''
로또 순위 매기는 방법

등수	방법
1등	당첨번호 6개 일치
2등	당첨번호 5개 일치 + 보너스번호 일치
3등	5개 번호 일치
4등	4개 번호 일치
5등	3개 번호 일치
꽝	2개 이하 일치


예)
13 23 24 35 40 45 7     ===> 로또 당첨번호 + 보너스 번호
 2  6  7 23  40 44      ====> 지혜가 가진 로또 번호
따러서 지혜는 "꽝"
'''

lotto_target = (list(map(str, input().split())))
lotto_train = (list(map(str, input().split())))
target_count = 0

for i in range(0, len(lotto_target)-1):
    if lotto_target[i] in lotto_train:
        target_count += 1
if lotto_target[-1] in lotto_train:
    target_count += 0.5

if target_count >= 6:
    print(1)
elif target_count >= 5.5:
    print(2)
elif target_count >= 5:
    print(3)
elif target_count >= 4:
    print(4)
elif target_count >= 3:
    print(5)
else:
    print(0)