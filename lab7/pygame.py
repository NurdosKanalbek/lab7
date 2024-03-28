import pygame
from datetime import datetime as dt

pygame.init()
screen = pygame.display.set_mode((620 , 620))
pygame.display.set_caption("mickey mouse watch")
suret = pygame.image.load(r'C:/Users/kanal/Downloads/WhatsApp Image 2024-03-28 at 10.02.23 PM.jpeg')
suret = pygame.transform.scale(suret, (620, 620)) 
suret2 = pygame.image.load(r'C:/Users/kanal/Downloads/WhatsApp Image 2024-03-28 at 10.02.23 PM (1).jpeg')
suret2 = pygame.transform.scale(suret2, (930,880)) 
suret3 = pygame.image.load(r'C:/Users/kanal/Downloads/WhatsApp Image 2024-03-28 at 10.02.00 PM.jpeg')
suret3 = pygame.transform.scale(suret3, (70,620)) 
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255,255,255))
    screen.blit(suret, (10, 10))

    current_time = dt.now().time()

    seconds_angle = -(current_time.second * 6)
    minutes_angle = -(current_time.minute * 6)

    rotated_leftarm = pygame.transform.rotate(suret3, seconds_angle)
    rotated_rightarm = pygame.transform.rotate(suret2, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center=(310, 310))
    rightarm_rect = rotated_rightarm.get_rect(center=(310, 310))

    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()