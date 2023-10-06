import pygame, pygame_gui, time
from menu.menu import Menu
from menu.impl.main_menu import MainMenu
from menu.impl.game_menu import GameMenu

###################################################################################
# Konstanten
###################################################################################

WIDTH = 1280
HEIGHT = 720
TITLE = "Shooting Range"
FPS = 60
   
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'game-mp/theme.json', True)
        self.menu: Menu = MainMenu(self.manager, self.screen, pygame)
        self.state = "MENU"

    def tick(self):
        self.events()
        self.clock.tick(FPS)
        self.menu.update()
        self.manager.update(self.clock.get_time())
        self.menu.draw()
        # Updated core components
        self.manager.draw_ui(self.screen)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            self.menu.events(event)
            if event.type == pygame.QUIT:
                self.running = False
            self.manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if self.state == "MENU":
                    if event.ui_element == MainMenu.get_play_ui_button(self.menu):
                        self.menu = GameMenu(self.manager, self.screen, pygame, self.clock)
                        self.state = "GAME"
                        
                        
                    


###################################################################################
# Hauptprogramm
###################################################################################

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.tick()

    pygame.quit()
