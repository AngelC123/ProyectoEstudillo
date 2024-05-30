from tkinter import *
from PIL import ImageTk, Image


class LogIn:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def create_interface(self):
        self.root = Toplevel(self.master, background="white")
        self.root.geometry("600x500")

        # Frame donde se almacena el nombre de la emplesa
        self.con1 = Frame(self.root, bg="#D2BBD2", width=100, height=80)  # Define el tamaño y el color del frame
        self.con1.pack_propagate(False)  # Hace que el tamaño del frame no dependa de su contenido
        self.con1.pack(expand=0, fill=BOTH, side=TOP)  # Colocamos el frame
        self.lbl1 = Label(self.con1, text="Nombre de la empresa", font=("Julius Sans One", 20), bg="#D2BBD2")  # Define el tipo de ortografia de nuestro Label
        self.lbl1.pack(pady=15)  # Colocamos label

        # Abrir la imagen de la empresa  y redimensionarla
        self.image = Image.open("C:/Users/migue/PycharmProjects/Topicos_Avanzados_Enero_Junio/empresaaa.jpg")  # Se coloca el nombre del la imagen
        self.new_size = (250, 250)  # Nuevo tamaño opara la imagen
        self.resized_image = self.image.resize(self.new_size)
        self.tkinter_image = ImageTk.PhotoImage(self.resized_image)
        self.con2 = Frame(self.root, background="white")  # Coloco la imagen en un nuevo frame
        self.con2.pack(fill=BOTH, side=LEFT, )
        label = Label(self.con2, image=self.tkinter_image)  # Coloco la imagen redimensionada en un label
        label.pack(padx=10, pady=0, side=LEFT)

        # Frama para el bienvenidos
        self.con3 = Frame(self.root, background="white")
        self.con3.pack(fill=BOTH)
        self.lbl2 = Label(self.con3, text="BIENVENIDO", font=("Julius Sans One", 18), background="white")
        self.lbl2.pack(pady=20)
        self.lbl3 = Label(self.con3, text="Inserte su codigo y", font=("Khula", 14), background="white")
        self.lbl3.pack()
        self.lbl4 = Label(self.con3, text="contraseña de empleado", font=("Khula", 14), background="white")
        self.lbl4.pack()

        # Frame para ingresar el codigo y contraseña


        def click_codigo(event):
            if self.ent1.get() == "Codigo de empleado":
               self.ent1.delete(0, "end")  # Borra el texto de ejemplo al hacer click
               self.ent1.config(fg="Black")  # Cambia el color del texto a negro


        def on_focusout_codigo(event):
            if self.ent1.get() == '':
                self.ent1.insert(0, "Codigo de empleado")  # Restaura el texto de ejemplo si no se ingresa nada
                self.ent1.config(fg='grey')  # Cambia el color del texto a gris


        def click_password(event):
            if self.ent2.get() == "Contraseña":
               self.ent2.delete(0, "end")  # Borra el texto de ejemplo al hacer clic
               self.ent2.config(fg="Black")  # Cambia el color del texto a negro


        def on_focusout_password(event):
            if self.ent2.get() == '':
                self.ent2.insert(0, "Contraseña")  # Restaura el texto de ejemplo si no se ingresa nada
                self.ent2.config(fg='grey')  # Cambia el color del texto a gris


        self.con4 = Frame(self.root, background="white")
        self.con4.pack(fill=BOTH, pady=50)
        self.ent1 = Entry(self.con4, fg='grey', borderwidth=1, relief="solid", width=30)  # Establece el color del texto a gris
        self.ent1.insert(0, "Codigo de empleado")  # Inserta el texto de ejemplo
        self.ent1.bind('<FocusIn>', click_codigo)  # Evento de click en el Entry
        self.ent1.bind('<FocusOut>', on_focusout_codigo)  # Evento de pérdida de enfoque del Entry
        self.ent1.pack(pady=10)

        self.ent2 = Entry(self.con4, fg='grey', borderwidth=1, relief="solid", width=30)  # Establece el color del texto a gris
        self.ent2.insert(0, "Contraseña")  # Inserta el texto de ejemplo
        self.ent2.bind('<FocusIn>', click_password)  # Evento de clic en el Entry
        self.ent2.bind('<FocusOut>', on_focusout_password)  # Evento de pérdida de enfoque del Entry
        self.ent2.pack(pady=10)

        btn = Button(self.con4, text="Ingresar", fg="white", bg="Black", width=25, font='Inter 10',
                     command=lambda: self.app.change_interface(self.app.main_instance))
        btn.pack(pady=5)


