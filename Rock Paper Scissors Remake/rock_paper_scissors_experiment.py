import pygame
import random
import time

pygame.init()

game_screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Rock Paper Scissors")

white = (255, 255, 255)
black = (0,255 ,0)
blue = (0, 0, 255)


class GameObject:

	#initializes all the variables
	def __init__(self, image_file, pos_tuple): 
		self.image_file = image_file
		self.pos_tuple = pos_tuple
		self.image = pygame.image.load(self.image_file)

	#draws the object
	def draw_object(self): 
		self.rect = game_screen.blit(self.image, self.pos_tuple)



#user positions
user_rock_xpos = 150
user_rock_ypos = 500
user_rock_pos_tuple = (user_rock_xpos, user_rock_ypos)

user_paper_xpos = 350
user_paper_ypos = 500
user_paper_pos_tuple = (user_paper_xpos, user_paper_ypos)

user_scissors_xpos = 550
user_scissors_ypos = 500
user_scissors_pos_tuple = (user_scissors_xpos, user_scissors_ypos)

#opponent positions
opp_choice_xpos = 160
opp_choice_ypos = 25
opp_choice_pos_tuple = (opp_choice_xpos, opp_choice_ypos)

opp_rock_xpos = 150
opp_rock_ypos = 100
opp_rock_pos_tuple = (opp_rock_xpos, opp_rock_ypos)

opp_paper_xpos = 350
opp_paper_ypos = 100
opp_paper_pos_tuple = (opp_paper_xpos, opp_paper_ypos)

opp_scissors_xpos = 550
opp_scissors_ypos = 100
opp_scissors_pos_tuple = (opp_scissors_xpos, opp_scissors_ypos)

messgae_xpos = 300
message_ypos = 300
message_tuple = (messgae_xpos, message_ypos)

#declares objects
Rock = GameObject('rock.png', user_rock_pos_tuple)
Paper = GameObject('paper.png', user_paper_pos_tuple)
Scissors = GameObject('scissors.png', user_scissors_pos_tuple)

OpponentsChoice = GameObject('opponents_choice.png', opp_choice_pos_tuple)
OpponentsRock = GameObject('rock.png', opp_rock_pos_tuple)
OpponentsPaper = GameObject('paper.png', opp_paper_pos_tuple)
OpponentsScissors = GameObject('scissors.png', opp_scissors_pos_tuple)

WinningMessage = GameObject('YouWon.png', message_tuple)
TieMessage = GameObject('YouTied.png', message_tuple)
LosingMessage = GameObject('YouLost.png', message_tuple)

images_array = [Rock, Paper, Scissors, OpponentsChoice, OpponentsRock, OpponentsPaper, OpponentsScissors]


def delete_opponents_images(): 

	rand_int = random.random() * 3
	#Rock <= 1; Paper<= 2; Scissors <= 3
	#if rock remove paper and scissors
	if rand_int <= 1: 
		images_array.remove(OpponentsPaper)
		images_array.remove(OpponentsScissors)
		return 'rock'
	#if paper remove rock and scissors
	elif rand_int <= 2: 
		images_array.remove(OpponentsRock)
		images_array.remove(OpponentsScissors)
		return 'paper'
	#if scissors remove rock and paper
	elif rand_int <= 3: 
		images_array.remove(OpponentsRock)
		images_array.remove(OpponentsPaper)
		return 'scissors'

def game_loop(): 

	game_exit = False
	background = white
	while not game_exit: 

		#clears the game_screen
		game_screen.fill(background)

		#draws Players objects
		for images in images_array: 
			images.draw_object()

		#updates the screen
		pygame.display.update()

		#Event Handling
		for event in pygame.event.get():			 

			if event.type == pygame.QUIT: 
				game_exit = True

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
				pos = pygame.mouse.get_pos()

				#if the user chooses rock, paper, or scissors delete objects
				if Rock.rect.collidepoint(pos): 
					images_array.remove(Paper)
					images_array.remove(Scissors)
					opponents_choice = delete_opponents_images()
					if opponents_choice == 'rock': 
						images_array.append(TieMessage)
					elif opponents_choice == 'paper': 
						images_array.append(LosingMessage)
					elif opponents_choice == 'scissors': 
						images_array.append(WinningMessage)
					
				
				if Paper.rect.collidepoint(pos): 
					images_array.remove(Rock)
					images_array.remove(Scissors)
					opponents_choice = delete_opponents_images()
					if opponents_choice == 'rock': 
						images_array.append(WinningMessage)
					elif opponents_choice == 'paper': 
						images_array.append(TieMessage)
					elif opponents_choice == 'scissors': 
						images_array.append(LosingMessage)

				if Scissors.rect.collidepoint(pos): 
					images_array.remove(Rock)
					images_array.remove(Scissors)
					opponents_choice = delete_opponents_images()
					if opponents_choice == 'rock': 
						images_array.append(LosingMessage)
					elif opponents_choice == 'paper': 
						images_array.append(WinningMessage)
					elif opponents_choice == 'scissors':
						images_array.append(TieMessage)

		
game_loop()

