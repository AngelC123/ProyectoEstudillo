import tkinter as tk
from tkinter import ttk

def on_right_click(event):
    # Obtener el elemento bajo el clic derecho
    item = tree.identify_row(event.y)
    if item:
        # Seleccionar el ítem en el que se ha hecho clic derecho
        tree.selection_set(item)
        # Mostrar el menú contextual
        menu.post(event.x_root, event.y_root)

def on_option_select():
    # Obtener el elemento seleccionado
    selected_item = tree.selection()[0]
    print(f"Opción seleccionada para el ítem: {tree.item(selected_item, 'text')}")

def insertar_items_en_treeview():
    global tree, menu

    # Crear ventana principal
    root = tk.Tk()
    root.title("Treeview con Menú Contextual")

    # Crear un Treeview
    tree = ttk.Treeview(root, columns=('Columna1', 'Columna2'))
    tree.heading('#0', text='Item')
    tree.heading('Columna1', text='Columna 1')
    tree.heading('Columna2', text='Columna 2')
    tree.grid(row=0, column=0, sticky='nsew')

    # Ajustar las columnas del Treeview
    tree.column('#0', width=200)
    tree.column('Columna1', width=100)
    tree.column('Columna2', width=100)

    # Agregar algunos elementos al Treeview
    tree.insert('', 'end', text='Item 1', values=('Valor 1', ''))
    tree.insert('', 'end', text='Item 2', values=('Valor 2', ''))
    tree.insert('', 'end', text='Item 3', values=('Valor 3', ''))

    # Crear un menú contextual
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Seleccionar Opción", command=on_option_select)

    # Asociar el evento de clic derecho al Treeview
    tree.bind('<Button-3>', on_right_click)

    root.mainloop()

insertar_items_en_treeview()
