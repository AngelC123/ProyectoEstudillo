from tkinter import *
from customtkinter import CTk, CTkEntry


class Modificar_Veh:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def validar_alnum_sin_espacios(self, entrada):
        if entrada == "":
            return True  # Permite la eliminación del texto

        # Verificar si todos los caracteres son dígitos o letras mayúsculas y no hay espacios
        if all(caracter.isdigit() or caracter.isupper() for caracter in entrada) and ' ' not in entrada:
            return True
        else:
            return False

    def validar_alnum_con_espacios(self, entrada):
        if entrada == "":
            return True  # Permite la eliminación del texto

        # Verificar si todos los caracteres son dígitos, letras mayúsculas o espacios
        if all(caracter.isdigit() or caracter.isupper() or caracter.isspace() for caracter in entrada):
            return True
        else:
            return False

    def validar_numeros(self, entrada):
        # Verificar si la entrada está vacía o si contiene solo números
        if entrada == "" or entrada.isdigit():
            return True
        else:
            return False



    def create_interface(self):
        self.root = Toplevel(self.master)
        self.root.attributes("-fullscreen", True)
        self.root.configure(background="white")
        self.titleFrame = Frame(self.root, background="#c9bbd2")
        self.titleFrame.pack(fill=X)

        self.titleLabel = Label(self.titleFrame, text="Modificar vehículo", font='Kameron 50', background="#c9bbd2")
        self.titleLabel.grid(row=0, column=0)

        self.infoFrame = Frame(self.root, background="white")
        self.infoFrame.pack(fill=X)


        self.vcmd = self.root.register(self.validar_alnum_sin_espacios)
        self.vcmd_1 = self.root.register(self.validar_alnum_con_espacios)
        self.vcmd_2 = self.root.register(self.validar_numeros)


        self.plaqueLabel = Label(self.infoFrame, text="Placa: ", font='Kameron 22', background="white")
        self.plaqueLabel.grid(row=0, column=0, padx=45, pady= 15, sticky=W)
        self.modelLabel = Label(self.infoFrame, text="Modelo: ", font='Kameron 22', background="white")
        self.modelLabel.grid(row=1, column=0, padx=45, pady=15, sticky=W)
        self.yearLabel = Label(self.infoFrame, text="Año: ", font='Kameron 22', background="white")
        self.yearLabel.grid(row=2, column=0, padx=45, pady=15, sticky=W)
        self.vinLabel = Label(self.infoFrame, text="Vin: ", font='Kameron 22', background="white")
        self.vinLabel.grid(row=3, column=0, padx=45, pady=15, sticky=W)
        self.kmLabel = Label(self.infoFrame, text="Kilometraje: ", font='Kameron 22', background="white")
        self.kmLabel.grid(row=4, column=0, padx=45, pady=15, sticky=W)
        self.motorLabel = Label(self.infoFrame, text="Motor: ", font='Kameron 22', background="white")
        self.motorLabel.grid(row=5, column=0, padx=45, pady=15, sticky=W)

        self.plaqueEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd, "%P"), font=('Inter Medium', 11), width=75
        )
        self.plaqueEntry.grid(row=0, column=1)
        self.modelEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd_1, "%P"), font=('Inter Medium', 11), width=75
        )
        self.modelEntry.grid(row=1, column=1)
        self.yearEntry = Entry(self.infoFrame, font=("Inter Medium", 11), width=45)
        self.yearEntry.grid(row=2, column=1)
        self.vinEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd_1, "%P"), font=('Inter Medium', 11), width=75
        )
        self.vinEntry.grid(row=3, column=1)
        self.kmEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd_2, "%P"), font=('Inter Medium', 11), width=75
        )
        self.kmEntry.grid(row=4, column=1)
        self.motorEntry = Entry(self.infoFrame, font=("Inter Medium", 11), width=45)
        self.motorEntry.grid(row=5, column=1)

        self.btnFrame = Frame(self.root, background="white")
        self.btnFrame.pack(expand=True)

        self.addVehBtn = Button(self.btnFrame, text="Modificar", font='Kameron 15', width=15, pady=2,
                                borderwidth=0,
                                command=lambda: self.app.change_interface(self.app.vehicle_instance))
        self.addVehBtn.grid(row=0, column=0, padx=50, pady=15,sticky=W)
        self.exitBtn = Button(self.btnFrame, text="Salir", font='Kameron 15', width=15, pady=2,
                              borderwidth=0,
                              command=lambda: self.app.change_interface(self.app.vehicle_instance))
        self.exitBtn.grid(row=0, column=1, padx=50, pady=15,sticky=W)
