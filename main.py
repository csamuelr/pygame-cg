import pygame 
import sys
import os

from pygame import mixer
from pygame.locals import *
from game import Game

pygame.init()
mixer.init()


if __name__ == '__main__':

	fps = 60
	frame = pygame.time.Clock()
	pygame.display.set_caption('Jogo Computação Gráfica')
	screen = pygame.display.set_mode((1080,720))
	background = pygame.image.load(os.path.join('assets', 'bg.jpg'))
	banner = pygame.image.load(os.path.join('assets', 'banner.png'))
	banner = pygame.transform.scale(banner, (500, 500))
	banner_rec = banner.get_rect()
	banner_rec.x = screen.get_width() / 4

	play_button = pygame.image.load(os.path.join('assets', 'button_start.png'))
	play_button = pygame.transform.scale(play_button, (400,150))
	play_button_rec = play_button.get_rect()
	play_button_rec.x = screen.get_width() / 3.33 # 33%
	play_button_rec.y = screen.get_height() / 1.99

	about_button = pygame.image.load(os.path.join('assets', 'button_about.png'))
	about_button = pygame.transform.scale(about_button, (400, 150))
	about_button_rec = about_button.get_rect()
	about_button_rec.x = screen.get_width() / 3.33
	about_button_rec.y = screen.get_height() / 1.55

	about_bg = pygame.image.load(os.path.join('assets', 'bg_about.png'))
	about_bg = pygame.transform.scale(about_bg, (600, 600))
	about_bg_rec = about_bg.get_rect(center=(screen.get_width()/2, screen.get_height()/2.3)) 

	back_button = pygame.image.load(os.path.join('assets', 'button_back.png'))
	back_button = pygame.transform.scale(back_button, (400, 150))
	back_button_rec = back_button.get_rect()
	back_button_rec.x = screen.get_width() /3.33
	back_button_rec.y = screen.get_height() /1.3

	game = Game()

	while True:
		
		screen.blit(background, (0, -200))
			
		if game.is_playing:
			game.update(screen)

		else:
			if game.is_about:
				screen.blit(about_bg, about_bg_rec)
				screen.blit(back_button, back_button_rec)
			else:
				screen.blit(play_button, play_button_rec)
				screen.blit(banner, banner_rec)
				screen.blit(about_button, about_button_rec)

		pygame.display.flip()

		for event in pygame.event.get():
			
			if event.type == QUIT:
				sys.exit()

			elif event.type == MOUSEBUTTONDOWN and not game.is_about:

				if play_button_rec.collidepoint(event.pos):
					mixer.Sound(os.path.join('assets', 'sounds', 'click.ogg')).play()
					game.is_playing = True
					game.generate_monster(4)

				elif about_button_rec.collidepoint(event.pos):
					mixer.Sound(os.path.join('assets', 'sounds', 'click.ogg')).play()
					game.is_about = True

			elif event.type == MOUSEBUTTONDOWN and game.is_about:
				
				if back_button_rec.collidepoint(event.pos):
					mixer.Sound(os.path.join('assets', 'sounds', 'click.ogg')).play()
					game.is_about = False

			if game.is_playing:

				if event.type == KEYDOWN:
					game.pressed[event.key] = True

					if event.key == K_SPACE:
						mixer.Sound(os.path.join('assets', 'sounds', 'tir.ogg')).play()
						game.player.launch_projectile()
						game.player.animate()

				elif event.type == KEYUP:
					game.pressed[event.key] = False

					if event.key == K_SPACE: 
						mixer.Sound(os.path.join('assets', 'sounds', 'tir.ogg')).play()
						game.player.launch_projectile()
						game.player.animate()

		pygame.display.update()
		frame.tick(fps)
