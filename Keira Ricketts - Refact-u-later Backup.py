"""
I didn't come up with the 'jokes' this calculator uses.
They're mainly a product of the internet people created by 
overlapping the numbers with their mirrored images.
"""

#variables
num1 = 0
num2 = 0
answer = 0
num_round = 0
name = ""
jokes = ""
operation = ""
second_operation = ""
again = ""

six_seven = "hehehe six sevennnnnnnn"

#program logic
print("Keira's Four Functions Calculator")
print("")

#function for allowing user to try again or to break code
def try_again():
    again = input("Try again? (yes/no): ")
    if again == "no":
        print("Great! Time to do math in your own!")
        print("Thanks for using my four functions calculator, " + name + "!")
        print("Have a great day! :)")
    elif again == "yes":
        print("Great!")
        print("")

#function for addition
def add(num1, num2):
    answer = round(num1 + num2, num_round)
    solution = name + ", the sum of " + str(num1) + " plus " + str(num2) + " is " + str(answer) + "."
    return solution

#function for subtraction
def subtract(num1, num2):
    answer = round(num1 - num2, num_round)
    solution = name + ", the sum of " + str(num1) + " minus " + str(num2) + " is " + str(answer) + "."
    return solution

#function for multiplication
def multiply(num1, num2):
     answer = round(num1 * num2, num_round)
     solution = name + ", the product of " + str(num1) + " times " + str(num2) + " is " + str(answer) + "."
     return solution

#function for division
def divide(num1, num2):
    if num2 == 0:
        solution = name + ", the quotient of " + str(num1) + " divided by " + str(num2) + " is undefined!"
    else:
        answer = round(num1 / num2, num_round)
        solution = name + ", the quotient of " + str(num1) + " divided by " + str(num2) + " is " + str(answer) + "."
    return solution

#function for exponents
def exponent(num1, num2):
    answer = round(num1 ** num2, num_round)
    solution = name + ", " + str(num1) + " to the power of " + str(num2) + " is " + str(answer) + "."
    return solution

#asks user for name and operation
name = input("Hi! What's your name?: ")
print("")
print("Nice to meet you, " + name + ".")
jokes = input("Do you want to hear some jokes, " + name + "? (yes/no): ")
print("")

#asks user if they want to hear jokes
if jokes == "yes" or jokes == "Yes":
    print("Great! There's gonna be quite a few!")
    print("Though, all of them are in the addition operation.")
    print("Add two of the same numbers to unlock the jokes :)")
    print("Start at 1 + 1!")
elif jokes == "no" or jokes == "No":
    print("Aw man! I was ready to crack some jokes!")
    print("Anyway, what operation would like to perform?")
else:
    print("Sorry, I didn't understand what you've said.")
    print("")
    try_again() == "no"
    jokes = input("Do you want to hear some jokes, " + name + "? (yes/no): ")

#loops program
while True:

        #asks user what decimal they want to round to
        try:
            print("")
            print("Before I calculate, what decimal would you like me to round to?")
            num_round = int(input("Enter a number. Example: 0 = nearest integer, 1 = tenth place, etc: ")) 
            print("")
        except ValueError:
            print("Please enter a whole number.")
            continue

        #asks what operation
        print("Operations: add(1), subtract(2), multiply(3), divide(4), or exponent(5)")
        operation = input("Enter operation #: ")
        
        #follows through with the operation
        if operation == "1" or operation == "2" or operation == "3" or operation == "4" or operation == "5":
            try:
                num1 = float(input("Enter 1st number: "))
                num2 = float(input("Enter 2nd number: "))
                print("")
            except ValueError:
                print("Do you best to enter a whole number, please.")
                continue
            
            #performs addition
            if operation == "1":
                solution = add(num1, num2)
                
                #makes very funny jokes about the shapes of numbers
                if jokes == "yes":
                    if num1 == 1 and num2 == 1:
                        print("1 + 1 = Window, " + name + ".")
                        print("Jk it's actually 2")
                    elif num1 == 2 and num2 == 2:
                        print("2 + 2 = Fish")
                        print("Wait no, its 4. Oops...")
                    elif num1 == 3 and num2 == 3:
                        print("3 + 3 = 8")
                        print("Oh, nvm its 6.")
                    elif num1 == 4 and num2 == 4:
                        print("4 + 4 = Arrow")
                        print("That's not right...")
                        print("Oh, right, this time it's 8")
                    elif num1 == 5 and num2 == 5:
                        print("5 + 5 = 10")
                        print("I know you were expecting a very hilarious joke rn.")
                        print("But unfortunately, 5 can't follow the same logic...")
                        print("Neither can 6. But 7 can.")
                    elif num1 == 7 and num2 == 7:
                        print("7 + 7 = Triangle")
                        print("Get it?")
                        print("When you turn them upside down, mirrow them, and connect them...")
                        print("They make a triangle! Ain't that hilarious?")
                    elif num1 == 8 and num2 == 8:
                        print("8 + 8 = Butterfl- wait, its actually 16. Oopsies, my bad.")
                        print("Well, you reached the end of the jokes.")
                        print("Have fun doing actual math, " + name + "!")
                    elif num1 == 6 and num2 == 7 or num1 == 7 and num2 == 6:
                        solution = add(num1, num2)
                        print(six_seven)
                        print("")
                        print("Anyway, " + solution)
                    else:
                        solution = add(num1, num2)
                        print(solution)
            
                #actually calculates the sum
                else: 
                    solution = add(num1, num2)
                    print(solution)
            
            #performs subtraction
            elif operation == "2":
                if num1 == 6 and num2 == 7 or num1 == 7 and num2 == 6:
                    print(six_seven)
                    print("")
                solution = subtract(num1, num2)
                print(solution)
            
            #performs multiplication
            elif operation == "3":
                if num1 == 6 and num2 == 7 or num1 == 7 and num2 == 6:
                    print(six_seven)
                    print("")
                solution = multiply(num1, num2)
                print(solution)
                        
            #performs division
            elif operation == "4":
                if num1 == 6 and num2 == 7 or num1 == 7 and num2 == 6:
                    print(six_seven)
                    print("")
                solution = divide(num1, num2)
                print(solution)

            #operates exponents
            elif operation == "5":
                if num1 == 6 and num2 == 7 or num1 == 7 and num2 == 6:
                    print(six_seven)
                    print("")
                solution = exponent(num1, num2)
                print(solution)
            
            #asks user if they want to use calculator again
            print("")
            second_operation = input("Another operation, " + name + "? (yes/no): ")
            if second_operation == "no" or second_operation == "no thanks":
                print("Great! Time to do math on your own!")
                print("Thanks for using my four functions calculator, " + name + "!")
                print("Have a great day! :)") 
                break
                
        #breaks loop and allows user to try again
        else:
            print("Invalid operation.")
            if try_again() == "no":
                break
