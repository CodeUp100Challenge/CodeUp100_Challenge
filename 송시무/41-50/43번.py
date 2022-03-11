'''
실수 2개(f1, f2)를 입력받아
f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.
'''

f1, f2 = input().split(' ')
f1 = float(f1)
f2 = float(f2)
print(format(f1/f2,".3f"))


'''
참고
python 언어에는 나눗셈(division)을 계산하는 연산자(/)가 있다.

컴퓨터 프로그래밍에서 실수 변환이나 실수를 사용하는 계산은 
정확하게 변환되거나 계산되는 것이 아니라, 거의 모두 근사값으로 계산되는 것이라고 할 수 있다.  

실수가 컴퓨터로 저장되기 위해서는 디지털방식으로 2진 정수화되어 저장되어야 하는데, 
그 과정에서 아주 작은 부분이 저장되지 않고 사라지는 잘림(truncation) 오차가 자주 발생하기 때문이다.

계산 결과값 중에서 믿을 수 있는 숫자의 개수를 의미하는, 유효숫자에 대해 찾아보자. 
과학실험에서 온도나 부피를 측정할 때에도 유효숫자는 중요하다. 
'''