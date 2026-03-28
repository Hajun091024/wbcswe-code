import pygame

def main():
    pygame.init()
    while True:
        pygame.time.Clock().tick(10)
        # fps 초당 몇번의 이미지를 나타내어 주는지에 대한 척도, 속도도 달라짐
        # 예) 1번이도하는데 10만큼 이동하고 1초에 10번 동작하면 1초에 100만큼 이동한다

