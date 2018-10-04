""" SOFTWARE DESARROLLADO POR ESTUDIANTES PARA ESTUDIANTES. """
#!/usr/bin/env python3


import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #Base Resolution
        self.pack(padx=200,pady=200)
        #Widget title name
        self.master.title("[WIP] Visualizador Grafico")
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.master.maxsize(1024,1024)
app.mainloop()
