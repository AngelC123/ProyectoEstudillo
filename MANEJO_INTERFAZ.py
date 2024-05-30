from tkinter import *
import tkinter as tk
#IMPORTAMOS EN ORDEN
from LogIn_Class import *
from MainMenu import *
#CLIENTES
from Clientes_Main import *
from Agregar_Cliente_Class import *
from Eliminar_Cliente_Class import *
from Modificar_Cliente_Class import *
from Vehiculos_Main import *

#Vehiculos
from Mod_Veh_Class import *
from Eliminar_Veh_Class import *
from Agregar_Veh_Class import *

#SERVICIOS
from Servicios_Main import *
from Hoja_Serv_Class import *
from Eliminar_Serv_Class import *
from Agregar_Servicio_Class import *
from Mod_Servicio_Class import *



class App:
    def __init__(self, master):
        self.master = master
        self.current_interface = None

    def change_interface(self, new_interface):
        if self.current_interface:
            self.current_interface.root.withdraw()  # Oculta la ventana actual
        new_interface.create_interface()
        new_interface.root.deiconify()  # Muestra la nueva ventana
        self.current_interface = new_interface

def main():
    root = Tk()
    app = App(root)

    # Crear todas las instancias de las interfaces
    login_instance = LogIn(root, app)
    main_instance = MainMenu(root, app)
    servicios_instance = Servicios(root, app)
    add_service_instance = Add_Service(root, app)
    see_service_instance = Hoja_Servicio(root, app)
    delete_service_instance = Eliminar_Servicio(root, app)
    modify_service_instance = Modify_Serv(root, app)

    clients_instance = Clientes(root, app)
    add_clients_instance = Agregar_Cliente(root, app)
    delete_clients_instance = Eliminar_Client(root, app)
    modify_clients_instance = Modificar_Cliente(root, app)

    vehicle_instance = Vehiculos(root, app)
    add_vehicle_instance = Agregar_Vehiculo(root, app)
    delete_vehicle_instance = Eliminar_Vehiculo(root, app)
    modify_vehicle_instance = Modificar_Veh(root, app)


    # Agregar las instancias de las interfaces a la aplicación
    app.login_instance = login_instance
    app.main_instance = main_instance


    #PUEDE SER CLIENTES Y VEHICULOS....
    app.clients_instance = clients_instance
    app.add_clients_instance = add_clients_instance
    app.delete_clients_instance = delete_clients_instance
    app.modify_clients_instance = modify_clients_instance

    app.vehicle_instance = vehicle_instance
    app.add_vehicle_instance = add_vehicle_instance
    app.delete_vehicle_instance = delete_vehicle_instance
    app.modify_vehicle_instance = modify_vehicle_instance

    #PUEDE SER SERVICIOS
    app.servicios_instance = servicios_instance
    app.add_service_instance = add_service_instance
    app.see_service_instance = see_service_instance
    app.delete_service_instance = delete_service_instance
    app.modify_service_instance = modify_service_instance



    # Mostrar la primera interfaz al inicio
    app.change_interface(login_instance)

    root.mainloop()

if __name__ == "__main__":
    main()
