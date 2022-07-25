import sys
import tkinter as tk
from tkinter import filedialog
import glob
import os.path
import subprocess

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


def run():

    subprocess.call([x])


def option_changed(*args):

    global x
    for x in glob.glob("E:\\ajin abhi\\*.bat"):
        os.path.basename(x)
        if os.path.basename(x) == variable.get():
            print(x)

    Button4 = tk.Button(root)
    Button4.place(relx=0.381, rely=0.8, height=24, width=87)
    Button4.configure(activebackground="beige")
    Button4.configure(activeforeground="black")
    Button4.configure(background="#00caca")
    Button4.configure(compound='left')
    Button4.configure(disabledforeground="#a3a3a3")
    Button4.configure(foreground="#000000")
    Button4.configure(highlightbackground="#d9d9d9")
    Button4.configure(highlightcolor="black")
    Button4.configure(pady="0")
    Button4.configure(text='''Execute .bat''', command=run)


def browseFiles():
    filename = filedialog.askdirectory(parent=root, initialdir="E:\\ajin abhi", title='Please select a directory')
    Entry1 = tk.Entry(root, textvariable=entry_text)
    Entry1.place(relx=0.354, rely=0.333, height=30, relwidth=0.529)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="TkFixedFont")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")
    entry_text.set(filename)

    OPTIONS = [os.path.basename(x) for x in glob.glob("E:\\ajin abhi\\*.bat")]

    # default value
    Text2 = tk.OptionMenu(root, variable, *OPTIONS, command=option_changed)
    Text2.place(relx=0.354, rely=0.567, height=30, relwidth=0.529)
    Text2.configure(background="white")
    Text2.configure(font="TkTextFont")
    Text2.configure(foreground="black")


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        self.entry_text = None
        top.geometry("367x300+660+227")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("API Automation Tool")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#ffffff")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.082, rely=0.03, height=28, width=303)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="#80ffff")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(compound='left')
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Label1.configure(foreground="#00caca")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''WebService Automation''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.054, rely=0.333, height=14, width=79)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Project Name''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.027, rely=0.567, height=16, width=102)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''TestCase Name''')

        Text2 = tk.Text(self.top)
        Text2.place(relx=0.354, rely=0.567, height=30, relwidth=0.529)
        Text2.configure(background="white")
        Text2.configure(font="TkTextFont")
        Text2.configure(foreground="black")

        self.Button3 = tk.Button(self.top)
        self.Button3.place(relx=0.681, rely=0.8, height=24, width=87)
        self.Button3.configure(activebackground="beige")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#00caca")
        self.Button3.configure(compound='left')
        self.Button3.configure(cursor="fleur")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Cancel''')

        self.Button4 = tk.Button(self.top, state=tk.DISABLED)
        self.Button4.place(relx=0.381, rely=0.8, height=24, width=87)
        self.Button4.configure(activebackground="beige")
        self.Button4.configure(activeforeground="black")
        self.Button4.configure(background="#00caca")
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Execute .bat''')

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.054, rely=0.8, height=24, width=87)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#00caca")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Browse Project''', command=browseFiles)

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.354, rely=0.333, height=30, relwidth=0.529)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")


def main(*args):
    '''Main entry point for the application.'''
    global root, filename
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1, entry_text, variable, OPTIONS
    _top1 = root
    _w1 = Toplevel1(_top1)
    entry_text = tk.StringVar()
    variable = tk.StringVar()
    variable.set("Select TestCase Name")
    root.mainloop()


if __name__ == '__main__':
    main()
