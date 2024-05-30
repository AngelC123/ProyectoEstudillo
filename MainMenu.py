from tkinter import *
from PIL import ImageTk, Image

class MainMenu:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def create_interface(self):
        self.root = Toplevel(self.master)
        self.root.attributes("-fullscreen", True)
        self.root.resizable(False, False)
        self.root.configure(bg="#FFFFFF")
        # Here we can find three frames to build the main window of the application
        self.mainMenuTitleFrame = Frame(self.root, bg="#C9BBD2")
        self.employeeInfoFrame = Frame(self.root, bg="#BABFEC")
        self.menuFrame = Frame(self.root, bg="#FFFFFF")
        # These are the components of the window, we can show the data of the employees and some options
        self.employeeRFCLabel = Label(self.employeeInfoFrame, text="RFC", bg="#BABFEC", font=("Kadwa", 15))
        self.employeeNameLabel = Label(self.employeeInfoFrame, text="Nombre", bg="#BABFEC", font=("Kadwa", 15))
        self.employeeLastNamesLabel = Label(self.employeeInfoFrame, text="Apellidos", bg="#BABFEC", font=("Kadwa", 15))
        self.employeeTelephoneLabel = Label(self.employeeInfoFrame, text="Teléfono", bg="#BABFEC", font=("Kadwa", 15))
        self.employeeEmailLabel = Label(self.employeeInfoFrame, text="Email", bg="#BABFEC", font=("Kadwa", 15))
        self.logOutLabel = Label(self.employeeInfoFrame, text="Cerrar Sesión", bg="#BABFEC", font=("Kadwa", 15))
        self.windowNameLabel = Label(self.mainMenuTitleFrame, text="Nombre de la Empresa",
                                     font=("Julius Sans One", 60), bg="#C9BBD2")
        self.questionLabel = Label(self.menuFrame, text="¿Qué desea hacer hoy?",
                                   font=("Kadwa", 50), bg="#FFFFFF")
        self.clientButton = Button(self.menuFrame, text="Cliente", fg="black", bg="#BABFEC", bd=0, font=("Inter", 25),
                                   command=lambda: self.app.change_interface(self.app.clients_instance))


        self.serviceButton = Button(self.menuFrame, text="Servicio", fg="black", bg="#BABFEC", bd=0, font=("Inter", 25),
                                    command=lambda: self.app.change_interface(self.app.servicios_instance))


        self.roundImage = Image.open(fp="C:/Users/migue/PycharmProjects/Topicos_Avanzados_Enero_Junio/empresaaa.jpg").resize((96, 96), Image.ADAPTIVE)
        self.icon = ImageTk.PhotoImage(self.roundImage)
        self.employeeImage = Label(self.employeeInfoFrame, image=self.icon, bg="#BABFEC")
        self.squareImage = Image.open(fp="C:/Users/migue/PycharmProjects/Topicos_Avanzados_Enero_Junio/empresaaa.jpg").resize((96, 96), Image.ADAPTIVE)
        self.squareIcon = ImageTk.PhotoImage(self.squareImage)
        self.clientIcon = Label(self.menuFrame, image=self.squareIcon, bg="white")
        self.service = Image.open(fp="C:/Users/migue/PycharmProjects/Topicos_Avanzados_Enero_Junio/empresaaa.jpg").resize((100, 100), Image.ADAPTIVE)
        self.serviceIcon = ImageTk.PhotoImage(self.service)
        self.serviceImage = Label(self.menuFrame, image=self.serviceIcon, bg="white")
        self.employeeInfoFrame.pack(side=LEFT, fill=Y)
        self.mainMenuTitleFrame.pack(side=TOP, fill=X)
        self.menuFrame.pack(padx=60, pady=100)
        self.employeeImage.pack(padx=10, pady=20)
        self.employeeRFCLabel.pack(padx=10, pady=20)
        self.employeeNameLabel.pack(padx=10, pady=20)
        self.employeeLastNamesLabel.pack(padx=10, pady=20)
        self.employeeTelephoneLabel.pack(padx=10, pady=20)
        self.employeeEmailLabel.pack(padx=10, pady=20)
        self.windowNameLabel.pack(pady=10)
        self.logOutLabel.pack(padx=10, pady=20)
        self.menuFrame.rowconfigure(index=0, weight=1)
        self.menuFrame.rowconfigure(index=1, weight=1)
        self.menuFrame.rowconfigure(index=2, weight=1)
        self.menuFrame.columnconfigure(index=0, weight=1)
        self.menuFrame.columnconfigure(index=1, weight=1)
        self.questionLabel.grid(row=0, column=0, columnspan=2, sticky=EW)
        self.clientIcon.grid(row=1, column=0, sticky=NSEW)
        self.serviceImage.grid(row=1, column=1, sticky=NSEW)
        self.clientButton.grid(row=2, column=0, sticky=NSEW, padx=20, pady=20)
        self.serviceButton.grid(row=2, column=1, sticky=NSEW, padx=20, pady=20)

    # These are the methods to navigate from the main window to the clients and the services windows.
    def logOut(self):
        return

    def toClientsWindow(self):
        return

    def toServicesWindow(self):

        return