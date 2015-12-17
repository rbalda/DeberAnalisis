import sys
import os

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


def leerArchivo(nombre_archivo,campeonato):
    arch = open(nombre_archivo,'r')
    index = 0
    total_list=0

    for line in arch:
        if index==0:
            campeonato.id_camp=int(line.strip())
        elif index==1:
            campeonato.nombre=line.strip()
        elif index==2:
            total_list = int(line.strip())
        elif index>2 and <total_list+3:
            equipo = Equipo(line.strip())
            campeonato.add_equipo(equipo)
        elif index==total_list+3:
            total_list = int(line.strip())
        else:
            encuentro = Encuentro()
            enc = line.split('@')
            encuentro.equipo1 = enc[0].split('#')[0]
            encuentro.goles1 = enc[0][1]
            encuentro.equipo2 = enc[1].split('#')[0]
            encuentro.goles2 = enc[1][1]
            campeonato.add_encuentro(encuentro)
        index += 1

def loop_archivos(dir_name=sys.argv[0]):
    for fn in os.listdir(dir_name):
        if os.path.isfile(fn):
            campeonato = Campeonato()
            leerArchivo(fn,campeonato)
