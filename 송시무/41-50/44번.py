'''
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단 0 <= a, b <= 2147483647, b는 0이 아니다.

첫 번째 줄에 합
두 번째 줄에 차,
세 번째 줄에 곱,
네 번째 줄에 몫,
다섯 번째 줄에 나머지,
여섯 번째 줄에 나눈 값을 순서대로 출력한다.
(실수, 소수점 이하 둘째 자리까지의 정확도로 출력)
'''

a, b = input().split(' ')
a = int(a)
b = int(b)
sum = a + b
sub = a - b
mul = a*b
quo = a//b
rem = a%b
div = a/b

print(sum)
print(sub)
print(mul)
print(quo)
print(rem)
print(format(div,".2f"))

