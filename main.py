# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


# pygame inits
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = ()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    dt = 0
    # done defining things
    print(
        f"Starting asteroids!\n"
        f"Screen width: {SCREEN_WIDTH}\n"
        f"Screen height: {SCREEN_HEIGHT}"
    )

    # draw black background
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        #screen draw bullshit
        screen.fill("black") # fill screen
        for d in drawable: # draw
            d.draw(screen)
        for u in updatable: # update
            u.update(dt)
        for a in asteroids:
            if a.collides_with(player):
                print("Game Over")
                sys.exit()
        pygame.display.flip() # refresh screen
        dt = clock.tick(60) / 1000 # limit framerate to 60 FPS








if __name__ == "__main__":
    main()