import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    if random_number == 1:
        print("You look great today!")

    if random_number == 2:
        print("On a scale of 1-10, you would be a 11")

    if random_number == 3:
        print("Being around you makes everything better!")

    if random_number == 4:
        print("")

    if random_number == 5:
        print("")

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
