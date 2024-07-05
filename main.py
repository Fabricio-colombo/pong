import turtle

screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

divider = turtle.Turtle()
divider.color("white")
divider.goto(0, 300)
divider.goto(0, -300)
divider.hideturtle()

jogador_direita = turtle.Turtle()
jogador_direita.speed(0)
jogador_direita.shape("square")
jogador_direita.color("white")
jogador_direita.shapesize(stretch_wid=5, stretch_len=1)
jogador_direita.penup()
jogador_direita.goto(350, 0)

jogador_esquerda = turtle.Turtle()
jogador_esquerda.speed(0)
jogador_esquerda.shape("square")
jogador_esquerda.color("white")
jogador_esquerda.shapesize(stretch_wid=5, stretch_len=1)
jogador_esquerda.penup()
jogador_esquerda.goto(-350, 0)

jogador_speed = 60

bola = turtle.Turtle()
bola.speed(40)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 6.3
bola.dy = -6.3

placar_direita = 0
placar_esquerda = 0

placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador Direita: 0  Jogador Esquerda: 0", align="center", font=("Courier", 24, "normal"))

def jogador_direita_para_cima():
    y = jogador_direita.ycor()
    if y < 250:
        y += jogador_speed
    jogador_direita.sety(y)

def jogador_direita_para_baixo():
    y = jogador_direita.ycor()
    if y > -240:
        y -= jogador_speed
    jogador_direita.sety(y)

def jogador_esquerda_para_cima():
    y = jogador_esquerda.ycor()
    if y < 250:
        y += jogador_speed
    jogador_esquerda.sety(y)

def jogador_esquerda_para_baixo():
    y = jogador_esquerda.ycor()
    if y > -240:
        y -= jogador_speed
    jogador_esquerda.sety(y)

screen.listen()
screen.onkey(jogador_direita_para_cima, "Up")
screen.onkey(jogador_direita_para_baixo, "Down")
screen.onkey(jogador_esquerda_para_cima, "w")
screen.onkey(jogador_esquerda_para_baixo, "s")

while True:
    screen.update()

    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if (bola.dx > 0) and (350 > bola.xcor() > 340) and (jogador_direita.ycor() + 50 > bola.ycor() > jogador_direita.ycor() - 50):
        bola.dx *= -1

    if (bola.dx < 0) and (-350 < bola.xcor() < -340) and (jogador_esquerda.ycor() + 50 > bola.ycor() > jogador_esquerda.ycor() - 50):
        bola.dx *= -1

    if bola.xcor() > 390:
        placar_esquerda += 1
        placar.clear()
        placar.write(f"Jogador Direita: {placar_direita}  Jogador Esquerda: {placar_esquerda}", align="center", font=("Courier", 24, "normal"))
        bola.goto(0, 0)
        bola.dx *= -1

    if bola.xcor() < -390:
        placar_direita += 1
        placar.clear()
        placar.write(f"Jogador Direita: {placar_direita}  Jogador Esquerda: {placar_esquerda}", align="center", font=("Courier", 24, "normal"))
        bola.goto(0, 0)
        bola.dx *= -1
