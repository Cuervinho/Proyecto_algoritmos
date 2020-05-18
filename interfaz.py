from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os
import subprocess



window = Tk()

window.title("Ruleta Predicción Numeros")

window.geometry('600x600')

lbl = Label(window, text="Introduce tú numero")

lbl.grid(column=1, row=120)

txt = Entry(window,width=10)

txt.grid(column=2, row=120)

im= Image.open("imagen.jpg")
im= im.resize((250, 250))
photo=ImageTk.PhotoImage(im)
cv = tk.Canvas()

cv.grid(column=2, row = 0)
cv.create_image(10, 10, image=photo, anchor='nw')
contador = 0;

lbl1 = Label(window, text = "Has introducido " + str(contador) + " numeros.")
lbl1.grid(column=2, row=80)

def calcular():
    # Correr programa C++ con valores en el valores.txt
    return 0;

def clicked():
    global contador
    contador += 1
    lbl1.configure(text="Has introducido " + str(contador) + " numeros.")
    file_object = open('valores.txt', 'a')
    file_object.write(txt.get())
    file_object.write("\n")
    file_object.close()

    if contador >= 20:
        btn1['state'] = tk.NORMAL


def calcular():
    x = subprocess.getoutput('g++ ' + "proyecto.cpp")
    if x == "":                         # no error/warning messages
        m = subprocess.getoutput("a.exe")     # run the program
    else:
        print(x)
    nwin = Toplevel()
    nwin.title("Predicción")
    #photo2 = PhotoImage(file = 'image_part_'+"0"+m+".png")
    #lbl2 = Label(nwin, image = photo2)
    #lbl2.pack()
    w = Label(nwin, text= m)
    w.pack()
    nwin.mainloop()



btn = Button(window, text="Agregar", command=clicked)
btn1 = Button(window, text="Calcular", command=calcular,state=tk.DISABLED)

btn.grid(column=5, row=180)
btn1.grid(column=5, row=120)

window.mainloop()
