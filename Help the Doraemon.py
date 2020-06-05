import pygame
import random
import sys  

pygame.init()

pygame.display.set_caption('Help the Doraemon')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

pygame.mixer.init()
pygame.mixer.music.load('unbelivable.mp3')
pygame.mixer.music.play()

WIDTH = 840
HEIGHT = 600
RED = (255,0,0)
YELLOW = (0, 0, 0)
BLUE = (0,0,255)
BACKGROUND_COLOR = (255, 105, 13)

player_size = 60
player_pos = ([WIDTH / 2, HEIGHT - 1.6 * player_size])

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

enemy_size = 40
enemy_pos = [random.randint(0, WIDTH - enemy_size),0]
enemy_list = [enemy_pos]

SPEED = 1


screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0
img = pygame.image.load('icon.png')

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
	if score < 20:
		SPEED = 10
	elif  score >= 20 and score < 30:
		SPEED = 11
	elif  score >= 30 and score < 40:
		SPEED = 12
	elif  score >= 40 and score < 50:
		SPEED = 13
	elif  score >= 50 and score < 60:
		SPEED = 14
	elif  score >= 60 and score < 70:
		SPEED = 15
	elif  score >= 70 and score < 80:
		SPEED = 16
	elif  score >= 80 and score < 90:
		SPEED = 17
	elif  score >= 90 and score < 100:
		SPEED = 18
	elif  score >= 100 and score < 105:
		SPEED = 19
	elif  score >= 105 and score < 110:
		SPEED = 20
	elif  score >= 110 and score < 115:
		SPEED = 21
	elif  score >= 115 and score < 120:
		SPEED = 22
	elif  score >= 120 and score < 125:
		SPEED = 23
	elif  score >= 125 and score < 130:
		SPEED = 24
	else:
		SPEED = 25
	return SPEED

def set_size(score, enemy_size):
	if score >= 70:
		enemy_size = 55
	return enemy_size

def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 15 and delay < .1:
		x_pos = random.randint(0, WIDTH - enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		ig = pygame.image.load('rat.png')
		ig = pygame.transform.scale(ig, (enemy_size, enemy_size))
		display_surface.blit(ig, (enemy_pos[0], enemy_pos[1]))

def update_enemy_positions(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED

		else:
			enemy_list.pop(idx)
			score += 1
	return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True
	return False

while not game_over:

	for event in pygame.event.get():

		# if event.type == pygame.QUIT:
		# 	sys.exit()

		if event.type == pygame.KEYDOWN:
			
			x = player_pos[0]
			y = player_pos[1]
			
			if event.key == pygame.K_LEFT and player_pos[0] > 0:
				x -= player_size
				img = pygame.image.load('doraemon2.png')

			elif event.key == pygame.K_RIGHT and player_pos[0] < WIDTH - player_size:
				x += player_size
				img = pygame.image.load('doraemon1.png')


			player_pos = [x, y]

	screen.fill(BACKGROUND_COLOR)

	
	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	SPEED = set_level(score, SPEED)
	enemy_size = set_size(score, enemy_size)

	text = "Score : " + str(score) + "    "
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH - 250, HEIGHT - 40))

	if collision_check(enemy_list, player_pos):
		game_over = True

	if game_over:
		screen = pygame.display.set_mode((WIDTH, HEIGHT))
		txt = "Score : " + str(score) + "    "
		lbl = myFont.render(txt, 1, BACKGROUND_COLOR)
		screen.blit(lbl, (0, 0))
		print(txt)

	draw_enemies(enemy_list)
	
	img = pygame.transform.scale(img, (player_size, player_size))
	display_surface.blit(img, (player_pos[0], player_pos[1]))
	clock.tick(30)

	pygame.display.update()
	print(score)