import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    
    # Initialize pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set groups as containers for Player
    Player.containers = (updatable, drawable)
    
    # Set groups as containers for Asteroid
    Asteroid.containers = (asteroids, updatable, drawable)
    
    # Set groups as containers for Shot
    Shot.containers = (shots, updatable, drawable)
    
    # Set groups as containers for AsteroidField (only updatable)
    AsteroidField.containers = (updatable,)
    
    # Create player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Create asteroid field
    asteroid_field = AsteroidField()
    
    # Create clock and delta time variables
    clock = pygame.time.Clock()
    dt = 0
    
    # Game loop
    while True:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all updatable objects
        updatable.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return
        
        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.kill()
                    shot.kill()
                    break  # Break inner loop since asteroid is destroyed
        
        # Fill screen with black
        screen.fill("black")
        
        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Control frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()
