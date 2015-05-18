#!/usr/bin/python

# -*- coding: utf-8 -*-

import Tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()


    def createLabel(self):
        self.label = tk.Label(master=self)

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=self.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


def setApp2Center(rt, width, height):
    curWidth  = width
    curHeight = height
    scnWidth  = rt.winfo_screenwidth()
    scnHeight = rt.winfo_screenheight()
    tmpcnf = '%dx%d+%d+%d'%(curWidth,curHeight,(scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
    rt.geometry(tmpcnf)

def main():
    root = tk.Tk()
    setApp2Center(root, 200, 200)
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
