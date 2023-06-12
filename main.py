import pygame

# Initialize Pygame and set up the game window
pygame.init()
width, height = 1024, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tron Legacy")

# Define player variables
player1_x, player1_y = width // 4, height // 2
player2_x, player2_y = width // 4 * 3, height // 2
player1_color = (0, 255, 0)  # Green
player2_color = (255, 0, 0)  # Red
player1_width = 10
player2_width = 10
player1_direction = "up"
player2_direction = "up"
speed = 0.3
# Define trail variables
trail1 = []
trail2 = []
trail_width = 5
#
diff = 4
diff1, diff2 = player1_width/2, player1_width/2+diff
#
trail_max_length = 1000  # Maximum length of the trails
#
cooldown_counter_1 = 0
cooldown_counter_2 = 0
press_cooldown = 40
#
image = pygame.image
color_check_1 = ()
color_check_2 = ()
#
# Define game over text variables
game_over_font = pygame.font.Font(None, 100)
game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
game_over_text_rect = game_over_text.get_rect(center=(width // 2, height // 2))

player1_font = pygame.font.Font(None, 50)
player1_over_text = player1_font.render("Green Won", True, (0, 255, 0))
player1_over_text_rect = game_over_text.get_rect(center=(width // 2 + 130, height // 2 + 100))

player2_font = pygame.font.Font(None, 50)
player2_over_text = player2_font.render("Red Won", True, (255, 0, 0))
player2_over_text_rect = game_over_text.get_rect(center=(width // 2 + 140, height // 2 + 100))
winner = ""
#

trail1.append((player1_x+diff1, player1_y))
trail2.append((player2_x+diff1, player2_y))

# Game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if game_over:
        # Display "GAME OVER" text
        window.blit(game_over_text, game_over_text_rect)
        if winner == "player 1":
            window.blit(player1_over_text, player1_over_text_rect)
        else:
            window.blit(player2_over_text, player2_over_text_rect)
        pygame.display.update()
        pygame.time.wait(300)

    else:
        if player1_direction == "up":
            player1_y -= speed
            color_check_1 = (0, -player1_width/2)
        elif player1_direction == "right":
            player1_x += speed
            color_check_1 = (player1_width/2+2, 0)
        elif player1_direction == "down":
            player1_y += speed
            color_check_1 = (0, player1_width/2+2)
        elif player1_direction == "left":
            player1_x -= speed
            color_check_1 = (-player1_width/2-2, 0)

        player1_y = round(player1_y,1)
        player1_x = round(player1_x,1)

        if player2_direction == "up":
            player2_y -= speed
            color_check_2 = (0, -player1_width/2)
        elif player2_direction == "right":
            player2_x += speed
            color_check_2 = (player1_width/2+2, 0)
        elif player2_direction == "down":
            player2_y += speed
            color_check_2 = (0, player1_width/2+2)
        elif player2_direction == "left":
            player2_x -= speed
            color_check_2 = (-player1_width/2-2, 0)

        player2_y = round(player2_y, 1)
        player2_x = round(player2_x, 1)

    # Player movement
    if cooldown_counter_1 <= 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1_direction = "up"
            trail1.append((player1_x+diff1, player1_y))
            cooldown_counter_1 = press_cooldown
        elif keys[pygame.K_s]:
            player1_direction = "down"
            trail1.append((player1_x+diff1, player1_y))
            cooldown_counter_1 = press_cooldown
        elif keys[pygame.K_a]:
            player1_direction = "left"
            trail1.append((player1_x+diff1, player1_y))
            cooldown_counter_1 = press_cooldown
        elif keys[pygame.K_d]:
            player1_direction = "right"
            trail1.append((player1_x+diff1, player1_y))
            cooldown_counter_1 = press_cooldown
    #
    cooldown_counter_1 -= 1
    #
    if cooldown_counter_2 <= 0:
        if keys[pygame.K_UP]:
            player2_direction = "up"
            trail2.append((player2_x+diff1, player2_y))
            cooldown_counter_2 = press_cooldown
        elif keys[pygame.K_DOWN]:
            player2_direction = "down"
            trail2.append((player2_x+diff1, player2_y))
            cooldown_counter_2 = press_cooldown
        elif keys[pygame.K_LEFT]:
            player2_direction = "left"
            trail2.append((player2_x+diff1, player2_y))
            cooldown_counter_2 = press_cooldown
        elif keys[pygame.K_RIGHT]:
            player2_direction = "right"
            trail2.append((player2_x+diff1, player2_y))
            cooldown_counter_2 = press_cooldown
    #
    cooldown_counter_2-=1
    #


    # Clear the window
    window.fill((0, 0, 0))

    # Draw players
    pygame.draw.line(window,
                     player1_color,
                     (player1_x, player1_y),
                     (player1_x + player1_width, player1_y),
                     player1_width
                     )

    pygame.draw.line(window,
                     player2_color,
                     (player2_x, player2_y),
                     (player2_x + player2_width, player2_y),
                     player2_width
                     )


    # print(trail1)

    # Draw lines
    trail1.append((player1_x+diff1, player1_y))
    trail2.append((player2_x+diff1, player2_y))

    for i in range(1, len(trail1)):

        pygame.draw.line(
            window,
            player1_color,
            (trail1[i-1][0], trail1[i-1][1]),
            (trail1[i][0], trail1[i][1]),
            trail_width
        )

    for i in range(1, len(trail2)):
        pygame.draw.line(
            window,
            player2_color,
            (trail2[i-1][0], trail2[i-1][1]),
            (trail2[i][0], trail2[i][1]),
            trail_width
        )

    #
    #window.set_at((int(trail1[len(trail1)-1][0]+color_check_1[0]), int(trail1[len(trail1)-1][1]+color_check_1[1])), (255,255,255))
    
    colorX1 = int(trail1[len(trail1)-1][0]+color_check_1[0])
    colorY1 = int(trail1[len(trail1)-1][1]+color_check_1[1])
    if window.get_at((colorX1, colorY1)) != (0, 0, 0):
        game_over = True
        winner = "player 2"
    #
    colorX2 = int(trail2[len(trail2)-1][0]+color_check_2[0])
    colorY2 = int(trail2[len(trail2)-1][1]+color_check_2[1])
    if window.get_at((colorX2, colorY2)) != (0, 0, 0):
        game_over = True
        winner = "player 1"
    #

    trail1.pop()
    trail2.pop()

    # Update the window
    pygame.display.update()

# Quit the game

pygame.quit()



