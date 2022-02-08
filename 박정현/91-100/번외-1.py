'''
우리는 숫자를 int나 long long으로 숫자를 처리하였다.

이번엔 그보다 더 큰 숫자를 비교해보자.

최대 100자리의 두 숫자가 입력되면 작은수와 큰 수를 차례대로 출력하시오.
'''

a, b = list(map(int, input().split()))

print(min(a, b), max(a, b))