total = 0
totalLoops = 0
employeeRate = 0
loop_again = 'y'
while loop_again == 'y':
    employeeRate = float(input("What is your hourly rate? "))
    while employeeRate < 10 or employeeRate > 100:
        print("You have entered an invalid number.")
        employeeRate = float(input("What is your hourly rate? "))
    else:
        total = total + employeeRate
        totalLoops = totalLoops + 1
        print(total, totalLoops)
        loop_again = input("\nDo you want to loop again? (y to loop again): ")

# A prime number is a natural number greater than 1 that
# cannot be formed by multiplying two smaller natural
# numbers together. Given a single #, n, write a function
# to return whether or not the # is prime. Additionally,
# if the # is prime, save it into an array, a.

# the array
a = []


# check if the number is prime
# def main():
    again = 'Y'
    while again == 'Y' or again == 'y':
        # define n
        n = int(input("Enter a number to determine if it prime: "))
        # check if there is a remainder
        if n % 2 == 1:
            print("This number is prime! It has been saved to the array. ")
            a.append(n)
            if input("Would you like to see the array? Type Yes: ") == "Yes":
                for x in a:
                    print(x)
            again = input("Would you like to try a different number? Type Y/y to continue: ")
        else:
            again = input("This number is not prime! Would you like to try a different number? Type Y/y to continue: ")


# call main function
# main()

# Write code using Python Pandas to select the rows where the students' favorite color is blue or yellow and their grade is above 90.
import pandas as pd

raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
                'age': [20, 19, 22, 21],
                'favorite_color': ['blue', 'blue', 'yellow', "green"],
                'grade': [88, 92, 95, 70]}

#	age	favorite_color	grade	name
#0	20	blue	        88	    Willard Morris
#1	19	blue	        92	    Al Jennings
#2	22	yellow	        95	    Omar Mullins
#3	21	green	        70	    Spencer McDaniel


df = pd.DataFrame(raw_data) # this line reads the raw_data csv and converts it into a Panda list
df.head() # this lists ss

if df.