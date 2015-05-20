#!/usr/bin/python

# -*- coding: utf-8 -*-

import Tkinter as tk

class TextViewer(tk.Frame):
    def __init__(self, parent=None, text='', file=None):
        tk.Frame.__init__(self, parent)
        #self.pack(expand=tk.YES, fill=tk.BOTH)
        self.createwidgets()

    def createwidgets(self):
        text = tk.Text(self)
        text.pack(expand=tk.YES, fill=tk.BOTH)

class TextInput(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        #self.pack(expand=tk.YES, fill=tk.Y)
        self.createwidgets()

    def createlabelentry(self, text):
        iframe = tk.Frame(self)
        ilabel = tk.Label(iframe, text=text)
        ientry = tk.Entry(iframe)
        ilabel.pack(side=tk.LEFT, fill=tk.Y)
        ientry.pack(side=tk.RIGHT, fill=tk.Y)
        return iframe

    def createwidgets(self):
        wframe = tk.Frame(self)
        base_entry = self.createlabelentry(text='BaseAddr :')
        stack_entry = self.createlabelentry(text='StackAddr:')
        base_entry.pack(side=tk.TOP, fill=tk.NONE, padx=10, pady=10)
        stack_entry.pack(side=tk.BOTTOM, fill=tk.NONE, padx=10, pady=5)
        wframe.pack(side=tk.RIGHT, fill=tk.Y)
        
class FileInput(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        #self.pack(expand=tk.YES, fill=tk.BOTH)
        self.createwidgets()

    def createwidgets(self):
        path_entry = tk.Entry(self)
        upload_button = tk.Button(self, text='...')
        path_entry.pack(side=tk.LEFT, padx=10)
        upload_button.pack(side=tk.RIGHT, ipadx=10)
    
    
class InputViewer(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        #self.pack(expand=tk.YES, fill=tk.BOTH)
        self.createwidgets()

    def createwidgets(self):
        textinput = TextInput(self)
        fileinput = FileInput(self)
        dstackbutton = tk.Button(self, text='dstack')

        textinput.pack(anchor='w')
        fileinput.pack(anchor='w', pady=10)
        dstackbutton.pack(ipadx=10, pady=20)

class SimpleApp(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.createApp()

    def createApp(self):
        inputviewer = InputViewer(self)
        textviewer = TextViewer(self)

        inputviewer.pack(side=tk.LEFT, fill=tk.Y)
        textviewer.pack(expand=tk.YES, fill=tk.BOTH)
        

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
