from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview, Style


class Vehiculos:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def create_interface(self):

        self.root = Toplevel(self.master)
        self.root.attributes("-fullscreen", True)
        self.root.configure(background="white")

        self.titleFrame = Frame(self.root)
        self.titleFrame.config(bg="#c9bbd2")
        self.titleFrame.pack(fill=X)

        self.titleLabel = Label(self.titleFrame, text="Vehículos", background="#c9bbd2", font='Kameron 50')
        self.titleLabel.grid(column=0, row=0, )
    #creacion del canvas para poder mostrar una tabla de informacion
        self.canvasFrame = Frame(self.root)
        self.canvasFrame.pack(fill=X, pady=50)
        self.canvas = Canvas(self.canvasFrame, width=800, height=600, bd=0)
        self.canvas.pack(fill=X)
        self.style = Style()
        self.style.layout('Edge.Treeview', [('Edge.Treeview.treearea', {'sticky': 'nsew'})], )
        self.style.configure('Treeview.Heading',font=('Inter Medium', 14))
        self.style.configure('Treeview', font= ('Inter Medium', 12))
        self.tree = Treeview(self.canvas, style='Edge.Treeview')
        self.tree["columns"]= ("Placa", "Modelo", "Año")

        self.scrollbar = Scrollbar(self.canvas, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        #le damos formato a las columnas
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Placa", anchor=W, width=80)
        self.tree.column("Modelo", anchor=W, width=200)
        self.tree.column("Año", anchor=W, width=200)

        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("Placa", text="Placa", anchor=W)
        self.tree.heading("Modelo", text="Modelo", anchor=W)
        self.tree.heading("Año", text="Año", anchor=W)

        #le agregamos filas a la tabla
        data = [
            ("FIG-123", "Task 1", "Project 1"),
            ("FIG-122", "Task 2", "Acme GTM"),
            ("FIG-121", "Write blog post for demo day", "Acme GTM"),
            ("FIG-120", "Publish blog page", "Website launch"),
        ]
        for item in data:
            self.tree.insert("", "end", values=item)

        self.tree.pack(side=TOP, fill=X)

        self.btnFrame = Frame(self.root, background="white")
        self.btnFrame.pack(side=LEFT)

        self.addVehicleBtn = Button(self.btnFrame, text="Agregar vehículo", font='Kameron 15', border=0,
                                command=lambda: self.app.change_interface(self.app.add_vehicle_instance))
        self.addVehicleBtn.grid(row=0, column=0, padx=45)
        self.modifyVehicleBtn = Button(self.btnFrame, text="Modificar vehículo", font='Kameron 15', border=0,
                                       command=lambda: self.app.change_interface(self.app.modify_vehicle_instance))
        self.modifyVehicleBtn.grid(row=0, column=2, padx=45)
        self.deleteVehicleBtn = Button(self.btnFrame, text="Eliminar vehículo", font='Kameron 15', border=0,
                                       command=lambda: self.app.change_interface(self.app.delete_vehicle_instance))
        self.deleteVehicleBtn.grid(row=0, column=3, padx=45)
        self.exitBtn = Button(self.btnFrame, text="Salir", font='Kameron 15', border=0,
                              command=lambda: self.app.change_interface(self.app.clients_instance))
        self.exitBtn.grid(row=0, column=4, padx=45)




