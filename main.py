# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0

    Updatable = pygame.sprite.Group()
    Drawable = pygame.sprite.Group()
    Asteroids = pygame.sprite.Group()
    Shots = pygame.sprite.Group()
    Player.containers = (Updatable, Drawable)
    Shot.containers = (Drawable, Updatable, Shots)
    Asteroid.containers = (Asteroids, Drawable, Updatable)
    AsteroidField.containers = (Updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    asteroidfield = AsteroidField()

    print("Starting Asteroids!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))

        for obj in Drawable:
            obj.draw(screen)

        Updatable.update(dt)

        for ast in Asteroids:
            if ast.collision(player):
                print("Game over!")
                sys.exit()

            for shot in Shots:
                if ast.collision(shot):
                    ast.split()
                    shot.kill()

        pygame.display.flip()

        Clock.tick(60)
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()
