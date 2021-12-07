# Jonathan Lee and Joshua Burton

import turtle as trtl
import random as rand
import pyglet

wn = trtl.Screen()
wn.setup(width=.55, height=.475)
paddle_shape = 'pong_paddle.gif'
ball_shape = 'pong_ball.gif'
background = 'pong_background.gif'
pause_button = 'pause_button.gif'
hit_sound = 'pong_hit.mp3'

wn.addshape(paddle_shape)
wn.addshape(ball_shape)
wn.addshape(background)
wn.addshape(pause_button)
sound = pyglet.media.load(hit_sound, streaming=False)

wn.bgpic(background)
wn.bgcolor('black')
paddle1 = trtl.Turtle(shape=paddle_shape)
paddle2 = trtl.Turtle(shape=paddle_shape)
ball = trtl.Turtle(shape=ball_shape)
writer1 = trtl.Turtle()
writer2 = trtl.Turtle()
pauser = trtl.Turtle(shape=pause_button)
name_writer = trtl.Turtle()

name_writer.speed(0)
name_writer.pencolor('white')
name_writer.hideturtle()
pauser.hideturtle()
writer1.hideturtle()
writer2.hideturtle()
paddle1.pu()
paddle2.pu()
ball.pu()
ball.speed(0)
paddle1.speed(0)
paddle2.speed(0)
writer1.speed(0)
writer2.speed(0)
paddle1.setpos(-275, 0)
paddle2.setpos(275, 0)
writer1.setpos(-220, 100)
writer2.setpos(220, 100)
writer1.pencolor('white')
writer2.pencolor('white')
player1 = input('Player 1\'s name: ').upper()
player2 = input('Player 2\'s name: ').upper()
end_score = int(input('What are you playing to? (<10): '))

def leaderboard():
    name_writer.pu()
    font_set = ('Times New Roman', 35, 'bold')
    name_writer.goto(-265, 140)
    name_writer.pd()
    name_writer.write(player1 + ':', font=('Times New Roman', 15, 'normal'))
    name_writer.pu()
    name_writer.goto(180, 140)
    name_writer.pd()
    name_writer.write(player2 + ':', font=('Times New Roman', 15, 'normal'))
    writer1.write(str(player1_score), font=font_set)
    writer2.write(str(player2_score), font=font_set)

pauser.pu()
pauser.goto(-150, 0)
pauser.pencolor('white')
pauser.write('PRESS \'SPACE\' TO START', font=('Times New Roman', 20, 'bold'))
started = False
def manage_game():
    global started
    if started:
        started = False
        pauser.pu()
        pauser.goto(0, 0)
        pauser.showturtle()
    else:
        started = True
        pauser.clear()
        pauser.hideturtle()
        move_ball()

def quit_game():
    global started
    started = False
    pauser.hideturtle()
    pauser.goto(-85, 0)
    pauser.write('QUIT? (y/n)', font=('Times New Roman', 20, 'bold'))

def yes():
    wn.bye()

def no():
    global started
    pauser.clear()
    started = True
    move_ball()
    
dx_list = [-5, 5]
player1_score = 0
player2_score = 0
width = wn.window_width()
height = wn.window_height()
minX, maxX = -width/2, width/2
ball.dx = 35
ball.dy = rand.choice(dx_list)
def move_ball():
    while started:
        wn.update()
        ball.pu()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        collision()
        leaderboard()
        end_game()
        if ball.dx > 0 and started:
            if ball.ycor() >= 175 or ball.ycor() <= -175:
                ball.dy *= -1
            if ball.xcor() > maxX:
                ball.reset()
                ball.dx *= -1
                update_p1_score()
        if ball.dx < 0 and started:
            if ball.ycor() >= 175 or ball.ycor() <= -175:
                ball.dy *= -1
            if ball.xcor() < minX:
                ball.reset()
                ball.dx *= -1
                update_p2_score()


def collision():
    if abs(ball.xcor() - paddle1.xcor()) <= 10 and abs(ball.ycor() - paddle1.ycor()) <= 50:
        sound.play()
        ball.setx(paddle1.xcor() + 15)
        ball.dx *= -1
        
    if abs(ball.xcor() - paddle2.xcor()) <= 10 and abs(ball.ycor() - paddle2.ycor()) <= 50:
        sound.play()
        ball.setx(paddle2.xcor() - 15)
        ball.dx *= -1
    
def end_game():
    global started
    if player1_score == end_score or player2_score == end_score:
        started = False
        wn.clear()
        wn.bgcolor('blue')
        writer1 = trtl.Turtle()
        writer1.hideturtle()
        writer1.pu()
        writer1.goto(-200, 0)
        writer1.pencolor('white')
        writer1.pd()
        if player1_score > player2_score:
            writer1.write(f'Congratulations, {player1}!', font=('Times New Roman', 27, 'bold'))
        else:
            writer1.write(f'Congratulations, {player2}!', font=('Times New Roman', 27, 'bold'))

def update_p1_score():
    global player1_score
    writer1.clear()
    player1_score += 1
    
def update_p2_score():
    global player2_score
    writer2.clear()
    player2_score += 1

def paddle1_move_up():
    if paddle1.ycor() <= 125 and started:
        paddle1.goto(paddle1.xcor(), paddle1.ycor() + 15)

def paddle1_move_down():
    if paddle1.ycor() >= -125 and started:
        paddle1.goto(paddle1.xcor(), paddle1.ycor() - 15)

def paddle2_move_up():
    if paddle2.ycor() <= 125 and started:
        paddle2.goto(paddle2.xcor(), paddle2.ycor() + 15)

def paddle2_move_down():
    if paddle2.ycor() >= -125 and started:
        paddle2.goto(paddle2.xcor(), paddle2.ycor() - 15)

wn.onkeypress(paddle1_move_up, 'w')
wn.onkeypress(paddle1_move_down, 's')
wn.onkeypress(paddle2_move_up, 'Up')
wn.onkeypress(paddle2_move_down, 'Down')
wn.onkeypress(manage_game, 'space')
wn.onkeypress(quit_game, 'q')
wn.onkeypress(yes, 'y')
wn.onkeypress(no, 'n')

wn.listen()
wn.mainloop()