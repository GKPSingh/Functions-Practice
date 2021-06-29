# "Write a function that takes a color as an argument.
# If color if red, function should print Today’s winner is red team
# If color if blue, function should print Today’s winner is blue team
# If color if green, function should print Today’s winner is green team
# For any other colors, function should print No game today"
def team_color(color):
    if color == 'red':
        print(f"Today's winner is {color} team")
    elif color == 'blue':
        print(f"Today's winner is {color} team")
    elif color == 'green':
        print(f"Today's winner is {color} team")
    else:
        print(f"No Game Today")


team_color('black')