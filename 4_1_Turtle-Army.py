import turtle
bob = turtle.Turtle()
bob.shape('turtle')
bob.color('green')

for y in range(3):
  for i in range(4):
    bob.stamp()
    bob.forward(50)
  bob.backward(200)
  bob.right(90)
  bob.forward(50)
  bob.left(90)
bob.hideturtle()
