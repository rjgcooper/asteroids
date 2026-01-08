import sys
import pygame
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    g_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        dt = g_clock.tick(60) / 1000
        #print(f"{dt}")
        

if __name__ == "__main__":
    main()
