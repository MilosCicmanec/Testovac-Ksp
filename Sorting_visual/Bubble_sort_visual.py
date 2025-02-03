import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
width = 1500
height = 900 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bubble sort")  # Set window title

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Variable to control the game loop
running = True

# Define a class for the blocks used in visualization
class Block:
    def __init__(self, value, x, colour):
        self.value = value  # Height of the block (determines its value in sorting)
        self.x = x  # X-coordinate position of the block
        self.colour = colour  # Color of the block
    
    def draw_self(self):    
        # Draw a rectangle representing the block
        pygame.draw.rect(screen, self.colour, (self.x, self.value, 13, height - self.value))

# Create a list of blocks with random heights
blocks = []
for i in range(0, width + 1, width // 100):
    blocks.append(Block(random.randint(1, 850), i, green))

# Flag to check if sorting is completed
sorted = False    

# Main game loop
while running:
    # Bubble Sort Algorithm Visualization
    while not sorted:
        sorted = True  # Assume the array is sorted
        
        for i in range(len(blocks) - 1):
            b1 = blocks[i]
            b2 = blocks[i + 1]
            
            # Highlight the blocks being compared
            b1.colour = red
            b2.colour = red
            
            # Clear the screen before redrawing
            screen.fill(black)
            
            # Draw all blocks
            for block in blocks:
                block.draw_self()
            
            # Update the display
            pygame.display.flip()
            
            # Swap blocks if they are out of order
            if b1.value > b2.value:
                b1.value, b2.value = b2.value, b1.value
                sorted = False  # If a swap happens, array is not yet sorted
            
            # Reset block colors back to green
            b1.colour = green
            b2.colour = green
            
            # Check for quit event to allow user to exit while sorting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sorted = True  # Stop sorting if quitting
                    break
    
    # Small delay after sorting completes
    pygame.time.delay(50)
    
    # Exit the loop when sorting is done
    if sorted:
        break        
    
    # Check for quit event in the main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.time.delay(10)

# Quit pygame when the loop ends
pygame.quit()
