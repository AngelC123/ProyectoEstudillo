#NADA QUE VALIDAR
from LogIn_Class import LogIn

#NADA QUE VALIDAR
from MainMenu import MainMenu

#NADA QUE VALIDAR
from Vehiculos_Main import Vehiculos

#NADA QUE VALIDAR
from Eliminar_Veh_Class import Eliminar_Vehiculo

#NADA QUE VALIDAR
from Servicios_Main import Servicios

#YA QUEDO VALIDADO
from Mod_Servicio_Class import Modify_Serv

#YA QUEDO VALIDADO
from Agregar_Servicio_Class import Add_Service

#NADA QUE VALIDAR
from Eliminar_Serv_Class import Eliminar_Servicio

#NADA QUE VLAIDAR
from Clientes_Main import Clientes

#NADA QUE VALIDAR
from Eliminar_Cliente_Class import Eliminar_Client

#YA QUEDO
from Agregar_Cliente_Class import Agregar_Cliente

#YA QUEDO
from Modificar_Cliente_Class import Modificar_Cliente

#YA QUEDO
from Agregar_Veh_Class import Agregar_Vehiculo

#YA QUEDO
from Mod_Veh_Class import Modificar_Veh


#NADA QUE MODIFICAR
from Hoja_Serv_Class import Hoja_Servicio

from tkinter import *

Root = Tk()

vehicle1 = Servicios(Root)
vehicle1.create_interface()

Root.mainloop()