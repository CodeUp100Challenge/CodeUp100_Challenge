'''
개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.


개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
'''
def maze_printer(maze):
    '''
    미로 출력
    :param maze: 미로
    '''
    for i in maze:
        for j in i:
            print(j, end=' ')
        print()

maze = []

for i in range(10):
    maze.append(list(map(str, input().split())))

x, y = 1, 1
maze[x][y] = '9' # 시작점
while True:
    if maze[x][y+1] == '0': # 오른쪽 가능
        y += 1
        maze[x][y] = '9' # 움직인 표시
    elif maze[x+1][y] == '0': # 아래쪽 가능
        x += 1
        maze[x][y] = '9' # 움직인 표시
    elif maze[x+1][y] == '2':
        maze[x+1][y] = '9'
    elif maze[x][y+1] == '2':
        maze[x][y+1] = '9'

    else:
        maze_printer(maze)
        break
