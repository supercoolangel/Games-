computer_wins = 0
user_wins = 0
for x in range(3):
    user_pick=input("Type Rock/Paper/Scissors: ")
    options = "rock" , "paper" , "scissors"
    computer_pick = options [0 or 1 or 2]

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    if user_pick== "rock":
        print(rock)
    elif user_pick== "paper":
            print(paper)
    elif user_pick== "scissors":
            print(scissors)
    else:
        print(" I did not understnasd your answer " )
            

    if computer_pick== "rock":
        print(rock)
    elif computer_pick== "paper":
            print(paper)
    elif computer_pick== "scissors":
            print(scissors)
            

    if user_pick=="rock" and computer_pick=="scissors":
        print("You won ! ")
        user_wins +=1
    elif user_pick=="paper" and computer_pick=="rock":
        print("You won ! ")
        user_wins +=1
    elif user_pick=="scissors" and computer_pick=="paper":
        print("You won ! ")
        user_wins +=1
    elif user_pick == computer_pick:
        print("It's a Tie !")
    else:
        print("You lost!")
        computer_wins +=1

    print("Computer won " + str(computer_wins) + " times")
    print("User wins " + str(user_wins) + " times")
    if x == [0,1]:
        print("Try 1 more time !")
    else:
        print(" ")
print("Goodbye!")


    

