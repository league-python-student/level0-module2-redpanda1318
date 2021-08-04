import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()


    thing = str(random.randint(0,20))
    thingy = random.randint(1,2)
    thingo = random.randint(2,3)
    thingi = random.randint(3,4)
    thinge = random.randint(4,5)
    thingoo = random.randint(5,6)
    # TODO 1) Get 6 random numbers to put on your lottery ticket
    messagebox.showinfo(title = 'number', message= ""+ thing )

    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
