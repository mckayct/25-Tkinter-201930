"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Colton McKay.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------

    root = tkinter.Tk()


    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------

    frame1 = ttk.Frame(root, padding=100)
    frame1.grid()

    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------

    button = ttk.Button(frame1,text = "1st Button")
    button['command'] = (lambda:print_hello())
    button.grid(row = 0, column = 1)

    ##^PrintsHello when pressed

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid(row = 1, column = 0)

    my_entry_box2 = ttk.Entry(frame1)
    my_entry_box2.grid(row = 1, column = 2)

    ###^Attachs the entry boxes to the frame

    print_entry_button = ttk.Button(frame1, text='Print entry')
    print_entry_button['command'] = (lambda:
                                     print_hello_goodbye(my_entry_box))
    print_entry_button.grid(row = 2, column = 0)

    #^ creates a button that runs a command when pressed, for entry box 1

    button = ttk.Button(frame1, text="Print a word _ many times")
    button['command'] = (lambda: print_string_n_times(my_entry_box,my_entry_box2))
    button.grid(row = 2, column = 2)

    #^ creats a new button that needs to print the string from the 1st entry box
    # the n number of times that is written in the second entry box

    root.mainloop()

    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------

def print_hello():
    print("Hello")
    return

def print_hello_goodbye(entry_box):
    if entry_box.get() == 'ok':
        print("Hello")
    else:
        print('Goodbye')

def print_string_n_times(entry_box, entry_box2):
    word = entry_box.get()
    number = entry_box2.get()
    n = int(number)
    for k in range(n):
        print(word)


    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------



    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
