from sqlalchemy import Column, BigInteger, DATE, ForeignKey, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Clientes(Base):
    __tablename__ = "Cliente"
    RFC = Column(String, primary_key=True)
    Nombre = Column(String)
    Telefono = Column(BigInteger)
    Correo = Column(String)

    vehicles_rel_clients = relationship("Vehiculos", back_populates="clientes_rel_vehicles")
    servs_rel_clients = relationship("Servicios", back_populates="cliente_rel_servs")

class Vehiculos(Base):
    __tablename__ = "Vehiculo"
    Placa = Column(String, primary_key=True)
    RFC_Cliente = Column(String, ForeignKey('Cliente.RFC', ondelete="CASCADE", onupdate="CASCADE"))
    Modelo = Column(String)
    Year = Column(Integer)
    Vin = Column(String)
    Kilometraje = Column(Integer)
    Motor = Column(String)

    clientes_rel_vehicles = relationship("Clientes", back_populates="vehicles_rel_clients")
    servs_rel_vehicles = relationship("Servicios", back_populates="vehiculo_rel_servs")

class Fallas(Base):
    __tablename__ = "Fallas"
    ID_Falla = Column(Integer, primary_key=True)
    Tipo_Falla = Column(String)

    servs_rel_fallas = relationship("Servicios", back_populates="falla_rel_servs")

class Empleado(Base):
    __tablename__ = "Empleados"
    ID_Empleado = Column(String, primary_key=True)
    Nombre = Column(String)
    Apellidos = Column(String)
    Email = Column(String)
    Numero_Tel = Column(BigInteger)
    Edad = Column(Integer)
    Puesto = Column(String)
    Contraseña = Column(String)
    Imagen = Column(String)

    servs_rel_empleado = relationship("Servicios", back_populates="empleado_rel_servs")

class Servicios(Base):
    __tablename__ = "Servicios"
    Numero_Orden = Column(Integer, primary_key=True)
    Fecha = Column(DATE)
    Reporte_Cliente = Column(String)
    ID_Falla = Column(Integer, ForeignKey('Fallas.ID_Falla'))
    Inspeccion_Tecnico = Column(String)
    Job = Column(String)
    Refacciones = Column(String)
    Obs = Column(String)
    Placa_Veh = Column(String, ForeignKey('Vehiculo.Placa'))
    Mano_obra = Column(Float)
    Costo_piezas = Column(Float)
    ID_Empleado = Column(String, ForeignKey('Empleados.ID_Empleado'))
    RFC_Cliente = Column(String, ForeignKey('Cliente.RFC', ondelete="CASCADE", onupdate="CASCADE"))

    vehiculo_rel_servs = relationship("Vehiculos", back_populates="servs_rel_vehicles")
    falla_rel_servs = relationship("Fallas", back_populates="servs_rel_fallas")
    empleado_rel_servs = relationship("Empleado", back_populates="servs_rel_empleado")
    cliente_rel_servs = relationship("Clientes", back_populates="servs_rel_clients")

engine = create_engine("sqlite:///Database_Proyecto.db", echo=True, future=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
