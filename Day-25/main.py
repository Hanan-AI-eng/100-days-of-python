import turtle
from turtle import Screen,Turtle
import pandas

#screen
screen=Screen()
screen.title("U.S State Game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# record of the correct answers
correct_answer=[]

# make a box and convert the text into Title case
answer_state = screen.textinput(title='Guess the State',prompt="What's another state's name?").title().strip()

#get the data from the file
states_data=pandas.read_csv("50_states.csv")

# all the states
all_state=states_data["state"].tolist()



while len(correct_answer)< 50:

    #get out the game
    if answer_state== "Exit":
        # make a list of the one that got missed
        missed_state = states_data[~states_data["state"].isin(correct_answer)]
        missed_state.to_csv("States to learn.csv",index=False)
        break

    # check if the data that the use provide is in the csv file
    if answer_state in all_state:

        # get the location from each state
        state= states_data[states_data["state"]== answer_state]
        location_state_data_X=state["x"].iloc[0]
        location_state_data_Y=state["y"].iloc[0]

        #put the correct answer in the screen
        answer=Turtle()
        answer.hideturtle()
        answer.penup()
        answer.goto(location_state_data_X, location_state_data_Y)
        answer.write(answer_state)
        correct_answer.append(answer_state)

    # ask again to show the score
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 States Correct",
                                        prompt="What's another state's name?").title().strip()