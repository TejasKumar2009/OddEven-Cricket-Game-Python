import random

# Functions
# Game Function
def game(user_decision, user_runs, comp_runs, comp_winner, user_out, comp_out):

    user_out = user_out
    comp_out = comp_out
    if user_decision==0 or comp_winner!=None and comp_winner==False:
        while True:
            if user_out == False or user_out < 10:
                user_runs_input = int(input("Enter Number for Runs (1-6) : "))
                comp_balls_input = random.randint(1, 6)
                if user_runs_input < 7:
                    if user_runs_input == comp_balls_input:
                        if user_out==False:
                            user_out = True
                        else:
                            user_out += 1
                        print(f"You are out on {user_runs} Runs !")
                        # if user_out == 10:
                        #     print(f"Computer won by {user_runs-comp_runs} Runs !")
                        

                    else:
                        user_runs+=user_runs_input
                        print(f"Your Runs : {user_runs}/{user_out}")
                    
                else:
                    print("You are entering the number which is not allowed or above 6. Please Try Again!")
                print(f"Target for Computer : {user_runs+1}")
                    
            elif user_out == 10 and comp_out < 10:
                user_balls_input = int(input("Enter Number for Bowling (1-6) : "))
                comp_runs_input = random.randint(1, 6)
                if user_balls_input < 7:
                      
                    if comp_runs_input == user_balls_input:
                        print(f"Computer are out on {comp_runs} Runs !")
                        
                        if comp_runs < user_runs:
                            if comp_out==False:
                                comp_out = True
                            else:
                                comp_out += 1
                                # if comp_out == 10:
                                    # print(f"You won by {user_runs-comp_runs} Runs !")

                    else:
                        comp_runs+=comp_runs_input
                        print(f"Computer Runs : {comp_runs}/{comp_out}")
                        if comp_runs < user_runs:
                            print(f"Computer Needs {user_runs-comp_runs+1}")
                        else:
                            print(f"Computer won the game by {10-comp_out} Wickets !")
                            exit()
                else:
                    print("You are entering the number which is not allowed or above 6. Please Try Again!")


    if user_decision!=0 or comp_winner!=None and comp_winner==True:
        while True:
            if comp_out == False or comp_out < 10:
                user_balls_input = int(input("Enter Number for Bowling (1-6) : "))
                comp_runs_input = random.randint(1, 6)
                if user_balls_input < 7:
                    if comp_runs_input == user_balls_input:
                        print(f"Computer are out on {comp_runs} Runs !")
                        print(f"Target for You : {comp_runs+1}")
                        if comp_out==False:
                            comp_out = True
                        else:
                            comp_out += 1

                    else:
                        print(f"Computer Number : {comp_runs_input}")
                        comp_runs+=comp_runs_input
                        print(f"Computer Runs : {comp_runs}/{comp_out}")
                else:
                    print("You are entering the number which is not allowed or above 6. Please Try Again!")

            elif comp_out == True or user_out < 10:
                user_runs_input = int(input("Enter Number for Runs (1-6) : "))
                comp_balls_input = random.randint(1, 6)
                if user_runs_input < 7:
                    if user_runs_input == comp_balls_input:
                        if user_runs < comp_runs:
                            if user_out==False:
                                user_out = True
                                print("True means 1 wicket!")
                            else:
                                user_out += 1
                                print("Wicket")
                            print(f"You are out on {user_runs} Runs !")
                        

                    else:
                        print(f"Computer Number : {comp_balls_input}")
                        user_runs+=user_runs_input
                        print(f"Your Runs : {user_runs}/{user_out}")
                        if user_runs < comp_runs:
                            print(f"You Needs {comp_runs-user_runs+1} Runs !")
                        else:
                            print(f"You won the game by {10-user_out} Wickets !")
                            exit()
                    
                else:
                    print("You are entering the number which is not allowed or above 6. Please Try Again!")

# Toss
toss_options = ["Even", "Odd"]
toss_options_bb = ["Batting", "Bowling"]
user_decision = None
comp_decision = None
comp_winner = None

user_out = 0
comp_out = 0
print("10 wicket match!")

user_toss_choice = int(input("What you will choose Even(0) or Odd(1) : "))
if user_toss_choice == 0:
    comp_toss_choice = 1
elif user_toss_choice == 1:
    comp_toss_choice = 0
else:
    print("Please Enter 0 or 1. Try Again!!")
    exit()
user_toss_number = int(input("Enter the number between 1 and 6 for toss : "))
comp_toss_number = random.randint(1, 6)
print("Your Number", user_toss_number)
print("Computer Number", comp_toss_number)
# print()
if (user_toss_number+comp_toss_number)%2==0:
    win_choice = 0
    print("Even Won !")
else:
    win_choice = 1
    print("Odd Won !")

if win_choice==user_toss_choice:
    user_decision = int(input("Congo! You won the toss what do you want to choose (Bat-0, Ball-1) : "))
else:
    comp_decision = random.choice(toss_options_bb)
    if comp_decision==toss_options_bb[0]:
        comp_winner=True
        print("Computer Won The Toss and decided to Bat First !")
    elif comp_decision==toss_options_bb[1]:
        comp_winner=False
        print("Computer Won The Toss and decided to Ball First !")

# Game
user_runs = 0
comp_runs = 0

game(user_decision, user_runs, comp_runs, comp_winner, user_out, comp_out)
