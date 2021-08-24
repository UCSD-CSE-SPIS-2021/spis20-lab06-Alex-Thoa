import pygame

import os

 

# These are the dimensions of the background image for our game

screen_length = 600

screen_height = 427 

dim_field = (screen_length, screen_height)


screen = pygame.display.set_mode(dim_field)

background = pygame.image.load(os.path.join("assets","background.jpg"))

background = pygame.transform.scale(background, dim_field)

player = pygame.image.load(os.path.join("assets", "player.png")).convert()

player.set_colorkey((101, 141, 209))

winningflag = pygame.image.load(os.path.join("assets", "flag.png"))
# Location 1

x = 200
y = 200
playerWidth = 24
playerHeight = 26
rect_player = pygame.Rect(x, y, playerWidth, playerHeight)
platform1Width = 200
platform1Height = 10
rect_platform1 = pygame.Rect(x + 50, y + 170, platform1Width, platform1Height)
floorWidth = 600
floorHeight = 10
rect_floor = pygame.Rect(x - 200, y + 223, floorWidth, floorHeight)
platform_list = [ rect_platform1, rect_floor ]

step_size = 12
step_size_fall = 6

# Game Loop

FPS = 60 

running = True

clock = pygame.time.Clock()

while running:
    
    clock.tick(FPS)

        # Processing events
    for event in pygame.event.get():
      # Quit game
      if event.type == pygame.KEYDOWN: 

        if event.key == pygame.K_q:
            
            running = False

        # if event.key == pygame.K_LEFT:

             # rect_player.move_ip(-step_size, 0)
             
        # if event.key == pygame.K_RIGHT:

             # rect_player.move_ip(step_size, 0)
             
        # if event.key == pygame.K_UP:

             # rect_player.move_ip(0,-step_size)

        # if event.key == pygame.K_DOWN:

             # rect_player.move_ip(0,step_size)
    
    keys = pygame.key.get_pressed()

    index = rect_player.collidelist(platform_list)

    if keys[pygame.K_LEFT]:

        rect_player.move_ip(-step_size, 0)

    if keys[pygame.K_RIGHT]:

        rect_player.move_ip(step_size, 0)

    if keys[pygame.K_UP]:

        rect_player.move_ip(0, -step_size)

    # if keys[pygame.K_DOWN]:

        # rect_player.move_ip(0, step_size)

    if rect_player.left < screen_length - screen_length:

        rect_player.left = screen_length - screen_length

    if rect_player.right > screen_length:

        rect_player.right = screen_length

    if rect_player.top < screen_height - screen_height:

        rect_player.top = screen_height - screen_height

    if rect_player.bottom > screen_height:

        rect_player.bottom = screen_height

    if index == -1:

        rect_player.move_ip(0, step_size_fall)

	# move the rect_player to the left by step_size
	# move the rect_player to the left by step_size
        

    screen.blit(background, (0,0))

    pygame.draw.rect(screen, (0,0,255), rect_platform1) 

    pygame.draw.rect(screen, (255, 0, 0), rect_floor)

    #pygame.draw.rect(rect_floor, rect_platform1)
    screen.blit(player, rect_player)

    pygame.display.update ()
