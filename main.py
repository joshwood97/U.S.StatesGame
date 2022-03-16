import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game.")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []


# Function to find coor for each state to add to .csv
#def get_mouse_click_coor(x, y):
    #print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)

# Create a loop to allow the user to keep guessing
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct ", prompt="Guess another state name. ").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_you_need_to_learn.csv")
        break

    # Check if the guess is amongst the 50 states
        #If right, create a turtle to write the name of the state at the correct x,y coor
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # Write the correct guess onto the map
        t.write(answer_state)



turtle.mainloop()
