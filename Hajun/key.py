import pygame
import sys
import time

def main():
    pygame.init()
    pygame.display.set_caption('첫 번째 Pygame: 키 입력 ')
    screen = pygame.display.set_mode((800, 600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 화면 종룔를 위해서 사용됨
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed() # 실시간으로 key의 입력 변화를 받음
        if key[pygame.K_UP] == 1:print('UP',end=' ')
        if key[pygame.K_DOWN] == 1:print('DOWN',end=' ')
        if key[pygame.K_LEFT] == 1:print('LEFT',end=' ')
        if key[pygame.K_RIGHT] == 1:print('RIGHT',end=' ')
        if key[pygame.K_SPACE] == 1:print('SPACE',end=' ')
        print()
        pygame.display.update()
        pygame.time.Clock().tick(10)

if __name__ == '__main__':
    main()
