from tkinter import *

class Eliminar_Vehiculo:
    def __init__(self, master, app):
        self.master = master
        self.app = app


    def create_interface(self):
        self.root = Toplevel(self.master)
        self.root.geometry("450x225")

        self.titleFrame = Frame(self.root)
        self.titleFrame.config(background="#ec6868")
        self.titleFrame.pack(fill=X)

        self.titleLabel = Label(self.titleFrame, text="Eliminar vehículo", font='Kameron 20', background="#ec6868")
        self.titleLabel.grid(row=0, column=0)

        self.msgFrame = Frame(self.root)
        self.msgFrame.pack()
        self.msgLabel = Label(self.msgFrame, text="¿Está seguro de eliminar este \n vehículo?", font='Kameron 15', pady=15)
        self.msgLabel.grid(row=0, column=0)

        self.btnFrame = Frame(self.root)
        self.btnFrame.pack(expand=True)
        self.acceptBtn = Button(self.btnFrame, text="Aceptar", font=("Inter Medium", 8), background="#ec6868", borderwidth=0,
                                width=10, pady=2,
                                command=lambda: self.app.change_interface(self.app.vehicle_instance))
        self.acceptBtn.grid(row=0, column=0, padx=50)
        self.cancelBtn = Button(self.btnFrame, text="Cancelar", font=("Inter Medium", 8), background="#acacac",
                                borderwidth=0, width=10, pady=2,
                                command=lambda: self.app.change_interface(self.app.vehicle_instance))
        self.cancelBtn.grid(row=0, column=1, padx=35)