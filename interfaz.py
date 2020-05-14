from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk



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




btn = Button(window, text="Agregar", command=clicked)
btn1 = Button(window, text="Calcular", command=calcular,state=tk.DISABLED)

btn.grid(column=5, row=180)
btn1.grid(column=5, row=120)

window.mainloop()
