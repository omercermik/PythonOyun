import turtle
import time

wn = turtle.Screen()
wn.title("Savaş Oyunu")
wn.bgcolor("black")
wn.setup(width=600, height=600)

player = turtle.Turtle()
player.color("pink")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

enemy = turtle.Turtle()
enemy.color("white")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(0, 250)

bullet = turtle.Turtle()
bullet.color("blue")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = ((t1.xcor()-t2.xcor())**2 + (t1.ycor()-t2.ycor())**2)**0.5
    if distance < 15:
        return True
    else:
        return False

wn.listen()
wn.onkeypress(fire_bullet, "space")

bulletstate = "ready"

while True:
    enemy.forward(2)

    if enemy.xcor() > 280 or enemy.xcor() < -280:
        enemy.right(180)

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    if is_collision(bullet, enemy):
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        enemy.setposition(-200, 250)

    time.sleep(0.01)
