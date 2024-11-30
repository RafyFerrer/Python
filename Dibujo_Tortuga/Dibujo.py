import turtle

# Crea una tortuga y configura su tamaño y velocidad
t = turtle.Turtle()
t.speed(10)
t.pensize(5)

# Dibuja el cuerpo del coche
t.begin_fill()
t.color("red")
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.end_fill()

# Dibuja las ruedas
t.color("black")
t.up()
t.forward(10)
t.right(90)
t.forward(10)
t.left(90)
t.down()
t.circle(10)
t.up()
t.forward(90)
t.left(90)
t.forward(10)
t.right(90)
t.down()
t.circle(10)

# Oculta la tortuga y muestra el dibujo
t.hideturtle()
turtle.done()


