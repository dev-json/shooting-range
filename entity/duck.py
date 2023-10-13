import random

class Duck:
    def __init__(self, duck_img):
        self.posX = random.randint(500, 1000)
        self.posY = random.randint(100, 400)
        self.img = duck_img
        self.collision = duck_img.get_rect(topleft = (self.posX, self.posY)) 