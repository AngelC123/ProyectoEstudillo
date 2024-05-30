from tkinter import *
from customtkinter import CTk, CTkEntry


class Agregar_Cliente:
    def __init__(self, master, app):
        self.app = app
        self.master=master

    def validar_numeros_mayusculas(self, entrada):
        if entrada == "":
            return True  # Permite la eliminación del texto

        # Verificar si todos los caracteres son dígitos o letras mayúsculas
        if all(caracter.isdigit() or caracter.isupper() for caracter in entrada):
            return True
        else:
            return False

    def validar_alphabet(self, entrada):
        if entrada == "":
            return True  # Permite la eliminación del texto

        # Verificar si todos los caracteres son del alfabeto y no hay más de un espacio consecutivo
        for i, caracter in enumerate(entrada):
            if not (caracter.isalpha() or (caracter.isspace() and (i == 0 or entrada[i - 1].isalpha()))):
                return False
        return True

    def validar_numeros(self, entrada):
        if entrada == "":
            return True  # Permite la eliminación del texto

        # Verificar si todos los caracteres son dígitos
        if all(caracter.isdigit() for caracter in entrada):
            return True
        else:
            return False

    def create_interface(self):
        self.root=Toplevel(self.master)

        self.root.attributes("-fullscreen", True)
        self.root.configure(background="white")

        self.titleFrame=Frame(self.root, background="#c9bbd2")
        self.titleFrame.pack(fill=X)

        self.titleLabel=Label(self.titleFrame, text="Agregar cliente", background="#c9bbd2", font='Kameron 50')
        self.titleLabel.grid(row=0, column=0)

        self.infoFrame=Frame(self.root, background="white")
        self.infoFrame.pack(fill=X)

        self.nameLabel = Label(self.infoFrame, text="Nombre: ", font='Kameron 25', background="white")
        self.nameLabel.grid(row=0, column=0, padx=45, pady=15, sticky=W)
        self.rfcLabel = Label(self.infoFrame, text="RFC: ", font='Kameron 25', background="white")
        self.rfcLabel.grid(row=1, column=0, padx=45, pady=15, sticky=W)
        self.telLabel = Label(self.infoFrame, text="Teléfono: ", font='Kameron 25', background="white")
        self.telLabel.grid(row=2, column=0, padx=45, pady=15, sticky=W)
        self.mailLabel = Label(self.infoFrame, text="Correo: ", font='Kameron 25', background="white")
        self.mailLabel.grid(row=3, column=0, padx=45, pady=15, sticky=W)

        self.vcmd = self.root.register(self.validar_alphabet)
        self.vcmd_1 = self.root.register(self.validar_numeros)
        self.vcmd_2 = self.root.register(self.validar_numeros_mayusculas)

        self.nameEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd, "%P"), font=('Inter Medium', 11), width=75
        )

        self.nameEntry.grid(row=0, column=1)

        self.rfcEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd_2, "%P"), font=('Inter Medium', 11), width=75
        )
        self.rfcEntry.grid(row=1, column=1)

        self.telEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd_1, "%P"), font=('Inter Medium', 11), width=75
        )

        self.telEntry.grid(row=2, column=1)
        self.mailEntry = Entry(self.infoFrame, font=("Inter Medium", 11), width=30)
        self.mailEntry.grid(row=3, column=1)

        self.btnFrame = Frame(self.root, background="white")
        self.btnFrame.pack(fill=X)
        self.addBtn = Button(self.btnFrame, text="Agregar", font='Kameron 15', borderwidth=0, width=10, pady=2,
                             command=lambda: self.app.change_interface(self.app.clients_instance))
        self.addBtn.grid(row=0, column=0, padx=50, pady=20)
        self.exitBtn = Button(self.btnFrame, text="Salir", font='Kameron 15', borderwidth=0, width=10, pady=2,
                              command=lambda: self.app.change_interface(self.app.clients_instance))
        self.exitBtn.grid(row=0, column=1, padx=50, pady=20)