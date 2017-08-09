import turtle
turtle.register_shape('girl.gif')
turtle.shape('girl.gif')



turtle.clone()
turtle.register_shape("basket3.gif")
turtle.shape("basket3.gif")
turtle.penup()
turtle.goto(340,300)
turtle.pendown()
turtle.stamp()
turtle.hideturtle()
turtle.penup()

##turtle.clone()
##turtle.register_shape('bananas3.gif')
##turtle.shape('bananas3.gif')
##turtle.goto(340,300)
##turtle.stamp()
##turtle.penup()

score = turtle.clone()
score.goto(380, 300)
score.pendown()
cur_score = '0'
score.write("score: " + cur_score)

def score_couter():
    if riddle_answer == true:
        int(cur_score)
        cur_score+=16
        str(cur_score)
        score.goto(380,300)
        score.write("                              ", color="white")
        score.goto(380,300)
        score.write("score: "  + "cur_score")






    
        
    
    




