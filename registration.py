from tabnanny import check
from tkinter import *
root = Tk()
root.geometry ("500x300")

def getvals():
    print("Aceptado")

Label(root, text="Registración del Hotel", font ="ar 15 bold").grid(row=0, column=3)

Nombre= Label(root, text= "Nombre")
Telefono= Label(root, text= "Telefono")
Género= Label(root, text= "Género")
Mododepago= Label(root, text= "Modo de pago")

Nombre.grid(row=1, column=2)
Telefono.grid(row=2, column=2)
Género.grid(row=3, column=2)
Mododepago.grid(row=4, column=2)

Nombrevalue = StringVar
Telefonovalue = StringVar
Génerovalue = StringVar
Mododepagovalue = StringVar
checkvalue= IntVar

Nombreentry = Entry(root, textvariable=Nombrevalue)
Telefonoentry = Entry(root, textvariable=Telefonovalue)
Géneroentry = Entry(root, textvariable=Génerovalue)
Mododepagoentry = Entry (root, textvariable=Mododepagovalue)

Nombreentry.grid(row=1, column=3)
Telefonoentry.grid(row=2, column=3)
Géneroentry.grid(row=3, column=3)
Mododepagoentry.grid(row=4, column=3)

#Creating Checkbox
checkbtn = Checkbutton (text= "Recordarme?", variable= checkvalue)
checkbtn.grid(row=5, column=3)

#Submit button
Button(text= "Submit", command=getvals).grid(row=6, column=3)


root.mainloop()