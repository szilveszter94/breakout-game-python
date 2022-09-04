from turtle import Screen
from paddle import Paddle
from border import Border
from ball import Ball
import time
from elements import draw_elements
from scoreboard import Scoreboard, high_score_reader


# Main function
def main():
    # set constants
    SCORE = 0
    game = True
    # set screen
    screen = Screen()
    screen.tracer(0)
    screen.bgcolor('#EEEEEE')
    screen.setup(width=800, height=600)
    screen.listen()
    # set border, ball, square elements and paddle
    Border()
    ball = Ball(0, 0)
    element_list = draw_elements()
    paddle = Paddle()
    # set highscore text
    high_score = high_score_reader()
    scoreboard = Scoreboard(high_score)
    # configure keyboard keys
    screen.onkeypress(fun=paddle.move_right, key="d")
    screen.onkeypress(fun=paddle.move_left, key="a")
    # start game with infinite loop
    while game:
        ball.move_forward()
        time.sleep(0.04)
        ball.collision_with_wall()
        # check the ball collision with paddle
        if ball.distance(paddle) < 30 and ball.ycor() < -230:
            ball.middle_collision_with_paddle()
        # check the paddle position and manage the ball movement
        elif ball.distance(paddle) < 110 and ball.ycor() < -230:
            if ball.xcor() < paddle.xcor():
                ball.left_side_collision_with_paddle()
            else:
                ball.right_side_collision_with_paddle()
        # check the ball collision with the square elements and hide that elements
        for i in element_list:
            if ball.distance(i) < 40:
                element_list.remove(i)
                i.hideturtle()
                SCORE += 1
                scoreboard.update_scoreboard(high_score)
                ball.bouncing()
            # when all elements cleared, draw elements again
            if len(element_list) == 0:
                element_list = draw_elements()
        # check if the ball is out
        if ball.ycor() < -280:
            ball.game_over()
            # overwrite the highscore
            if SCORE > high_score:
                with open('highscore.txt', 'w') as f:
                    f.write(f'{SCORE}')
            # show restart after the end of the game
            restart = screen.textinput("Game Over", "\nDo you want to restart ? (y/n)")
            if restart == "y":
                # restart
                screen.clearscreen()
                main()
            else:
                break
        screen.update()
    screen.mainloop()


# start the app
if __name__ == '__main__':
    main()
