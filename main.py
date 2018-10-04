""" SOFTWARE DESARROLLADO POR ESTUDIANTES PARA ESTUDIANTES. """
#!/usr/bin/env python3


from tkinter import*
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #Base Resolution
        #Widged Tittle
        self.master.title("[WIP] Visualizador Grafico")
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = Button(self.master)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row = 0, column = 0, pady = 5, padx =5)

        self.quit = Button(self.master, command = self.quit_selection, text = "Close")
        self.quit.grid(row = 0, column = 1, pady = 5, padx =5)

    def say_hi(self):
        print("Hello")

    def quit_selection(self):
        close = messagebox.askquestion("Close","Desea salir?",icon='warning')
        if close == 'yes':
            self.master.quit()


root = Tk()
app = Application(master=root)
app.master.minsize(200,200)
app.master.maxsize(1024,1024)
app.mainloop()
