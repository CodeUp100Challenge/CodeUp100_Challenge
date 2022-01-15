'''
단어와 반복 횟수를 입력받아 여러 번 출력해보자.
'''

'''
(송시무 의식의 흐름)
단어와 반복 횟수를 입력 받는다
word는 출력할 대상이고, numberOfRepeat는 반복 횟수다
반복 횟수만큼 출력을 반복한다.
내장함수가 존재할 것 같다. 그 함수를 모르니까 내가 만들어보자. 반복문을 쓰면 될 것 같다.

word, numberOfRepeat = input().split()
numberOfRepeat = int(numberOfRepeat)
for _ in range(numberOfRepeat):
    print(word)

안타깝다. 특강 때 배운 range 함수를 이용한 반복문을 응용해봤는데 틀렸다.
문제에서 요구하는 건 단어 출력이 가로로 연달아 되어야 하는데 내가 짠 코드는 세로로 출력된다. 
힌트를 참고해보자.

예시
w, n = input().split()
print(w*int(n))

참고
문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.

개간단하다. 귀도 짱. 
변수명을 직관적으로 알아볼 수 있게 단어 그대로 쓰고 있는데 다 짜고 보니 뭔가 지저분하다.
조금 더 깔끔했음 좋겠다.
'''


word, numberOfRepeat = input().split()
numberOfRepeat = int(numberOfRepeat)
print(word*numberOfRepeat)