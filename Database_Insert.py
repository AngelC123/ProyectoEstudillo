import Database_Schettino
from sqlalchemy import Column, BigInteger, DATE, ForeignKey, Float, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from datetime import datetime


Session = sessionmaker(bind=Database_Schettino.engine)
session = Session()


i1 = Database_Schettino.Servicios(
    Numero_Orden = 10,
    Fecha = datetime.strptime("2024-02-19", "%Y-%m-%d").date(),
    Reporte_Cliente = "Codigos activos de nivel de refrigerante",
    ID_Falla = 3,
    Inspeccion_Tecnico = "Nivel de anticongelante bajo",
    Job = "Se relleno el anticongelante, escaneo de la unidad",
    Refacciones = "7 LT de anticongelante",
    Obs = "Cambiar sensor de nivel",
    Placa_Veh = "LMA012",
    Mano_obra = 120,
    Costo_piezas = 1000,
    ID_Empleado = "IWIM2342",
    RFC_Cliente = "OJMK23423KII"
)


"""
i1 = Database_Schettino.Fallas(
    ID_Falla = 12,
    Tipo_Falla = "Hidraulico"
)
"""


session.add(i1)
session.commit()