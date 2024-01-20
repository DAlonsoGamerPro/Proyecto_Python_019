from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Mirador de Imágenes")
root.geometry("500x500")
root.config(bg="turquoise1")

label_planet_image = Label(root,bg="red",highlightthickness=5,borderwidth=2,relief=SOLID)
btn = Button(root,text="Abrir Imagen")
btn2 = Button(root,text="Rotar Imagen")
label_credits = Label(root,bg="turquoise1",text="Hecho por Diego Alonso, con la ayuda de BYJU´S Learning y la maestra Ivonne Margarita Pinto Herrera")

label_planet_image.place(relx=0.5,rely=0.5,anchor=CENTER)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)
btn2.place(relx=0.5,rely=0.8,anchor=CENTER)
label_credits.place(relx=0.5,rely=0.98,anchor=CENTER)

root.mainloop()