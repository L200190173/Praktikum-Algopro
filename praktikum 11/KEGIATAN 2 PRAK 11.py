from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Kalkulator')

L0 = Label(app, text="Angka 1")
L0.grid(row=0, column=0, sticky="W")

angka1 = IntVar()
E0 = Entry(app, textvariable=angka1)
E0.grid(row=0, column=1, columnspan=3)

L1 = Label(app, text="Angka 2")
L1.grid(row=1, column=0, sticky="W")

angka2 = IntVar()
E1 = Entry(app, textvariable=angka2)
E1.grid(row=1, column=1, columnspan=3)

HL = Label(app, text="Hasil")
HL.grid(row=3, column=0, sticky="W")

HA = Label(app)
HA.grid(row=3, column=2, sticky="W")

def press(param):
    angka = 0
    if param == 1:
        angka = angka1.get() + angka2.get()
    elif param == 2:
        angka = angka1.get() - angka2.get()
    elif param == 3:
        angka = angka1.get() * angka2.get()
    else:
        angka = angka1.get() / angka2.get()

    HA.config(text="Result is %d" % angka)
              

B1 = Button(app, text="+", width=8, command= lambda : press(1))
B1.grid(row=2, column=0)

B2 = Button(app, text="-", width=8, command= lambda : press(2))
B2.grid(row=2, column=1)

B3 = Button(app, text="x", width=8, command= lambda : press(3))
B3.grid(row=2, column=2)

B4 = Button(app, text="/", width=8, command= lambda : press(4))
B4.grid(row=2, column=3)

app.mainloop()
