"""Write a python program which will keep adding stream of numbers inputted by User.
The adding stops as soon as user presses q key on the keyboard"""

sum = 0

while True:
    userInput = input("Enter the item price or press 'q' to quit: ")
    if userInput != 'q':
        sum = sum + int(userInput)
        print(f"Your order total so far {sum}")
    else:
        print(f"Your total bill is {sum}. Thanks for coming")
        break

"""checking git"""
