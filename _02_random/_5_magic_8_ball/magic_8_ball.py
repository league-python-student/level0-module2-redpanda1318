import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring("Enter a question for the magic 8-ball to answer")

    # Make a variable and initialize it to a random number between 0 and 3
    number = random.randint(0,3)
    print(number)


    # If the random number is 0
    if number == 0:
        print("Yes")

        # tell the user "Yes"

    # If the random number is 1
    if number == 1:
        print("No")

        # tell the user "No"

    # If the random number is 2
    if number == 2:
        print("Maybe you should ask Google?")

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if number == 3:
        print("Yes No Maybe So")

        # write your own answer
