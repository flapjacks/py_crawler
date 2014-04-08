'''
Created on Dec 19, 2012

@author: mwbarry
'''

from tkinter import *
from tkinter import ttk
#from new_crawler import get_page
import urllib.request
from urllib.error import URLError
from html.parser import HTMLParser

import command_line
        
root = Tk()
root.title('web crawler')

#style and format the overall box
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1, pad=3)
mainframe.columnconfigure(1, weight=1, pad=3)
mainframe.columnconfigure(2, weight=1, pad=3)
mainframe.rowconfigure(0, weight=1, pad=3)
mainframe.rowconfigure(1, weight=1, pad=3)
mainframe.rowconfigure(2, weight=1, pad=3)
mainframe.rowconfigure(3, weight=1, pad=3)

#create menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='new')
filemenu.add_command(label='open')
filemenu.add_separator()
filemenu.add_command(label='exit', command=mainframe.quit)

'''frame  = Frame(mainframe, height=276, width=386)
frame.pack()
frame.pack_propagate(0)
'''

text_write = Entry(mainframe)
text_write.grid(row=0, columnspan=3, sticky=W+E)
Label(mainframe, text='enter URL to find links').grid(row=1, column=0, sticky=W+E)

text_out = Text(mainframe)
text_out.grid(row=2, columnspan=3, sticky=W+E)

button = Button(mainframe, text='quit', command=mainframe.quit)
button.grid(row=3, column=2, sticky=W+E)

hi_there = Button(mainframe, text='get links', command=lambda:text_out.insert(END, command_line.get_page(text_write.get())))
hi_there.grid(row=3, column=1, sticky=W+E)

#starts the focus in the url entry box
text_write.focus()

#create instance of the crawler called app
#app = crawler(root)

root.mainloop()
'''
root = Tk()

w = Label(root, text="hello world")
w.pack()

root.mainloop()'''
 
#if __name__ == '__main__':
    #test()
    