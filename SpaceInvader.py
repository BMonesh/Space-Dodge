import pygame
import sys
import random

pygame.init()# Initialize Pygame

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

player_size = 50
player_speed = 5
player = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT - 2 * player_size, player_size, player_size)

bullet_speed = 7
bullets = []

alien_size = 50
alien_speed = 2
aliens = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - player_speed > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x + player_size + player_speed < WIDTH:
        player.x += player_speed

    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    if random.randint(1, 100) < 2:
        aliens.append(pygame.Rect(random.randint(0, WIDTH - alien_size), 0, alien_size, alien_size))

    for alien in aliens:
        alien.y += alien_speed
        if alien.colliderect(player):
            pygame.quit()
            sys.exit()

    for bullet in bullets:
        for alien in aliens:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    for alien in aliens:
        pygame.draw.rect(screen, RED, alien)

    pygame.display.flip()
    clock.tick(FPS)
