import pygame
import os

from random import randint
from pygame import mixer

class Comet(pygame.sprite.Sprite):

    '''
        Esta classe implementa o Cometa (ou meteoro)
        que é lançado a cada periodo de tempo e o player precisa
        evitar ser atingido por eles. O período de 
        lançamento de meteooros é deginifo em commet_event.py
    '''

    def __init__(self, comet_evet):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'comet.png'))
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect()
        self.rect.x = randint(20, 800)
        self.rect.y = - randint(0, 800)
        self.velocity = randint(4, 7)
        self.comet_evet = comet_evet
        
    def remove(self):
        self.comet_evet.all_comets.remove(self)

        if len(self.comet_evet.all_comets) == 0:
            self.comet_evet.reset_percent()
            self.comet_evet.game.generate_monster(4)

    def fall(self):
        
        self.rect.y += self.velocity
       
        if self.rect.y >= 500:
            self.remove()

            if len(self.comet_evet.all_comets) == 0:
                self.comet_evet.reset_percent()
                self.comet_evet.fall_mode = False

        if self.comet_evet.game.check_collision(
            self, self.comet_evet.game.all_players
        ):
            self.remove()
            self.comet_evet.game.player.demage(20)
