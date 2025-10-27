import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    
    # Initialize pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    
    # Create player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Create clock and delta time variables
    clock = pygame.time.Clock()
    dt = 0
    
    # Game loop
    while True:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill("black")
        
        # Draw the player
        player.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Control frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

if __name__ == "__main__":
    main()
