from . duck import Duck

class MovingDuck(Duck):
    def __init__(self, duck_img, speed):
        super().__init__(duck_img)
        self.img = duck_img
        self.speed = speed
        self.directionX = 1  
        self.directionY = 1  

    def update_position(self):
        new_posX = self.posX + self.speed * self.directionX
        if new_posX < 0 or new_posX > 1280 - self.img.get_width():
            self.directionX *= -1 
        new_posY = self.posY + self.speed * self.directionY
        if new_posY < 0 or new_posY > 720 - self.img.get_height():
            self.directionY *= -1 

        self.posX = new_posX
        self.posY = new_posY