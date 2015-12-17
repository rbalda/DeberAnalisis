import sys

class Campeonato:
    self.__init__(self,id_camp="",nombre=""):
        self.id_camp = id_camp
        self.nombre = nombre
        self.equipos = []
        self.encuentros = []

    self.add_equipo(self,equipo):
        self.equipos.append(equipo)

    self.add_encuentro(self,encuentro)
        self.encuentros.append(encuentro)

class Equipo:
    self.__init__(self,nombre):
        self.nombre = nombre

class Encuentro:
    self.__init__(self):
        self.equipo1 = None
        self.equipo2 = None
        self.goles1 = 0
        self.goles2 = 0
    

def leerArchivo(nombre_archivo=sys.argv[0],campeonato):
    arch = open(nombre_archivo,'r')
    index = 0
    for line in arch:
        if index==0:
            campeonato.id_camp=line.


    

    
    
    
