'''
정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.
'''

a, b = input().split()
a = int(a)
b = int(b)
print(a-b)

'''
모범풀이
a, b = input().split()
c = int(a)-int(b)
print(c)

(송시무 의식의 흐름)
이게 좀 더 깔끔하네
형변환 할 때 굳이 변수에 또 대입할 필요 없이 바로 int(a) 꼴로 쓸 수 있음. HTML 표현식(?)(<%= %>) 같다.
'''