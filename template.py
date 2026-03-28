import pygame

pygame.init()
screen = pygame.display.set_mode((360, 480))
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
