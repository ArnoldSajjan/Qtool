import glob
import subprocess
import sys
import tkinter as tk
import tkinter.ttk as ttk
from os.path import exists
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40'  # X11 color: #666666
_ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
_ana2color = 'beige'  # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'


def close():
    root.destroy()


def run():
    try:
        subprocess.call([x])
        Label2 = tk.Label(root)
        Label2.place(relx=0.100, rely=0.770, height=21, width=104)
        Label2.configure(anchor='w')
        Label2.configure(background="#ffffff")
        Label2.configure(compound='left')
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(foreground="#00FF00")
        Label2.configure(text='''Successful''')
    except:
        Label2 = tk.Label(root)
        Label2.place(relx=0.100, rely=0.770, height=21, width=104)
        Label2.configure(anchor='w')
        Label2.configure(background="#ffffff")
        Label2.configure(compound='left')
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(foreground="#FF0000")
        Label2.configure(text='''Failed''')


def test_option(*args):
    global x

    for x in glob.glob("E:\\ajin abhi\\" + variable.get() + "\\" + test_variable.get()):
        os.path.basename(x)

        if os.path.basename(x) == test_variable.get():
            Button1 = tk.Button(root)
            Button1.place(relx=0.430, rely=0.770, height=23, width=67)
            Button1.configure(activebackground="beige")
            Button1.configure(activeforeground="black")
            Button1.configure(background="#00cccc")
            Button1.configure(compound='left')
            Button1.configure(disabledforeground="#a3a3a3")
            Button1.configure(foreground="#000000")
            Button1.configure(highlightbackground="#d9d9d9")
            Button1.configure(highlightcolor="black")
            Button1.configure(pady="0")
            Button1.configure(text='''Execute''', command=run)
            break


def option_changed(*args):
    global TEST_OPTIONS, test_variable
    try:

        test_variable = tk.StringVar()
        test_variable.set("Select Test Case Name")
        TEST_OPTIONS = [os.path.basename(x) for x in glob.glob("E:\\ajin abhi\\" + variable.get() + "\\*.bat")]
        Listbox2 = tk.OptionMenu(root, test_variable, *TEST_OPTIONS, command=test_option)
        Listbox2.place(relx=0.418, rely=0.566, relheight=0.105, relwidth=0.53)
        Listbox2.configure(background="white")
        Listbox2.configure(disabledforeground="#a3a3a3")
        Listbox2.configure(font="-family {Segoe UI} -size 9")
        Listbox2.configure(foreground="#000000")
    except:
        test_variable = tk.StringVar()
        test_variable.set("OOPS !!")
        TEST_OPTIONS = ["No Files Found"]
        Listbox2 = tk.OptionMenu(root, test_variable, *TEST_OPTIONS)
        Listbox2.place(relx=0.418, rely=0.566, relheight=0.105, relwidth=0.53)
        Listbox2.configure(background="white")
        Listbox2.configure(disabledforeground="#a3a3a3")
        Listbox2.configure(font="-family {Segoe UI} -size 9")
        Listbox2.configure(foreground="#000000")


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("409x312+660+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("QAutomation")
        top.configure(background="#ffffff")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.049, rely=0.064, relheight=0.856
                          , relwidth=0.907)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.162, rely=0.075, height=44, width=259)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.Label1.configure(foreground="#009595")
        self.Label1.configure(text='''Legacy Guardian''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.054, rely=0.412, height=21, width=104)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Application Name''')

        OPTIONS = [os.path.basename(x) for x in glob.glob("E:\\ajin abhi\\*")]
        self.Listbox1 = tk.OptionMenu(self.Frame1, variable, *OPTIONS, command=option_changed)
        self.Listbox1.place(relx=0.404, rely=0.412, relheight=0.100, relwidth=0.59)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="-family {Segoe UI} -size 9")
        self.Listbox1.configure(foreground="#000000")

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.081, rely=0.599, height=21, width=94)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Test Case Name''')

        self.Listbox2 = tk.Listbox(self.Frame1)
        self.Listbox2.place(relx=0.404, rely=0.599, relheight=0.100, relwidth=0.59)
        self.Listbox2.configure(background="white")
        self.Listbox2.configure(disabledforeground="#a3a3a3")
        self.Listbox2.configure(font="TkFixedFont")
        self.Listbox2.configure(foreground="#000000")

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.674, rely=0.824, height=24, width=67)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#00cccc")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Cancel''', command=close)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.809, rely=0.075, height=21, width=64)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 7")
        self.Label4.configure(foreground="#00cece")
        self.Label4.configure(text='''QAutomation''')


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1, variable, OPTIONS
    _top1 = root
    variable = tk.StringVar()
    variable.set("Select Application Name")
    _w1 = Toplevel1(_top1)
    root.mainloop()


if __name__ == '__main__':
    main()
