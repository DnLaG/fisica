from interface import admin
from interface import ideal
from interface import balistica

if __name__ == '__main__':
    # Create the entire GUI program
    program = ideal.Interface()

    # Start the GUI event loop
    program.window.mainloop()
