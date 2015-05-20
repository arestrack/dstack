#!/usr/bin/python

# -*- coding: utf-8 -*-

import Tkinter as tk

class TextViewer(tk.Frame):
    def __init__(self, parent=None, text='', file=None):
        tk.Frame.__init__(self, parent)
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.createwidgets()

    def createwidgets(self):
        text = tk.Text(self)
        text.pack(expand=tk.YES, fill=tk.BOTH)

class TextInput(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack(side=tk.TOP, fill=tk.X)
        self.createwidgets()

    def createlabelentry(self, text):
        iframe = tk.Frame(self)
        ilabel = tk.Label(iframe, text=text)
        ientry = tk.Entry(iframe)
        ilabel.pack(side=tk.LEFT, fill=tk.BOTH)
        ientry.pack(side=tk.RIGHT, fill=tk.BOTH)
        return iframe

    def createwidgets(self):
        wframe = tk.Frame(self)
        base_entry = self.createlabelentry(text='BaseAddr :')
        stack_entry = self.createlabelentry(text='StackAddr:')
        base_entry.pack(side=tk.TOP, fill=tk.BOTH)
        stack_entry.pack(side=tk.BOTTOM, fill=tk.BOTH)
        
class FileInput(tk.Frame):
    pass
    
    
class 

class SimpleApp(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.createApp()

    def createApp(self):
        textviewer = TextViewer(self)
        textinput = TextInput(self)

        textviewer.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
        textinput.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)

    def say_hi(self):
        print("hi there, everyone!")


def setApp2Center(rt):
    scnWidth  = rt.winfo_screenwidth()
    scnHeight = rt.winfo_screenheight()
    tmpcnf = '%dx%d+%d+%d'%(scnWidth/2,scnHeight/2,scnWidth/4,scnHeight/4)
    rt.geometry(tmpcnf)

def main():
    root = tk.Tk()
    root.title('dstack')
    setApp2Center(root)
    app = SimpleApp(root)
    app.mainloop()

if __name__ == "__main__":
    main()
