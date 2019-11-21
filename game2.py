
from gamelib import*
game2=Game(800,600,"Basketball")

bk=Image ("ball court.jpg",game2)
bk.resizeTo(800,600)

Damian=Image("Damian.png",game2)
Damian.resizeBy(-50)
Damian.setSpeed(8,60)

Kevin=Image("Kevin.png",game2)
Kevin.resizeBy(-30)
Kevin.setSpeed(10,60)

ball = Image("ball.png",game2)
ball.resizeBy(-50)

while not game2.over:
    game2.processInput()
    
    bk.draw()
    Damian.move(True)
    Kevin.move(True)
    ball.moveTo(mouse.x,mouse.y)
    game2.update(30)
    
game.quit()
