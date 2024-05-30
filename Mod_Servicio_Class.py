from tkinter import *
from tkinter import ttk
from tkinter import Tk
import tkinter as tk
from customtkinter import CTk, CTkEntry



class Modify_Serv:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def validar_float(self, entrada):
        if entrada == "":
            return True  # Permite la eliminación del texto
        try:
            # Verificar si el valor puede ser convertido a float
            float(entrada)
        except ValueError:
            return False  # La entrada no es un número válido

        # Permitir solo un punto decimal
        if entrada.count('.') > 1:
            return False

        return True

    def create_interface(self):
        self.root = Toplevel(self.master)
        self.root.attributes("-fullscreen", True)
        self.root.configure(background="white")

        self.titleFrame = Frame(self.root, background="#c9bbd2")
        self.titleFrame.pack(fill=X)

        self.titleLabel = Label(self.titleFrame, text="Modificar servicio: ", font='Kameron 50', background="#c9bbd2")
        self.titleLabel.grid(row=0, column=0)

        self.infoFrame = tk.Frame(self.root, background="white")
        self.infoFrame.pack(fill=X)


        self.dateLabel = Label(self.infoFrame, text="Fecha: ", font='Kameron 15', background="white")
        self.dateLabel.grid(row=1, column=0, padx=45, pady=10, sticky=W)
        self.dateEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75)
        self.dateEntry.grid(row=1, column=1)
        self.clientRepLabel = Label(self.infoFrame, text="Reporte del cliente: ", font='Kameron 15', background="white")
        self.clientRepLabel.grid(row=2, column=0, padx=45, pady=10, sticky=W)
        self.clientRepEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75)
        self.clientRepEntry.grid(row=2, column=1)
        self.idFallLabel = Label(self.infoFrame, text="ID de falla: ", font='Kameron 15', background="white")
        self.idFallLabel.grid(row=3, column=0, padx=45, pady=10, sticky=W)

        self.opciones = ["Opción 1", "Opción 2", "Opción 3"]

        self.id_Falla = ttk.Combobox(self.infoFrame, values=self.opciones)
        self.id_Falla.set("Seleccione el tipo de falla")
        self.id_Falla.configure(state='readonly')
        self.id_Falla.grid(row=3, column=1)

        self.inspTecLabel = Label(self.infoFrame, text="Inspección del técnico: ", font='Kameron 15', background="white")
        self.inspTecLabel.grid(row=4, column=0, padx=45, pady=10, sticky=W)
        self.inspTecEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75)
        self.inspTecEntry.grid(row=4, column=1)
        self.jobDoneLabel = Label(self.infoFrame, text="Trabajo realizado", font='Kameron 15', background="white")
        self.jobDoneLabel.grid(row=5, column=0, padx=45, pady=10, sticky=W)
        self.jobDoneEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75)
        self.jobDoneEntry.grid(row=5, column=1)
        self.refsLabel = Label(self.infoFrame, text="Refacciones", font='Kameron 15', background="white")
        self.refsLabel.grid(row=6, column=0, padx=45, pady=10, sticky=W)
        self.refsEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75)
        self.refsEntry.grid(row=6, column=1)
        self.obsLabel = Label(self.infoFrame, text="Observaciones: ", font='Kameron 15', background="white")
        self.obsLabel.grid(row=7, column=0, padx=45, pady=10, sticky=W)
        self.obsEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75)
        self.obsEntry.grid(row=7, column=1)
        self.plaqueLabel = Label(self.infoFrame, text="Placa", font='Kameron 15', background="white")
        self.plaqueLabel.grid(row=8, column=0, padx=45, pady=10, sticky=W)
        self.plaqueEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75)
        self.plaqueEntry.grid(row=8, column=1)
        self.manPowLabel = Label(self.infoFrame, text="Mano de obra: ", font='Kameron 15', background="white")
        self.manPowLabel.grid(row=9, column=0, padx=45, pady=10, sticky=W)

        self.vcmd = self.root.register(self.validar_float)

        self.manPowEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd, "%P"), font=('Inter Medium', 11), width=75
        )

        self.manPowEntry.grid(row=9, column=1)
        self.piecesCostLabel= Label(self.infoFrame, text="Costo de las piezas: ", font='Kameron 15', background="white")
        self.piecesCostLabel.grid(row=10, column=0, padx=45, pady=10, sticky=W)

        self.piecesCostEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd, "%P"), font=('Inter Medium', 11), width=75
        )

        self.piecesCostEntry.grid(row=10, column=1)
        self.servTotalLabel = Label(self.infoFrame, text="Total del servicio: ", font='Kameron 15', background="white")
        self.servTotalLabel.grid(row=11, column=0, padx=45, pady=10, sticky=W)

        self.servTotalEntry = CTkEntry(
            self.infoFrame, validate="key", validatecommand=(self.vcmd, "%P"), font=('Inter Medium', 11), width=75
        )

        self.servTotalEntry.grid(row=11, column=1)

        self.btnFrame = Frame(self.root, background="white")
        self.btnFrame.pack(side=LEFT)

        self.endRegBtn = Button(self.btnFrame, text="Listo para modificar", font=('Inter Medium', 10), background="#c9bbd2",
                                borderwidth=0, width=18, padx=9, pady=15,
                                command=lambda: self.app.change_interface(self.app.servicios_instance))
        self.endRegBtn.grid(row=0, column=0, padx=45)
        self.exitBtn = Button(self.btnFrame, text="Salir", font=('Inter Medium', 10), background="#c9bbd2",
                              borderwidth=0, width=18, padx=9, pady=15,
                              command=lambda: self.app.change_interface(self.app.servicios_instance))

        self.exitBtn.grid(row=0, column=1, padx=50)
