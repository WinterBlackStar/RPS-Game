def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)
    
            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response
            
        except ValueError:
            print(error)
    

# Main Routine Starts here

# Initialise game variables

mode = "regular"
rounds_played = 0

print()
print("✂️ 📄💎 Rock / Paper / Scissors Game💎📄✂️")

# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for inifinte mode: ")


if num_rounds == "infinite":
    mode = "inifinte"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Round headings
    if mode == "infinite":
        rounds_heading = f"\n000 rounds {rounds_played + 1} (Infinite Mode) 000"
    else:
        rounds_heading = f"\n 💿💿💿 round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "inifinte":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area
