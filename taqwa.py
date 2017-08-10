import turtle
import time

SIZE_X=1000
SIZE_Y=700
screen = turtle.Screen()
screen.bgpic("world_map.gif")
screen.setup(SIZE_X, SIZE_Y)
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()

ethiopia = turtle.clone()
ethiopia.shape("square")
ethiopia.penup()
ethiopia.goto(-50,-120)
ethiopia.pendown()
ethiopia.stamp()

madagascar = turtle.clone()
madagascar.shape("circle")
madagascar.penup()
madagascar.goto(50,300)
madagascar.pendown()
madagascar.stamp()


chad = turtle.clone()
chad.shape("arrow")
chad.penup()
chad.goto(-400,200)
chad.stamp


peru = turtle.clone()
peru.shape("turtle")
peru.penup()
peru.goto(320,40)
peru.stamp

afghanistan= turtle.clone()
afghanistan.shape("classic")
afghanistan.penup()
afghanistan.goto(-300,-110)
afghanistan.stamp

pos_list = [(-50.00,-120.00), (50,300), (-400,200), (320,40), (-300,-100)]

riddle_dict = {

        'ethiopia': {
                'question': 'a kind of tree you can carry in your hand____',
                'answer_choices' :['dead tree' , 'palm tree' , 'apple tree' , 'lost tree'],
                'correct' : 'palm tree'
                } ,
        'madagascar': {
                'question': 'What is an astronauts favourite meal?____' ,
                'answer_choices' :['Launch' , 'Breakfast' , 'Dinner' , 'Brunch'],
                'correct' : 'Launch'
                } ,
        'chad': {
                'question' : 'In israel there is a doctor for each 400 person , in Chad there is a doctor foe each ____',
                'answer_choices' :['47,500' , '13,750' , '23,600' , '24,600'],
                'correct' : '23,600'
                } ,
        'peru': {
                'question': 'what is orange and sounds like a parrot?____',
                'answer_choices' :['tomato' , 'orange' , 'potato' , 'carrot'],
                'correct' : 'carrot'
                } ,
        'afghanistan': {
                'question' : "'Snake, Elephant, Tapir, ...",
                'answer_choices' :['Rabbit' , 'Bear' , 'Ostrich' , 'Whale'],
                'correct' : 'Rabbit'
                }
        }


turtle.register_shape('girl.gif')
turtle.shape('girl.gif')
girl = turtle.clone()
turtle.hideturtle()
girl.goto(0,0)


basket=turtle.clone()
turtle.register_shape("basket3.gif")
turtle.shape("basket3.gif")
turtle.penup()
turtle.goto(340,300)
turtle.pendown()
turtle.stamp()
turtle.hideturtle()
turtle.penup()

score = turtle.clone()
score.goto(380, 300)
score.pendown()
cur_score = 0
score.write("score: " + str(cur_score))

def score_counter():
    global cur_score
    cur_score+=16
    score.clear()
    score.write("score: "  + str(cur_score))

turtle.shape("square")
turtle.resizemode("user")
white_stamp = turtle.clone()
white_stamp.shape("square")
white_stamp.goto(0,0)
white_stamp.color("white")
white_stamp.shapesize(100,100,0)

def answer_A():
    turtle.clear()
    turtle.goto(0,0)
    global country
    riddle_answer = riddle_dict[country]['answers_choices'][0] == riddle_dict[country]['correct']
    if riddle_answer == True:
        turtle.write('You answered right', font=("Ariel", 20, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        score_counter()
    else:
        turtle.write('You answered wrong', font=("Ariel", 20, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
    turtle.clear()
   
        
def answer_B():
    turtle.clear()
    turtle.goto(0,0)
    global country
    riddle_answer = riddle_dict[country]['answer_choices'][1] == riddle_dict[country]['correct']
        
    if riddle_answer == True:
        turtle.write('You answered right', font=("Ariel", 20, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        score_counter()
    else:
        turtle.write('You answered wrong', font=("Ariel", 20, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
    turtle.clear()
       
def answer_C():
    turtle.clear()
    turtle.goto(0,0)
    global country
    riddle_answer = riddle_dict[country]['answers_choices'][2] == riddle_dict[country]['correct']
        
    if riddle_answer == True:
        turtle.write('You answered right', font=("Ariel", 20, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        score_counter()
    else:
        turtle.write('You answered wrong', font=("Ariel", 20, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
    turtle.clear()
   
def answer_D():
    turtle.clear()
    turtle.goto(0,0)
    global country
    riddle_answer = riddle_dict[country]['answers_choices'][3] == riddle_dict[country]['correct']
    
    if riddle_answer == True:
        turtle.write('You answered right', font=("Ariel", 20, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
        score_counter()
    else:
        turtle.write('You answered wrong', font=("Ariel", 20, "normal"))
        time.sleep(2)
        turtle.clear()
        white_stamp.hideturtle()
    turtle.clear()
def lis():
    turtle.onkeypress(answer_A, 'a')
    turtle.onkeypress(answer_B, 'b')
    turtle.onkeypress(answer_C, 'c')
    turtle.onkeypress(answer_D, 'd')
    turtle.listen()

letters = ['a', 'b', 'c', 'd']
pos1_list= [(-SIZE_X * 0.3, SIZE_Y / 7),(-SIZE_X * 0.3, -SIZE_Y * 2 / 7),(SIZE_X * 3 / 10, SIZE_Y / 7),(SIZE_X * 3 / 10, -SIZE_Y * 2 /7)]
def riddles():
    global country, riddle_dict, letters,pos1_list
    if girl.pos() == pos_list[0]:
        country = 'ethiopia'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()
             
    if girl.pos() == pos_list[1]:
        white_stamp.showturtle()
        country = 'madagascar'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()
                    
    if girl.pos() == pos_list[2]:
        white_stamp.showturtle()
        country='chad'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()
        
    if girl.pos() == pos_list[3]:
        white_stamp.showturtle()
        country='peru'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()
            
    if girl.pos() == pos_list[-1]:
        white_stamp.showturtle()
        country='afghanistan'
        white_stamp.showturtle()
        turtle.penup()
        turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
        #turtle.showturtle()
        turtle.pendown()
        turtle.write(riddle_dict[country]['question'], font=("Ariel", 20, "normal"))
        turtle.penup()
        for n in range (4):
            turtle.goto(pos1_list[n])
            turtle.pendown()
            turtle.write(letters[n] + '. ' + riddle_dict[country]['answer_choices'][n], font=("Ariel", 20, "normal"))
            turtle.penup()
        lis()



def move_girl():
    my_pos = girl.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==UP:
        girl.goto(x_pos, y_pos + 10)
        print("Up")
    elif direction==LEFT:
        girl.goto(x_pos - 10, y_pos)
        print("Left")
    elif direction==RIGHT:
        girl.goto(x_pos + 10, y_pos)
        print("Right")
    elif direction==DOWN:
        girl.goto(x_pos, y_pos - 10)
        print("Down")

    riddles()
        
turtle.penup()
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
direction = UP
def up():
    global direction
    direction=UP
    move_girl()
    print("you pressed the up key")

direction = DOWN
def down():
    global direction
    direction=DOWN
    move_girl()
    print("you pressed the down key")

direction = LEFT
def left():
    global direction
    direction=LEFT
    move_girl()
    print("you pressed the left key")

direction = RIGHT
def right():
    global direction
    direction=RIGHT
    move_girl()
    print("you pressed the right key")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()

dictionary = {"a kind of tree you can carry in your hand ____" : 'palm tree' , "What is an astronaut's favourite meal?____" : 'Launch' , "In israel there is a doctor fot every 400 person , in Chad there is a doctor for each ____" : '23,600' , "what's orange and sounds like a parrot?____" : 'carrot' , " Snake , Elephant , Tapir , ...": 'Rabbit' }
SIZE_X = 1000
SIZE_Y = 700



stamp = turtle.clone()
stamp.shape("square")
stamp.pensize(1000)
        






    
        
    
    




