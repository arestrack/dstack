#!/usr/bin/python

# -*- coding: UTF-8 -*-


import Tkinter as tk

class TextViewer(tk.Frame):
    def __init__(self, parent=None, text='', file=None):
        tk.Frame.__init__(self, parent)
        #self.pack(expand=tk.YES, fill=tk.BOTH)
        self.createwidgets()

    def createwidgets(self):
        text = tk.Text(self)
        text.pack(expand=tk.YES, fill=tk.BOTH)
        self.text = text

    def appendText(self,text=''):
        self.text.insert(tk.END, text)

class TextInput(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        #self.pack(expand=tk.YES, fill=tk.Y)
        self.createWidgets()

    def createWidgets(self):
        bframe = tk.Frame(self)
        sframe = tk.Frame(self)

        blabel = tk.Label(bframe, text='BaseAddr :')
        bentry = tk.Entry(bframe)
        blabel.pack(side=tk.LEFT)
        bentry.pack(side=tk.RIGHT)

        slabel = tk.Label(sframe, text='StackAddr:')
        sentry = tk.Entry(sframe)
        slabel.pack(side=tk.LEFT)
        sentry.pack(side=tk.RIGHT)

        bframe.pack(side=tk.TOP, padx=10, pady=10)
        sframe.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.bentry = bentry
        self.sentry = sentry

    def getBaseAddr(self):
        return self.bentry.get()

    def getStackAddr(self):
        return self.sentry.get()

    def getAddrOffset(self):
        baseAddr = self.getBaseAddr()
        stackAddr = self.getStackAddr()
        offsetAddr = hex( int(stackAddr,16)-int(baseAddr,16) )
        return offsetAddr

class FileInput(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        #self.pack(expand=tk.YES, fill=tk.BOTH)
        self.createWidgets()

    def createWidgets(self):
        pentry = tk.Entry(self)
        upbutton = tk.Button(self, text='unsupport', command=self.sorry)
        pentry.pack(side=tk.LEFT, padx=10)
        upbutton.pack(side=tk.RIGHT, ipadx=10)

        self.pentry = pentry
        self.upbutton = upbutton

    def sorry(self):
        print 'Oh,Sorry,\nNow Unsupport Load File Dialog...'

    def getFilePath(self):
        filePath = self.pentry.get()
        return filePath


class InputViewer(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        #self.pack(expand=tk.YES, fill=tk.BOTFH)
        self.createWidgets()

    def createWidgets(self):
        textinput = TextInput(self)
        fileinput = FileInput(self)
        dstackbutton = tk.Button(self, text='dstack', command=self.commit)

        textinput.pack(anchor='w')
        fileinput.pack(anchor='w', pady=10)
        dstackbutton.pack(ipadx=10, pady=20)

        self.textinput = textinput
        self.fileinput = fileinput
        self.dstackbutton = dstackbutton

    def commit(self):
        # 1. sftp file
        # 2. dissassemble
        # 3. get text
        pass

    def getAddrOffset(self):
        return self.textinput.getAddrOffset()

    def getFilePath(self):
        return self.fileinput.getFilePath()



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

        self.inputviewer = inputviewer
        self.textviewer = textviewer

        self.inputviewer.dstackbutton['command'] = self.runApp

    def runApp(self):
        offsetAddr = self.inputviewer.getAddrOffset()
        filePath = self.inputviewer.getFilePath()

        self.textviewer.appendText(offsetAddr+'\n')
        self.textviewer.appendText(filePath)


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
