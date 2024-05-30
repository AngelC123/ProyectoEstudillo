from tkinter import *


class Hoja_Servicio:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def create_interface(self):
        self.root = Toplevel(self.master)
        self.root.attributes("-fullscreen", True)
        self.root.configure(background="white")

        self.titleFrame = Frame(self.root, background="#c9bbd2")
        self.titleFrame.pack(fill=X)

        self.titleLabel = Label(self.titleFrame, text="Hoja de servicio", font='Kameron 50', background="#c9bbd2")
        self.titleLabel.grid(row=0, column=0)

        self.infoFrame = Frame(self.root, background="white")
        self.infoFrame.pack(fill=X)

        self.orderNumLabel = Label(self.infoFrame, text="No. de Orden: ", font='Kameron 15', background="white")
        self.orderNumLabel.grid(row=0, column=0, padx=45, sticky=W)
        self.dateLabel = Label(self.infoFrame, text="Fecha: ", font='Kameron 15', background="white")
        self.dateLabel.grid(row=1, column=0, padx=45, pady=10, sticky=W)
        self.clientRepLabel = Label(self.infoFrame, text="Reporte del cliente: ", font='Kameron 15', background="white")
        self.clientRepLabel.grid(row=2, column=0, padx=45, pady=10, sticky=W)
        self.idFallLabel = Label(self.infoFrame, text="ID de falla: ", font='Kameron 15', background="white")
        self.idFallLabel.grid(row=3, column=0, padx=45, pady=10, sticky=W)
        self.inspTecLabel = Label(self.infoFrame, text="Inspección del técnico: ", font='Kameron 15',
                                  background="white")
        self.inspTecLabel.grid(row=4, column=0, padx=45, pady=10, sticky=W)
        self.jobDoneLabel = Label(self.infoFrame, text="Trabajo realizado", font='Kameron 15', background="white")
        self.jobDoneLabel.grid(row=5, column=0, padx=45, pady=10, sticky=W)
        self.refsLabel = Label(self.infoFrame, text="Refacciones", font='Kameron 15', background="white")
        self.refsLabel.grid(row=6, column=0, padx=45, pady=10, sticky=W)
        self.obsLabel = Label(self.infoFrame, text="Observaciones: ", font='Kameron 15', background="white")
        self.obsLabel.grid(row=7, column=0, padx=45, pady=10, sticky=W)
        self.plaqueLabel = Label(self.infoFrame, text="Placa", font='Kameron 15', background="white")
        self.plaqueLabel.grid(row=8, column=0, padx=45, pady=10, sticky=W)
        self.manPowLabel = Label(self.infoFrame, text="Mano de obra: ", font='Kameron 15', background="white")
        self.manPowLabel.grid(row=9, column=0, padx=45, pady=10, sticky=W)
        self.piecesCostLabel = Label(self.infoFrame, text="Costo de las piezas: ", font='Kameron 15',
                                     background="white")
        self.piecesCostLabel.grid(row=10, column=0, padx=45, pady=10, sticky=W)
        self.servTotalLabel = Label(self.infoFrame, text="Total del servicio: ", font='Kameron 15', background="white")
        self.servTotalLabel.grid(row=11, column=0, padx=45, pady=10, sticky=W)

        self.orderNumEntry = Entry(self.infoFrame, font=("Inter Medium", 11), width=75, state=DISABLED)
        self.orderNumEntry.grid(row=0, column=1)
        self.dateEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.dateEntry.grid(row=1, column=1)
        self.clientRepEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.clientRepEntry.grid(row=2, column=1)
        self.idFallEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.idFallEntry.grid(row=3, column=1)
        self.inspTecEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.inspTecEntry.grid(row=4, column=1)
        self.jobDoneEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.jobDoneEntry.grid(row=5, column=1)
        self.refsEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.refsEntry.grid(row=6, column=1)
        self.obsEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.obsEntry.grid(row=7, column=1)
        self.plaqueEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.plaqueEntry.grid(row=8, column=1)
        self.manPowEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.manPowEntry.grid(row=9, column=1)
        self.piecesCostEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.piecesCostEntry.grid(row=10, column=1)
        self.servTotalEntry = Entry(self.infoFrame, font=('Inter Medium', 11), width=75, state=DISABLED)
        self.servTotalEntry.grid(row=11, column=1)

        self.btnFrame = Frame(self.root, background="white")
        self.btnFrame.pack(side=LEFT)


        self.exitBtn = Button(self.btnFrame, text="Salir", font=('Inter Medium', 10), background="#c9bbd2",
                              borderwidth=0, width=18, padx=9, pady=15,
                              command=lambda: self.app.change_interface(self.app.servicios_instance))
        self.exitBtn.grid(row=0, column=1, padx=50)
