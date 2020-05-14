# Import specific libraries
import random
import matplotlib.pyplot as plt

# Create function for simulating die roll
# The die takes values from 1 to 100. If the number is between 1 and 51,
# the house wins. If the number is between 52 and 100, the player wins.

def rolldice():

    # Create a dice which rolls 1-100
    dice = random.randint(1, 100)

    # Check to see the result
    if dice <= 51:
        # Player loses because it rolls less than 51
        return False
    if dice > 51 & dice <= 100:
        # Player wins because it rolls greater than 51 and less than 100
        return True

# Define a function for the play which takes 3 arguments :
# 1. total_funds = total money in hand the player is starting with
# 2. wager_amount = the betting amount each time the player plays
# 3. total_plays = the number of times the player bets on this game

def play(total_funds, wager_amount, total_plays):

    # Create empty lists for :
    # 1.Play_number
    play_num = []
    # 2.Funds available
    funds = []
    # 3.Final Fund
    final_funds = []

    # Start with play number 1 to simulate the first roll
    player_num = 1

    # If number of plays is less than the max number of plays we have set
    while player_num <= total_plays:  # total_plays is brought in as a global variable
        # If we win
        if rolldice(): # if we won, the previous "rolldice" function will return True
            # Add the money to our funds
            total_funds = total_funds + wager_amount
            # Append the play number
            play_num.append(player_num)
            # Append the new fund amount
            funds.append(total_funds)
        # If the house wins
        else:
            # Subtract the wager from our funds
            total_funds = total_funds - wager_amount
            # Append the play number
            play_num.append(player_num)
            # Append the new fund amount
            funds.append(total_funds)

        # Increase the play number by 1
        player_num = player_num + 1

    # Line plot of funds over time
    plt.plot(play_num, funds)
    final_funds.append(funds[-1])
    return final_funds

# Call the function to simulate the plays and calculate the remaining #funds of the player after all the bets
# Initialize the scenario number to 1
x = 1

# Create a list for calculating final funds
# Run the scenario 100 times to get a sample pool > 20
Final_funds = []
while x <= 100:
    ending_fund = play(100000, 1000, 5)
    x = x + 1

# Plot the line plot of "Account Value" vs "The number of plays"
plt.ylabel('Player Money in $')
plt.xlabel('Number of bets')
plt.show()

# Print the money the player ends with
print("The player starts the game with $100,000 and ends with $" + str(sum(ending_fund)/len(ending_fund)))