import tkinter as tk

class InterfazMain:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Interfaz Principal", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(self.frame, text="Ir a Interfaz Clientes", command=self.ir_a_clientes)
        self.button.pack()

    def ir_a_clientes(self):
        # Ocultar la interfaz actual
        self.frame.pack_forget()

        # Mostrar la nueva interfaz
        interfaz_clientes = InterfazClientes(self.root)


class InterfazClientes:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Interfaz de Clientes", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(self.frame, text="Volver a Interfaz Principal", command=self.volver_a_principal)
        self.button.pack()

    def volver_a_principal(self):
        # Ocultar la interfaz actual
        self.frame.pack_forget()

        # Mostrar la interfaz principal nuevamente
        interfaz_main = InterfazMain(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazMain(root)
    root.mainloop()
