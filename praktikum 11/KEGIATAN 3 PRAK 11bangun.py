from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Judul Aplikasi')

L0 = Label(app, text="Bangun Geometri", font=("Arial", 16))
L0.grid(row=0, column=0, sticky="W")

DESC = Label(app, text="Bola adalah bangun yang dibentuk oleh tak hingga lingkaran berjari-jari sama panjang dan berpusat pada satu titik yang sama. Bola hanya memiliki 1 sisi.", wraplength=250)
DESC.grid(row=1, sticky="W")

DIMENSI  = Label(app, text="Jajar genjang merupakan geometri tiga dimensi")
DIMENSI.grid(row=2, sticky="W")

CONTOH = Label(app, text="Contoh geometri bola adalah bola basket")
CONTOH.grid(row=3, sticky="W")

L1 = Label(app, text="Parameter 1")
L1.grid(row=4, column=0, sticky="W")

param1 = IntVar()
E2 = Entry(app, textvariable=param1)
E2.grid(row=4, column=1)

HL = Label(app, text="Luas")
HL.grid(row=6, column=0, sticky="W")

HA = Label(app)
HA.grid(row=6, column=1, sticky="W")

def press():
    angka = param1.get() ** 2 * 3.14
    HA.config(text=angka)
    

B1 = Button(app, text="Hitung", width=8, command= lambda : press())
B1.grid(row=6, column=3)

app.mainloop()
