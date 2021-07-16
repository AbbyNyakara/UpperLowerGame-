import random

# Display the art
from art import logo,vs
print(logo)

# Generate a random account from the game data
from game_data import data

# Game score
score = 0

# Putting the data into a printable format
def generate (account_info):
    '''Takes account input from dictionary values and gives a printable output'''
    account_name = account_info['name']
    account_profession = account_info['description']
    account_country = account_info['country']
    return f"{account_name}, a {account_profession} from {account_country}"

def check_guess(user_guess, followers_a, followers_b):
    """checks user's guess and accounts number of followers and returns output """
    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']
    if followers_a > followers_b:
        return user_guess == 'A'
    else:
        return user_guess == 'B'

''' 
Meaning of above code 
    if followers_a > followers_b:
        if user_guess == 'A':
            return True
        else:
            return False
    elif followers_b > followers_a:
        if user_guess == 'B':
            return True
        else:
            return false 
'''

account_b = random.choice(data)

should_continue = True
while should_continue:
    # Generate two random accounts
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # Print out the info
    print(f"Compare A: {generate(account_a)}")
    print(vs)
    print(f"Against B: {generate(account_b)}")

    # ask the user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # check if the user is correct
    ## Get the follower count for each account
    follower_count_a = account_a['follower_count']
    follower_count_b = account_b['follower_count']

    # Use the if statement to check if the answer is correct
    is_right = check_guess(user_guess, follower_count_a, follower_count_b)

    # followers = data['follower_count']
    # Keep track of the follower score
    if is_right:
        score += 1
        print(f"That's right. Your total score is {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        should_continue = False








