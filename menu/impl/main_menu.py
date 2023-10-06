from pygame_gui import UIManager
from pygame_gui.elements import *
from pygame import Rect, Surface
from menu.menu import Menu

import pygame


class MainMenu(Menu):
    def __init__(self, manager: UIManager, surface: Surface, pygame: pygame) -> None:
        super().__init__(manager, surface, pygame)

        ### Server
        self.server_ip_label = UILabel(
            manager=self.uimanager,
            text='server-ip',
            relative_rect=Rect(0,0,250, 16)
        )
        self.server_ip_label.text_horiz_alignment="left"
        self.server_ip_label.rebuild()

        self.server_ip_input = UITextEntryLine(
            relative_rect=Rect(0,18,300, 30),
            manager=self.uimanager
        )

        ### Username
        self.username_ip_label = UILabel(
            manager=self.uimanager,
            text='username',
            relative_rect=Rect(0,55,250, 16)
        )
        self.username_ip_label.text_horiz_alignment="left"
        self.username_ip_label.rebuild()

        self.username_ip_input = UITextEntryLine(
            relative_rect=Rect(0,73,300, 30),
            manager=self.uimanager
        )

        ### Play button
        self.play_button = UIButton(
            relative_rect=Rect((Menu.WIDTH/2)-(300/2), (Menu.HEIGHT/2)-(100/2), 300, 100),
            text='play',
            manager=self.uimanager,
            object_id='#play_button'
        )

        ### Start Server button
        self.start_server_button = UIButton(
            relative_rect=Rect(Menu.WIDTH-200, Menu.HEIGHT-50, 200, 50),
            text='start-server',
            manager=self.uimanager,
            object_id='#start_server_button'
        )

    def update(self):
        pass

    def draw(self):
        pass

    def events(self, event: pygame.Event):
        pass

    @staticmethod
    def get_play_ui_button(self) -> UIButton:
        return self.play_button