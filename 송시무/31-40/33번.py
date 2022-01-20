'''
<문제>
문자 1개를 입력받아 그 다음 문자를 출력해보자.
영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.
'''
'''
(송시무 의식의 흐름)
문자를 입력받아
문자는 순서표가 존재해. 그 순서표에서 다음 문자가 뭔지 찾아
그 문자를 출력해

순서표 = 아스키코드표(?) 유니코드표(?) ord()는 유니코드표 기준(?)

ord() : 문자->정수값, chr() : 정수값->문자
내가 짠 대로 돌아가니까 쾌감 개지린다.
아래에 모범코드랑 참고내용 첨부
'''

character = int(ord(input()))
character += 1
print(chr(character))

'''
참고
숫자는 수를 표현하는 문자로서 '0' 은 문자 그 자체를 의미하고, 0은 값을 의미한다.

힌트
아스키문자표에서 'A'는 10진수 65로 저장되고 'B'는 10진수 66으로 저장된다.
따라서, 문자도 값으로 덧셈을 할 수 있다. 어떤 문자의 값에 1을 더하면 그 다음 문자의 값이 된다.

모범코드
n1=input()
n2=ord(n1)+1
s=chr(n2)
print(s)
'''
