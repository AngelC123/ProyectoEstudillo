from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview, Style


class Clientes:
    def __init__(self, master, app):
        self.master = master
        self.app = app


    def on_right_click(self, event):
        # Obtener el elemento bajo el clic derecho
        self.item = self.tree.identify_row(event.y)
        if self.item:
            # Seleccionar el ítem en el que se ha hecho clic derecho
            self.tree.selection_set(self.item)
            # Mostrar el menú contextual
            self.menu.post(event.x_root, event.y_root)



    def create_interface(self):

        self.root = Toplevel(self.master)
        self.root.attributes("-fullscreen", True)
        self.root.configure(background="white")

        self.titleFrame = Frame(self.root)
        self.titleFrame.config(bg="#c9bbd2")
        self.titleFrame.pack(fill=X)

        self.titleLabel = Label(self.titleFrame, text="Clientes", background="#c9bbd2", font='Kameron 50')
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
        self.tree["columns"]= ("RFC", "Nombre", "Telefono", "Correo")

        self.scrollbar = Scrollbar(self.canvas, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")


        #le damos formato a las columnas
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("RFC", anchor=W, width=200)
        self.tree.column("Nombre", anchor=W, width=200)
        self.tree.column("Correo", anchor=W, width=200)
        self.tree.column("Telefono", anchor=W, width=200)


        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("RFC", text="RFC", anchor=W)
        self.tree.heading("Nombre", text="Nombre", anchor=W)
        self.tree.heading("Correo", text="Correo", anchor=W)
        self.tree.heading("Telefono", text="Telefono", anchor=W)

        #le agregamos filas a la tabla
        data = [
            ("FIG-123", "Task 1", "Project 1", "Prueba"),
            ("FIG-122", "Task 2", "Acme GTM", "Prueba"),
            ("FIG-121", "Write blog post for demo day", "Acme GTM", "Prueba"),
            ("FIG-120", "Publish blog page", "Website launch", "Prueba"),
        ]
        for item in data:
            self.tree.insert("", "end", values=item)

        self.tree.pack(side=TOP, fill=X)

        self.btnFrame = Frame(self.root, background="white")
        self.btnFrame.pack(side=LEFT)

        self.addClientBtn = Button(self.btnFrame, text="Agregar cliente", font='Kameron 15', border=0,
                                   command=lambda: self.app.change_interface(self.app.add_clients_instance))
        self.addClientBtn.grid(row=0, column=0, padx=45)
        self.modifyClientBtn = Button(self.btnFrame, text="Modificar cliente", font='Kameron 15', border=0,
                                command=lambda: self.app.change_interface(self.app.modify_clients_instance))
        self.modifyClientBtn.grid(row=0, column=2, padx=45)
        self.deleteClientBtn = Button(self.btnFrame, text="Eliminar cliente", font='Kameron 15', border=0,
                             command=lambda: self.app.change_interface(self.app.delete_clients_instance))
        self.deleteClientBtn.grid(row=0, column=3, padx=45)

        self.exitBtn = Button(self.btnFrame, text="Salir", font='Kameron 15', border=0,
                              command=lambda: self.app.change_interface(self.app.main_instance))

        self.exitBtn.grid(row=0, column=4, padx=45)

        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Mostrar Vehiculos",
                              command=lambda: self.app.change_interface(self.app.vehicle_instance))

        # Asociar el evento de clic derecho al Treeview
        self.tree.bind('<Button-3>', self.on_right_click)

