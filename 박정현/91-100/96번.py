'''
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

"십(+)자 뒤집기를 해볼까?"하고 생각했다.

십자 뒤집기는
그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후,
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

'''

def checker_change(tile, x, y):
    '''
    바둑알 뒤집기
    :param tile: 바둑판
    :param x: x좌표
    :param y: y좌표
    :return: 변경된 바둑판
    '''

    for t in range(19):
        tile[x][t] = int(bool(not tile[x][t]))

    for t in range(19):
        tile[t][y] = int(bool(not tile[t][y]))

    return tile

tile = [] # 바둑판

for i in range(19): # 19 * 19 짜리 바둑판 생성
    checkers = list(map(int, input().split()))
    tile.append(checkers)

flip_count = int(input())

for i in range(flip_count): # 뒤집기 횟수만큼 반복
    x, y = list(map(int, input().split()))

    #[10, 12] [10, 12] 이렇게 생김
    tile = checker_change(tile, x-1, y-1)


for i in tile:
    for j in i:
        print(j, end=' ')
    print()
