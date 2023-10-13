import pygame, pygame_gui, threading
from menu.menu import Menu
from menu.impl.main_menu import MainMenu
from menu.impl.game_menu import GameMenu
from Server import Server

###################################################################################
# Konstanten
###################################################################################

WIDTH = 1280
HEIGHT = 720
TITLE = "Shooting Range"
FPS = 60
   
class Game:
    state = "MENU"
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'game-mp/theme.json', True)
        self.menu: Menu = MainMenu(self.manager, self.screen, pygame)
        Game.state = "MENU"
        self.server_thread = threading.Thread(target=Server, name="server_start")


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
                if Game.state == "MENU":
                    if event.ui_element == MainMenu.get_play_ui_button(self.menu):
                        self.menu = GameMenu(self.manager, self.screen, pygame, self.clock, self)
                        Game.state = "GAME"
                    elif event.ui_element == MainMenu.get_start_server_ui_button(self.menu):
                        self.server_thread.start()

                        
                        
                    


###################################################################################
# Hauptprogramm
###################################################################################

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.tick()

    pygame.quit()