# Anh Vo
# 2037824
# Lab 11.27

# Function to input player roster information.
def input_roster():
    roster = {}
    for i in range(5):
        jersey_number = int(input("Enter player {}'s jersey number:\n".format(i + 1)))
        rating = int(input("Enter player {}'s rating:\n".format(i + 1)))
        print()
        roster[jersey_number] = rating
    return roster


# Function to output the entire player roster.
def output_roster(roster):
    print("ROSTER")
    for jersey_number in sorted(roster):
        rating = roster[jersey_number]
        print("Jersey number: {}, Rating: {}".format(jersey_number, rating))


# Function to output players with a rating above a specified threshold.
def output_above_rating(roster):
    rating_threshold = int(input("Enter a rating:\n"))
    print("ABOVE", rating_threshold)
    for jersey_number, rating in sorted(roster.items()):
        if rating > rating_threshold:
            print("Jersey number: {}, Rating: {}".format(jersey_number, rating))


# Function to add a new player to the roster.
def add_player(roster):
    jersey_number = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter the player's rating:\n"))
    roster[jersey_number] = rating


# Function to remove a player from the roster.
def remove_player(roster):
    jersey_number = int(input("Enter a jersey number:\n"))
    if jersey_number in roster:
        del roster[jersey_number]


# Function to update the rating of an existing player in the roster.
def update_rating(roster):
    jersey_number = int(input("Enter a jersey number:\n"))
    if jersey_number in sorted(roster):
        rating = int(input("Enter a new rating for player:\n"))
        roster[jersey_number] = rating


# Function to return the menu options.
def menu():
    return "\nMENU\n" \
           "a - Add player\n" \
           "d - Remove player\n" \
           "u - Update player rating\n" \
           "r - Output players above a rating\n" \
           "o - Output roster\n" \
           "q - Quit\n"


# Function to process the user's choice and perform the corresponding action.
def choice(choice, roster):
    if choice == "o":
        output_roster(roster)
    elif choice == "a":
        add_player(roster)
    elif choice == "d":
        remove_player(roster)
    elif choice == "u":
        update_rating(roster)
    elif choice == "r":
        output_above_rating(roster)


# Main part of the program
roster = input_roster()  # Input player roster.
output_roster(roster)    # Output the roster initially.

menu_options = menu()    # Get the menu options.
user_choice = ""

# Main loop to keep displaying the menu and processing user's choice until 'q' is selected (Quit).
while user_choice != "q":
    print(menu_options)
    user_choice = input("Choose an option:\n")
    choice(user_choice, roster)  # Process the user's choice.
