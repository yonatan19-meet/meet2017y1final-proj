import turtle
stamp = turtle.clone()
stamp.shape("square")
stamp.pensize(1000)
dictionary = {"a kind of tree you can carry in your hand ____" : 'palm tree' , "what is the flag of madagascar?____" : 'flag' , "In israel there is a doctor fot every 400 person , in Chad there is a doctor for each ____" : '23,600' , "what's orange and sounds like a parrot?____" : 'carrot' , " Snake , Elephant , Tapir , ...": 'Rabbit' }
SIZE_X = 1000
SIZE_Y = 700
def answer_a():
        turtle.clear()
        turtle.goto(0,0)
        turtle.write('You answered right')

turtle.onkeypress(answer_a,'a')
turtle.listen()
def riddles():
	if monkey.pos() == ethiopia:
                
		stamp.stamp()
		turtle.penup()
		turtle.goto(-SIZE_X * 0.3, SIZE_Y * 3 / 7)
		turtle.pendown()
		turtle.write("a kind of tree you can carry in your hand____")
		turtle.penup()
		turtle.goto(-SIZE_X * 0.3, SIZE_Y / 7)
		turtle.pendown()
		turtle.write("a/palm tree")
		turtle.penup()
		turtle.goto(-SIZE_X * 0.3, -SIZE_Y *2 / 7)
		turtle.pendown()
		turtle.write("b/lost tree")
		turtle.penup()
		turtle.goto(300, 100)
		turtle.pendown()
		turtle.write("c/apple tree")
		turtle.penup()
		turtle.goto(300, -200)
		turtle.pendown()
		turtle.write("d/dead tree")
		
##	if monkey.pos() in madagascar:
##		stamp.stamp()
##		turtle.penup()
##		turtle.goto(-300, 300)
##		turtle.pendown()
##		turtle.write("what is the flag of madagascar?____")
##		turtle.penup()
##		turtle.goto(-300, 100)
##		turtle.pendown()
##	if monkey.pos() in chad:
##		stamp.stamp()
##		turtle.penup()
##		turtle.goto(-300, 300)
##		turtle.pendown()
##		turtle.write("In israel there is a doctor for every 400 person , in Chad there is 			a doctor for each____")
##		turtle.penup()
##		turtle.goto(-300, 100)
##		turtle.pendown()
##		turtle.write("a/47,500")
##		turtle.penup()
##		turtle.goto(-300, -200)
##		turtle.pendown()
##		turtle.write("b/24,600")
##		turtle.penup()
##		turtle.goto(300, 100)
##		turtle.pendown()
##		turtle.write("c/13,750")
##		turtle.penup()
##		turtle.goto(300, -200)
##		turtle.pendown()
##		turtle.write("d/23,600")
##	if monkey.pos() in peru:
##		stamp.stamp()
##		turtle.penup()
##		turtle.goto(-300, 300)
##		turtle.write("what's orange and sounds like a parrot?____")
##	if monkey.pos() in afghanistan:
##		stamp.stamp()
##		turtle.penup()
##		turtle.goto(-300, 300)
##		turtle.write("Snake , Elephant , Tapir , ...")

		
monkey = turtle.clone()
ethiopia = monkey.pos()

riddles()
