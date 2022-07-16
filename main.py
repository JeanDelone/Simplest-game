import sys
import pygame
from tale import *
from pygame.locals import *
import random

pygame.init()
pygame.display.set_caption("Simplest game")
font = pygame.font.Font(None, 50)
score = 100

fps = 30
clock = pygame.time.Clock()

width, height = 1600, 900
screen = pygame.display.set_mode((width, height))

normal_tale = Tale((LIGHT_GRAY))
player_tale = Tale(WHITE_2, is_player=True, x = 1450, y = 750)
victorious_tale = Tale((0,255,121), is_victory = True, x = 100, y = 100)

# tales_list becomes 2D array of tales
tales_list = []
for i in range(int(width / normal_tale.width)):
    tales_list.append([])
    for j in range(int(height / normal_tale.height)):
        if i == 0 or i == (width / normal_tale.width) - 1 or j == 0 or j == (height / normal_tale.height) - 1:
            tales_list[i].append(Tale(DARK_GREY, is_solid = True, x = i * normal_tale.width, y = j * normal_tale.height))
        else:
            tales_list[i].append(Tale((50+(j*3),50+(j*3),50+(j*3)), x = i * normal_tale.width, y = j * normal_tale.height))

# Create X amount of random obsticles on map, so every game is slightly different. There always will be room to move on the edge so it's always possible to complete map
random_obsticles = 100
for i in range(random_obsticles):
    random_row = random.randint(2, int(width / normal_tale.width) - 2)
    random_col = random.randint(2, int(height / normal_tale.height) - 2)
    while tales_list[random_row + 1][random_col].is_solid == True or tales_list[random_row - 1][random_col].is_solid == True or tales_list[random_row][random_col + 1].is_solid == True or tales_list[random_row][random_col - 1].is_solid == True or tales_list[random_row][random_col].is_solid == True:
        random_row = random.randint(2, int(width / normal_tale.width) - 2)
        random_col = random.randint(2, int(height / normal_tale.height) - 2)
    tales_list[random_row][random_col] = (Tale(DARK_GREY, is_solid = True, x = random_row * normal_tale.width, y = random_col * normal_tale.height))

tales_list[29][15] = player_tale
tales_list[2][2] = victorious_tale

def display_score():
    score_surf = font.render(f"Score: {score}", False, (255,255,255))
    screen.blit(score_surf,(25,5))

# Checks if player can move further, if there is no possible move, game ends and player gets 0 points
def no_possible_move():
    if tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height) - 1].is_solid == True and tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height) + 1].is_solid == True and tales_list[int(player_tale.x / player_tale.width) - 1][int(player_tale.y / player_tale.height)].is_solid == True and tales_list[int(player_tale.x / player_tale.width) + 1][int(player_tale.y / player_tale.height)].is_solid == True:
        score = 0
        print(f"No possible moves left, score: {score}")
        return True
    if tales_list[2][3].is_solid == True and tales_list[3][2].is_solid == True and tales_list[2][1].is_solid == True and tales_list[1][2].is_solid == True:
        score = 0
        print(f"Cannot acces victorious tale anymore, score: {score}")
        return True

for row in tales_list:
    for item in row:
        pygame.draw.rect(screen, item.color, (item.x, item.y, item.width, item.height))

# Game loop.
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # First check if move is possible, so if tale that player wants to go is not solid
                if not tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height) - 1].is_solid:
                    # Tale that player wants to move is becoming player's tale
                    tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height) - 1] = player_tale
                    # Tale that player was just at is becoming visited tale
                    tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height)] = Tale(WHITE_1, is_solid = True, x = player_tale.x, y = player_tale.y)
                    player_tale.y -= 50
                    score -= 1
            elif event.key == pygame.K_s:
                # Same proccess as above
                if not tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height) + 1].is_solid:
                    tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height) + 1] = player_tale
                    tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height)] = Tale(WHITE_1, is_solid = True, x = player_tale.x, y = player_tale.y)
                    player_tale.y += 50
                    score -= 1
            elif event.key == pygame.K_a:
                if not tales_list[int(player_tale.x / player_tale.width) - 1][int(player_tale.y / player_tale.height)].is_solid:
                    tales_list[int(player_tale.x / player_tale.width) - 1][int(player_tale.y / player_tale.height)] = player_tale
                    tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height)] = Tale(WHITE_1, is_solid = True, x = player_tale.x, y = player_tale.y)
                    player_tale.x -= 50
                    score -= 1
            elif event.key == pygame.K_d:
                if not tales_list[int(player_tale.x / player_tale.width) + 1][int(player_tale.y / player_tale.height)].is_solid:
                    tales_list[int(player_tale.x / player_tale.width) + 1][int(player_tale.y / player_tale.height)] = player_tale
                    tales_list[int(player_tale.x / player_tale.width)][int(player_tale.y / player_tale.height)] = Tale(WHITE_1, is_solid = True, x = player_tale.x, y = player_tale.y)
                    player_tale.x += 50
                    score -= 1

            for row in tales_list:
                for item in row:
                    pygame.draw.rect(screen, item.color, (item.x, item.y, item.width, item.height))
            display_score()


    if not tales_list[2][2] == victorious_tale:
        print(f"Score: {score}")
        break

    if no_possible_move():
        break
    pygame.display.flip()
    clock.tick(fps)