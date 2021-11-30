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

class BigBrick(Brick):
    def __init__(self,x,y, width, height):
        super().__init__(x,y,width,height,"gold")
        self.power = 2

    def update(self, balls):
        if self.active:
            self.draw()
            for ball in balls:
                if self.checkHit(ball):
                    self.power -= 1
                    if self.power == 0:
                        self.active = False
                    else:
                        self.colour = "orange"

class MultiballBrick(Brick):
    def __init__(self,x,y, width, height):
        super().__init__(x,y,width,height,"#14b9bc")

    def update(self, balls):
        if self.active:
            self.draw()
            for ball in balls:
                if self.checkHit(ball):
                    balls.append(Ball(ball.x,ball.y,ball.xspeed*-1,ball.yspeed-3 ))
                    self.active = False
                    return

class Ball():
    def __init__(self,x,y, xspeed, yspeed):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
    
    def draw(self):
        drawEllipse(self.x-10, self.y-10, 20,20,"red")


    def move(self, lives):
        self.x += self.xspeed
        if self.x < 15 or self.x > 795:
            self.xspeed *=-1
        self.y += self.yspeed
        if self.y < 15 or self.y > 795:
            self.yspeed *=-1
        if self.y > 795:
            lives -= 1
            changeLabel(livesLabel,"Lives: " + str(lives))
            balls.remove(self)
            if len(balls)==0:
                balls.append(Ball(player.x, player.y-20,-5,-7))
        return lives


class Bat(Brick):
    def __init__(self):
        super().__init__(450,750,100,20,"white")

    def update(self):
        self.move()
        self.draw()
        for ball in balls:
            self.checkHit(ball)
                

    def move(self):
        if keyPressed("right"):
            self.x += 8
        if keyPressed("left"):
            self.x -= 8




bricks = []
balls = []

for x in range(2,750, 92):
    bricks.append(BigBrick(x, 90, 90,50))
for x in range(2,750, 72):
    bricks.append(Brick(x, 150, 70,50,"green"))
balls.append(Ball(100,300,5,7))
bricks.append(MultiballBrick(380,210,50,50))
player = Bat()


lives = 3
livesLabel = makeLabel("Lives: " + str(lives),20,10,10,"white")
showLabel(livesLabel)
while lives > 0:
    clearShapes()
    player.draw()
    for b in balls:
        lives = b.move(lives)
        b.draw()
    for br in bricks:
        br.update(balls)
    player.update()
    updateDisplay()
    tick(60)

endWait()



