import random

def __init__(self):

# 게임 초기화
def initialize_game(n):
    board_size = n
    treasure_position = (random.randint(0, n-1), random.randint(0, n-1))
    player_position = (random.randint(0, n-1), random.randint(0, n-1))
    return treasure_position, player_position

# 거리 계산
def calculate_distance(self, treasure_position, player_position):
    return abs(treasure_position[0] - player_position[0]) + abs(treasure_position[1] - player_position[1])

# 플레이어 이동
def move_player(board_size, player_position, direction):
    x, y = player_position
    if direction == 'N':
        x = max(x-1, 0) 
    elif direction == 'S':
        x = min(x+1, board_size-1) 
    elif direction == 'E':
        y = min(y+1, board_size-1)
    elif direction == 'W':
        y = max(y-1, 0)
    return x, y
# 게임 실행
def play_game(board_size):
    treasure_position, player_position = initialize_game(board_size)
    move = 0

    while True:
        print(f'현재 위치 : {player_position}')
        distance = calculate_distance(treasure_position, player_position)
        print(f'보물까지의 거리 : {distance}')
        
        if distance == 0:
            print(f'보물을 찾았습니다!! 이동 횟수 : {move}')
            break
        try:
            direction = input('이동 방향을 선택해주세요 (N, S, E, W)').upper()
            if direction not in ['N', "S", 'E', 'W']:
                raise ValueError('잘못된 값을 입력하셨습니다, N, S, E, W 중에 하나를 입력하세요')
            player_position  = move_player(board_size, player_position, direction)
            move += 1
        except ValueError as e:
            print(e)


# 게임 보드 크기 설정 및 게임 시작
if __name__ == "__main__":
    board_size = 5  
    play_game(board_size)
