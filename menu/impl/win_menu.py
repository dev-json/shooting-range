from pygame_gui import UIManager, UI_BUTTON_PRESSED
from pygame_gui.elements import *
from pygame import Rect, Surface, Event
from menu.menu import Menu
from menu.impl.main_menu import MainMenu

import pygame

class WinMenu(Menu):
    def __init__(self, manager: UIManager, surface: Surface, pygame: pygame, game: any, score: float) -> None:
        super().__init__(manager, surface, pygame)
        self.game = game
        manager.clear_and_reset() 
        self.pygame.mouse.set_visible(1)
        surface.fill((0, 0, 0))
       
        ### won label!
        self.won_label = UILabel(
            manager=self.uimanager,
            text=f'YOU WON! Score: {int(score)}',
            relative_rect=Rect((Menu.WIDTH/2)-(300/2), (Menu.HEIGHT/2)-(100/2), 300, 100),
            object_id="#won_label"
        )

        ### Play again button
        self.play_button = UIButton(
            relative_rect=Rect((Menu.WIDTH/2)-(300/2), (Menu.HEIGHT/2)+200, 300, 100),
            text='play again',
            manager=self.uimanager,
            object_id='#play_button'
        )

        self.won_label.text_horiz_alignment="center"
        self.won_label.rebuild()

    def update(self):
        pass

    def draw(self):
        pass        

    def events(self,  event: Event):
        if event.type == UI_BUTTON_PRESSED:
            if event.ui_element == self.play_button:
                self.game.menu = MainMenu(self.uimanager, self.surface, pygame)

