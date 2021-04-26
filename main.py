import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TIC TAC TOE')

#Variables
grid_size = 200
player1 = 'X'
player2 = 'O'
game_state = True
game_winner = ''

x_color = (255, 255, 255)
o_color = (255, 255, 255)

current_player = random.choice([player1, player2])

#Matrix
matrix = [
	['', '', ''],
	['', '', ''],
	['', '', '']

]

def draw_grid():
	pygame.draw.line(screen, (255, 255, 255), (grid_size * 1 - 4, 15), (grid_size * 1 - 4, SCREEN_HEIGHT - 15), 8)
	pygame.draw.line(screen, (255, 255, 255), (grid_size * 2 - 4, 15), (grid_size * 2 - 4, SCREEN_HEIGHT - 15), 8)

	pygame.draw.line(screen, (255, 255, 255), (15, grid_size * 1 - 4), (SCREEN_WIDTH - 15, grid_size * 1 - 4), 8)
	pygame.draw.line(screen, (255, 255, 255), (15, grid_size * 2 - 4), (SCREEN_WIDTH - 15, grid_size * 2 - 4), 8)


def check_winner_x():
	global game_state
	global game_winner
	for j in range(3):
		num = 0
		for i in range(3):
			if matrix[j][i] == 'X':
				num += 1
				if num >= 3:
					print('WIN X')
					game_state = False
					game_winner = 'X'
		num = 0

		for i in range(3):
			if matrix[i][j] == 'X':
				num += 1
				if num >= 3:
					print('WIN X')
					game_state = False
					game_winner = 'X'

	if (matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X') or (matrix[2][0] == 'X' and matrix[1][1] == 'X' and matrix[0][2] == 'X'):
		print('WIN X')
		game_state = False
		game_winner = 'X'

def check_winner_o():
	global game_state
	global game_winner
	for j in range(3):
		num = 0
		for i in range(3):
			if matrix[j][i] == 'O':
				num += 1
				if num >= 3:
					print('WIN O')
					game_state = False
					game_winner = 'O'

		num = 0

		for i in range(3):
			if matrix[i][j] == 'O':
				num += 1
				if num >= 3:
					print('WIN O')
					game_state = False
					game_winner = 'O'

	if (matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O') or (matrix[2][0] == 'O' and matrix[1][1] == 'O' and matrix[0][2] == 'O'):
		print('WIN O')
		game_state = False
		game_winner = 'O'


def check_draw():
	global game_state
	global game_winner
	num = 0
	for j in range(3):
		for i in range(0, 3):
			if matrix[j][i] != '':
				num += 1

	if num >= 9:
		game_state = False
		game_winner = '-'

while True:
	screen.fill((25, 25, 25))
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONUP and game_state:

			for j in range(3):
				for i in range(3):

					if (pygame.mouse.get_pos()[1] > grid_size * j) and (pygame.mouse.get_pos()[1] < grid_size * (j + 1)):
						if (pygame.mouse.get_pos()[0] > grid_size * i) and (pygame.mouse.get_pos()[0] < grid_size * (i + 1)):
							if (matrix[j][i] == ''):
								matrix[j][i] = current_player

								if current_player == 'X':
									current_player = 'O'
								else: 
									current_player = 'X'


		if event.type == pygame.KEYDOWN and not game_state:
			if event.key == pygame.K_SPACE:
				matrix = [
					['', '', ''],
					['', '', ''],
					['', '', '']

				]
				game_state = True
				x_color = (255, 255, 255)
				o_color = (255, 255, 255)
				
	for j in range(3):
		for i in range(3):
			if matrix[j][i] == 'O':
				pygame.draw.circle(screen, o_color, (grid_size * i + grid_size/2, grid_size * j + grid_size/2), 70, 10)
			elif matrix[j][i] == 'X': 
				pygame.draw.line(screen, x_color, (grid_size * i + 35, grid_size * j + 35), (grid_size * (i + 1) - 35, grid_size * (j + 1) - 35), 15)
				pygame.draw.line(screen, x_color, (grid_size * i + 35, grid_size * (j + 1) - 35), (grid_size * (i + 1) - 35, grid_size * j + 35), 15)

	draw_grid()
	if game_state:
		check_winner_x()
		check_winner_o()
		check_draw()

	else:
		if (game_winner == 'X'):
			x_color = (0, 200, 50)
		elif (game_winner == 'O'):
			o_color = (200, 0, 50)
		elif (game_winner == '-'):
			x_color = (230, 130, 50)
			o_color = (230, 130, 50)


	pygame.display.update()