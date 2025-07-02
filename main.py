import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(x, y)

    while True:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            shot = player.shoot()
            if shot != None:
                updatable.add(shot)
                drawable.add(shot)

        updatable.update(dt)

        for asteroid_obj in asteroids:
            for bullet_obj in shots:
                if asteroid_obj.collision(bullet_obj):
                    asteroid_obj.split()
                    bullet_obj.kill()

        for item in asteroids:
            if player.collision(item):
                sys.exit("Game Over!")

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(144))/1000


if __name__ == "__main__":
    main()
