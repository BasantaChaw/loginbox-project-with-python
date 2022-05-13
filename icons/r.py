from tkinter import*
from tkinter import Label, Button
from tkinter import font
from turtle import back, left, width
from PIL import Image, ImageTk
import os


def tab1():

    frame1 = Frame(home, width=206, height=720,
                   background='#f0f8ff', relief=FLAT)
    frame1.place(x=10, y=12)

    def tab2():
        frame1.destroy()
        
        global openimage
        openimage = ImageTk.PhotoImage(Image.open('icons/open.png'))
        but = Button(home, image=openimage, activebackground='red',command=tab1,
                      relief=FLAT, bd=0)
        but.place(x=15, y=20)


        def backing():
            but.destroy()
            tab1()
           


        closeimage = ImageTk.PhotoImage(Image.open('icons/close.png'))
        close = Button(frame1, image=closeimage, activebackground='red',
                   background='#f0f8ff', relief=FLAT, bd=0,command=backing)
        close.place(x=95, y=20)

        
    global closeimage
    closeimage = ImageTk.PhotoImage(Image.open('icons/close.png'))
    close = Button(frame1, image=closeimage, activebackground='red',
                   background='#f0f8ff', relief=FLAT, bd=0,command=tab2)
    close.place(x=95, y=20)
    btn1 = Button(frame1, text='Menu1', width=20, height=4, relief=FLAT, bd=0, font=(
        'Arial', 12, font.BOLD), activebackground='lightgreen')
    btn1.place(x=10, y=1664)
    btn2 = Button(frame1, text='menu2', width=20, height=4, relief=FLAT, bd=0, font=(
        'Arial', 12, font.BOLD), activebackground='lightgreen')
    btn2.place(x=10, y=252)
    btn3 = Button(frame1, text='Menu3', width=20, height=4, relief=FLAT, bd=0, font=(
        'Arial', 12, font.BOLD), activebackground='lightgreen')
    btn3.place(x=10, y=339)
    btn4 = Button(frame1, text='Menu4', width=20, height=4, relief=FLAT, bd=0, font=(
        'Arial', 12, font.BOLD), activebackground='lightgreen')
    btn4.place(x=10, y=426)
    btn5 = Button(frame1, text='Menu5', width=20, height=4, relief=FLAT, bd=0, font=(
        'Arial', 12, font.BOLD), activebackground='lightgreen')
    btn5.place(x=10, y=513)
    btn6 = Button(frame1, text='Menu6', width=20, height=4, relief=FLAT, bd=0, font=(
        'Arial', 12, font.BOLD), activebackground='lightgreen')
    btn6.place(x=10, y=600)


home = Tk()
tab1()
home.state("zoomed")
home.config(background='#cbd3e1')
home.mainloop()
