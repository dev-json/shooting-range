from pygame.surface import Surface
from pygame_gui import UIManager
import pygame


class Menu():
    WIDTH = 1280
    HEIGHT = 720
    def __init__(self, manager: UIManager, surface: Surface, pygame: pygame) -> None:
       self.uimanager = manager
       self.surface = surface
       self.pygame = pygame

    def draw(self):
        pass


    def update(self):
        pass

    def events(self, event: pygame.Event):
        pass