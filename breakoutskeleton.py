from pygame_functions import *

screenSize(800,800)
setBackgroundColour("darkblue")

setAutoUpdate(False)

class Brick():
    def __init__(self,x,y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.active = True

    def draw(self):
        drawRect(self.x, self.y, self.width, self.height,self.colour)

    def checkHit(self, ball):
        if ball.x > self.x-10 and ball.x < self.x+self.width+10 and ball.y > self.y-10 and ball.y< self.y+self.height+10:
            ball.yspeed *= -1
            if ball.yspeed <0:
                ball.y -=10
            else:
                ball.y +=10
            return True
        return False

    def update(self,balls):
        if self.active:
            self.draw()
            for ball in balls:
                if self.checkHit(ball):
                    self.active = False
                    return




bricks = []
balls = []

bricks.append(Brick(380, 150, 70,50,"green"))


lives = 3
livesLabel = makeLabel("Lives: " + str(lives),20,10,10,"white")
showLabel(livesLabel)
while lives > 0:
    clearShapes()
    for br in bricks:
        br.update(balls)
    updateDisplay()
    tick(60)

endWait()



