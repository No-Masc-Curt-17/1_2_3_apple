#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple_1 = trtl.Turtle()
apple_2 = trtl.Turtle()
apple_3 = trtl.Turtle()
apple_4 = trtl.Turtle()
apple_5 = trtl.Turtle()
apple_1.shape(apple_image)
apple_2.shape(apple_image)
apple_3.shape(apple_image)
apple_4.shape(apple_image)
apple_5.shape(apple_image)
apple_1.penup()
apple_1.goto(0,0)
apple_2.penup()
apple_2.goto(100,0)
apple_3.penup()
apple_3.goto(200,0)
apple_4.penup()
apple_4.goto(-100,0)
apple_5.penup()
apple_5.goto(-200,0)

letters=['a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't','u', 'v', 'w','x','y','z']
letter_1 = letters[rand.randint(1, 26)]
letters.pop(letters.index(str(letter_1)))
letter_2 = letters[rand.randint(1, 25)]
letters.pop(letters.index(str(letter_2)))
letter_3 = letters[rand.randint(1, 24)]
letters.pop(letters.index(str(letter_3)))
letter_4 = letters[rand.randint(1, 23)]
letters.pop(letters.index(str(letter_4)))
letter_5 = letters[rand.randint(1, 22)]
letters.pop(letters.index(str(letter_5)))
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def drop():
    wn.tracer(False)
    draw_an_A()
    apple_1.penup()
    wn.tracer(True)
    apple_1.goto(0, -200)
    apple_1.pendown()
    apple_1.clear()
def draw_an_A():
    apple_1.hideturtle()
    ok = apple_1.xcor()
    alr = apple_1.ycor()
    apple_1.penup()
    apple_1.goto(ok-18, alr+40)
    apple_1.pendown()
    apple_1.color("white")
    apple_1.write(letter_1, font=("Times New Roman", 55, "bold")) 
    apple_1.showturtle()

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def drop_apple():
    wn.tracer(False)
    draw_an_A()
    apple_1.penup()
    wn.tracer(True)
    apple_1.goto(0, -200)
    apple_1.pendown()
    apple_1.clear()

def draw_an_A():
    apple_1.hideturtle()
    set = apple_1.xcor()
    set_y = apple_1.ycor()
    apple_1.penup()
    apple_1.goto(set-18,set_y+40)
    apple_1.pendown()
    apple_1.color("white")
    apple_1.write(letter_1, font=("Arial", 55, "bold")) 
    apple_1.showturtle()
    
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def drop_apple1():
    apple_1.goto(0,-200)
    apple_1.pendown()
def drop_apple2():
    apple_2.goto(100,-200)
    apple_2.pendown()
def drop_apple3():
    apple_3.goto(200,-200)
    apple_3.pendown()
def drop_apple4():
    apple_4.goto(-100,-200)
    apple_4.pendown()
def drop_apple5():
    apple_5.goto(-200,-200)
    apple_5.pendown()

def draw_a_letter(a_apple, letter):
    a_apple.hideturtle()
    set = a_apple.xcor()
    set_y = a_apple.ycor()
    a_apple.penup()
    a_apple.goto(set-18,set_y+40)
    a_apple.color("white")
    a_apple.write(letter, font=("Arial", 55, "bold")) 
    a_apple.goto(set+18,set_y-40)
    a_apple.showturtle()

#-----function calls-----
draw_a_letter(apple_1,letter_1)
draw_a_letter(apple_2,letter_2)
draw_a_letter(apple_3,letter_3)
draw_a_letter(apple_4,letter_4)
draw_a_letter(apple_5,letter_5)

wn.onkeypress(drop_apple1,letter_1)
wn.onkeypress(drop_apple2,letter_2)
wn.onkeypress(drop_apple3,letter_3)
wn.onkeypress(drop_apple4,letter_4)
wn.onkeypress(drop_apple5,letter_5)
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()