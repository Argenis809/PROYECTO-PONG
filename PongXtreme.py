import turtle
import winsound


theme = winsound.PlaySound("theme.wav", winsound.SND_ASYNC)


#ventana
wn = turtle.Screen()
wn.title("PONG-XTREME")
wn. bgcolor("#000000")
wn.setup(width=800, height=600)
wn.tracer(0)
turtle.bgpic("fondo.png" ) #Fondo

#Jugador A

player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square") #La forma que tendrá
player_1.color("#C3140F")
player_1.penup() #elimina la linea de rastro que queda cuando se mueve
player_1.goto(-360,0)
player_1.shapesize(stretch_wid=5, stretch_len=1)

#Jugador B

player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square") 
player_2.color("#008DDC")
player_2.penup() 
player_2.goto(350,0)
player_2.shapesize(stretch_wid=5, stretch_len=1)

#Pelota

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle") 
ball.color("white")
ball.penup() 
ball.goto(0,0)
ball.dx = 1.5
ball.dy = 1.5

#Linea division

division = turtle.Turtle()
division.color("#383B44")
division.goto(0,400)
division.goto(0,-400)

#marcador
marcador=turtle.Turtle()
marcador.speed(0)
marcador.color("#FAA900")
marcador.penup()
marcador.hideturtle()
marcador.goto(0,240)
marcador.write("Jugador A: 0      Jugador B: 0", align="center", font=("Courier", 24,"normal"))

mensaje_marcador = turtle.Turtle()
mensaje_marcador.speed(0)
mensaje_marcador.color("#383B44")
mensaje_marcador.penup()
mensaje_marcador.hideturtle()
mensaje_marcador.goto(0,-260)
mensaje_marcador.write("GANA EL PRIMERO EN LLEGAR A 20", align="center",font=("Courier", 16,"normal") )

#variables del marcador

marcadorA = 0
marcadorB = 0

#Funciones

#jugador1
def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)

def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)

#Jugador2
def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)


def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)

#mensaje final
def winner_message():
    mensaje=turtle.Turtle()
    mensaje.speed(0)
    mensaje.color("white")
    mensaje.penup()
    mensaje.hideturtle()
    mensaje.goto(0,-220)
    mensaje.write("WE HAVE A WINNER \n CONGRATULATION!", align="center", font=("Courier", 24,"bold"))

#teclado
#Listen escucha por el teclado para ejecutar una determinada función
wn.listen()

#movimiento jugador uno
wn.onkeypress(player_1_up, "w")
wn.onkeypress(player_1_up, "W")
wn.onkeypress(player_1_down, "s")
wn.onkeypress(player_1_down, "S")

#movimiento jugador dos
wn.onkeypress(player_2_up, "Up")
wn.onkeypress(player_2_down, "Down")


while True:
    wn.update()

#movimiento de pelota

    ball.setx (ball.xcor() + ball.dx)
    ball.sety (ball.ycor() + ball.dy)
    
    #bordes en Y
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1

    #bordes en X
    if ball.xcor() > 350:
        ball.goto(0,0) #Para que vuelva al centro
        ball.dx *= -1
        marcadorA += 1
        marcador.clear()
        marcador.write("Jugador A:{}      Jugador B: {}".format(marcadorA,marcadorB), align="center", font=("Courier", 24,"normal"))
    
    if ball.xcor() < -350:
        ball.goto(0,0)
        ball.dx *= -1
        marcadorB += 1
        marcador.clear()
        marcador.write("Jugador A:{}      Jugador B: {}".format(marcadorA,marcadorB), align="center", font=("Courier", 24,"normal"))

    #REBOTE DE JUGADOR2
    if ((ball.xcor() > 340 and ball.ycor() < 350 )
        and (ball.ycor() < player_2.ycor() + 50 
        and ball.ycor() > player_2.ycor() -50)):
        ball.dx *= -1

    
    #REBOTE DE JUGADOR1
    if ((ball.xcor() < -340 and ball.xcor() > -350 )
        and (ball.ycor() < player_1.ycor() + 50 
        and ball.ycor() > player_1.ycor() -50)):
        ball.dx *= -1



    if marcadorA == 20 or marcadorB == 20:
        winner_message()
        game_over = winsound.PlaySound("game_over.wav", winsound.SND_ASYNC)
        game_over= winsound.SND_NOSTOP
        break

exit()
turtle.getscreen()._root.mainloop()





