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

    self.__unicode__(self):
        return self.nombre

class Equipo:
    self.__init__(self,nombre):
        self.nombre = nombre
        self.puntos = 0
        self.golesDiferencia = 0
        self.partidosGanados = 0
        self.golesFavor = 0
        self.partidosJugados = 0

    @property
    def valor_lexi(self):
        letras = list(self.nombre)
        valor = 0
        for l in letras:
            valor += ord(l)
        return valor

    self.__unicode__(self):
        return self.nombre


class Encuentro:
    self.__init__(self):
        self.equipo1 = None
        self.equipo2 = None
        self.goles1 = 0
        self.goles2 = 0

    self.__unicode__(self):
        self.


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


def merge_sort(lista):
    if len(lista)>1:
        mitad = len(lista)/2
        mitad_izquierda = lista[:mitad]
        mitad_derecha = lista[mitad:]

        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        i=0
        j=0
        k=0
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                lista[k]=mitad_izquierda[i]
                i=i+1
            else:
                lista[k]=mitad_derecha[j]
                j=j+1
            k=k+1

        while i < len(mitad_izquierda):
            lista[k]=mitad_izquierda[i]
            i=i+1
            k=k+1

        while j < len(mitad_derecha):
            lista[k]=mitad_derecha[j]
            j=j+1
            k=k+1


def quicksort(self,lista_input, primer, ultimo):
        i = primer
        j = ultimo
        pivote = lista_input[int((primer+ultimo)/2)]

        while i < j:
            while lista_input[i].Ganados < pivote.Ganados:
                i+=1
            while lista_input[j].Ganados > pivote.Ganados:
                j-=1
            if (i <= j):
                x = lista_input[j]
                lista_input[j] = lista_input[i]
                lista_input[i] = x
                i+=1
                j-=1

        if first < j:
            lista_input = self.quicksort(lista_input, primer, j)
        if last > i:
            lista_input = self.quicksort(lista_input, i, ultimo)

        return lista_input


def radix_sort(self, lista ):
          RADIX = 10
          max_length = False
          tmp , lugar = -1, 1

          while not max_length:
            max_length = True
            # declare and initialize buckets
            buckets = [list() for _ in range( RADIX )]

            # split aList between lists
            for  i in lista:
              tmp = i.GolesDiferencia / lugar
              buckets[int(tmp % RADIX)].append( i )
              if max_length and tmp > 0:
                max_length = False

            # empty lists into aList array
            a = 0
            for b in range( RADIX ):
              buck = buckets[b]
              for i in buck:
                lista[a] = i
                a += 1

            # move to next digit
            lugar *= RADIX
            return lista


def burbuja(lista):
    cantidad = len(lista)
    i= 0
    while (i < cantidad):
        j = i
        while (j < cantidad):
            if(lista[i] > lista[j]):
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
            j= j+1
        i=i+1


def selection_sort(lista,tamanio):
    for i in range(0,tamanio-1):
        minimo=i
        for j in range(i+1,tamanio):
            if lista[minimo] > lista[j]:
                minimo=j
        tmp=lista[minimo]
        lista[minimo]=lista[i]
        lista[i]=tmp


def insertion_sort(lista):
   for indice in range(1,len(lista)):

     actual = lista[indice]
     posicion = indice

     while posicion>0 and lista[posicion-1]>actual:
         lista[posicion]=lista[posicion-1]
         posicion = posicion-1

     lista[posicion]=actual
