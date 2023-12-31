from pygame_gui import UIManager
from pygame_gui.elements import *
from pygame import Rect, Surface, Clock, Event
from menu.menu import Menu
from entity.duck import Duck
from entity.moving_duck import MovingDuck
from menu.impl.win_menu import WinMenu
import random
import pygame


class GameMenu(Menu):

    def __init__(self, manager: UIManager, surface: Surface, pygame: pygame, clock: Clock, game: any) -> None:
        super().__init__(manager, surface, pygame)
        self.clock = clock
        self.game = game
        manager.clear_and_reset() 
        self.pygame.mouse.set_visible(0)

        self.wood_bg = pygame.image.load("Assets/Wood_BG.png")
        self.land_bg = pygame.image.load("Assets/land_BG.png")
        self.crosshair_img = pygame.image.load("Assets/crosshair.png")
        self.duck_img = pygame.image.load("Assets/duck.png")
        
        self.doom_gun = pygame.image.load("Assets/custom/doom_gun.png")
        self.doom_gun_fire = pygame.image.load("Assets/custom/doom_gun_fire.png")
        self.doom_gun = pygame.transform.scale(self.doom_gun, (200, 200))
        self.doom_gun_fire = pygame.transform.scale(self.doom_gun_fire, (100, 100))

        self.ducks = [] 
        self.ducks_mov = []
        for i in range(10):
            duck = Duck(self.duck_img)
            self.ducks.append(duck)

        for i in range(5):
            duck = MovingDuck(self.duck_img, random.randint(0, 5))
            self.ducks_mov.append(duck)

        self.score = 0
        self.lastTimeHit = 0
        self.currentTime = 0

        self.delta = 0

        self.shooting = False
        
        ### FPS
        self.fps_label = UILabel(
            manager=self.uimanager,
            text=f'fps: {int(self.clock.get_fps())}',
            relative_rect=Rect(0,0,100, 32),
            object_id="#fps_label"
        )
        self.fps_label.text_horiz_alignment="left"
        ### FPS
        self.score_label = UILabel(
            manager=self.uimanager,
            text=f'score: {self.score}',
            relative_rect=Rect(0,35, 300, 32),
            object_id="#fps_label"
        )
        self.score_label.text_horiz_alignment="left"
        self.score_label.rebuild()

    def update(self):
        self.currentTime += 1
        if self.shooting == True:
            self.delta += 1
            if self.delta > 20:
                self.shooting = False
                self.delta = 0

        for i in range(len(self.ducks_mov)):
            curr_duck: MovingDuck = self.ducks_mov[i]
            curr_duck.collision = curr_duck.img.get_rect(topleft = (curr_duck.posX, curr_duck.posY)) 
            curr_duck.update_position()

    def draw(self):
        self.fps_label.set_text(f'fps: {int(self.clock.get_fps())}')
        self.score_label.set_text(f'score: {int(self.score)}')
        self.surface.blit(self.wood_bg, (0, 0))
        self.surface.blit(self.land_bg, (0, 550))
        mx,my=pygame.mouse.get_pos()
        for duck in self.ducks:
            self.surface.blit(self.duck_img, (duck.posX, duck.posY))
        for duck in self.ducks_mov:
            self.surface.blit(self.duck_img, (duck.posX, duck.posY))
        self.surface.blit(self.crosshair_img, (mx-24, my-24))        
        self.surface.blit(self.doom_gun, (mx-140, 550))
        if self.shooting == True:
             #self.surface.blit(self.doom_gun_fire, (593, 491))
            self.surface.blit(self.doom_gun_fire, (mx-47, 492))

    def events(self,  event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.shooting == True:
                return
            self.shoot()
            for duck in self.ducks:
                if duck.collision.collidepoint(event.pos):
                    self.ducks.remove(duck)
                    self.lastTimeHit = self.currentTime
                    self.score += 1000 / (self.lastTimeHit + 1)
                    self.currentTime = 1

                    if len(self.ducks) == 0 and len(self.ducks_mov) == 0:
                        self.game.menu = WinMenu(self.uimanager, self.surface, pygame, self.game, self.score)
                        pass

            for duck in self.ducks_mov:
                if duck.collision.collidepoint(event.pos):
                    self.ducks_mov.remove(duck)
                    self.lastTimeHit = self.currentTime
                    self.score += 1000 / (self.lastTimeHit + 1)
                    self.currentTime = 1

                    if len(self.ducks) == 0 and len(self.ducks_mov) == 0:
                        self.game.menu = WinMenu(self.uimanager, self.surface, pygame, self.game, self.score)
                        pass


    def shoot(self):
        if self.shooting == True:
            return
        self.shooting = True
        

