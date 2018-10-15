from interface import admin
from interface import ideal
from interface import balistica
from graphics import motor

if __name__ == '__main__':
    # Create the entire GUI program
    program = ideal.Interface()
    viz = motor.window

    # Start the GUI event loop
    program.window.mainloop()
