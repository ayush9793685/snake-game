import pygame
import random
from pygame.locals import *

pygame.init()

width, height = 800, 600
frame_width,frame_height=1010,600
WIN = pygame.display.set_mode((frame_width, frame_height))
pygame.display.set_caption("Snake Game")
count2=0
h_count=0
def program(count2,h_count,width,height):
    sn=0



    BLACK=(0,0,0)
    green = (0, 255, 0)
    BLUE = (0,0,255)
    grey=(215, 213, 255)


    # Define the snake's initial position and size
    snake_size = 25
    snake_x = width // 2
    snake_y = height // 2

    # Define the snake's movement speed
    snake_dx = 0
    snake_dy = 0

    # Define the apple's initial position
    apple_x = random.randint(30,width-30)
    apple_y = random.randint(30,height-30)


    #no of times appe eaten
    count=0
    

    # Set up the clock
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_dx = 0
                    snake_dy = -snake_size
                    sn=1
                elif event.key == pygame.K_DOWN:
                    snake_dx = 0
                    snake_dy = snake_size
                    sn=2
                elif event.key == pygame.K_LEFT:
                    snake_dx = -snake_size
                    snake_dy = 0
                    sn=3
                elif event.key == pygame.K_RIGHT:
                    snake_dx = snake_size
                    snake_dy = 0
                    sn=4

        # Update snake's position
        snake_x += snake_dx
        snake_y += snake_dy

        if count2>h_count:
            h_count=count2
        
        # Check if the snake hits the boundaries
        if snake_x < 20 or snake_x >= width-30 or snake_y < 20 or snake_y >= height-30:
            running = False
            count2=count
            program(count2,h_count,width,height)

        # Check if the snake eats the apple
        for i in range(apple_x-15,apple_x+15):
            for j in range(apple_y-15,apple_y+15):
                if snake_x == i and snake_y==j:
                    count=count+1
                    apple_x = random.randint(20,width-30)
                    apple_y = random.randint(20,height-30)

        # Clear the screen
        WIN.fill(green)
        image2 = pygame.image.load("C:/Users/ayush/Downloads/gamebg.png")
        image2=pygame.transform.scale(image2,(width,height))
        WIN.blit(image2, (0,0))

        # Draw the snake and apple
        pygame.draw.rect(WIN, BLUE, (snake_x, snake_y, snake_size, snake_size))
        pygame.draw.rect(WIN,grey, (width, 0, 210, height))
        image = pygame.image.load('C:/Users/ayush/Downloads/apple.png')
        image=pygame.transform.scale(image,(20,21))
        WIN.blit(image, (apple_x,apple_y))
        '''
        if sn==1:
            image_s_up = pygame.image.load('C:/Users/ayush/OneDrive/Documents/lib/snakeup.png')
            image_s_up = pygame.transform.scale(image_s_up,(20,21))
            WIN.blit(image_s_up, (snake_x,snake_y))
        elif sn==2:
            image_s_down = pygame.image.load('C:/Users/ayush/OneDrive/Documents/lib/snakedown.png')
            image_s_down = pygame.transform.scale(image_s_down,(20,21))
            WIN.blit(image_s_down, (snake_x,snake_y))
        elif sn==3:
            image_s_left = pygame.image.load('C:/Users/ayush/OneDrive/Documents/lib/snakeleft.png')
            image_s_left = pygame.transform.scale(image_s_left,(20,21))
            WIN.blit(image_s_left, (snake_x,snake_y))
        elif sn==4:
            image_s_right = pygame.image.load('C:/Users/ayush/OneDrive/Documents/lib/snakeright.png')
            image_s_right = pygame.transform.scale(image_s_right,(20,21))
            WIN.blit(image_s_right, (snake_x,snake_y))
        elif sn==0:
            image_s_left = pygame.image.load('C:/Users/ayush/OneDrive/Documents/lib/snakeleft.png')
            image_s_left = pygame.transform.scale(image_s_left,(20,21))
            WIN.blit(image_s_left, (snake_x,snake_y))

        '''
        font = pygame.font.Font(None, 36)

        # Render the text
        text = font.render("score = "+str(count),True, BLACK)

        # Blit the text onto the screen
        x, y = width+10, 50
        WIN.blit(text, (x, y))

        text2=font.render("last score = "+str(count2),True,BLACK)
        x,y=width+10,100
        WIN.blit(text2,(x,y))

        text2=font.render("high score = "+str(h_count),True,BLACK)
        x,y=width+10,150
        WIN.blit(text2,(x,y))
        # Update the display
        pygame.display.update()
        if running==True:
            # Limit the game's FPS
            clock.tick(10)
            
    
program(count2,h_count,width,height)
# Quit the game
pygame.quit()