'''
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단 0 <= a, b <= 2147483647, b는 0이 아니다.
'''

a, b = list(map(int, input().split()))
sum = a+b
sub = a-b
mul = a*b
r = a%b

q = format(a/b, ".2f")
print(f"{sum}\n{sub}\n{mul}\n{a//b}\n{r}\n{q}")