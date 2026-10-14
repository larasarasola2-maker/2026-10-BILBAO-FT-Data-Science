import variables
import random
import copy

class Tablero:
    dim_x = variables.dim_x
    dim_y = variables.dim_y
    barcos = variables.dic_barcos
    #Inicializamos los tableros vacíos
    tablero1 = copy.deepcopy(variables.coord_tab) #Tablero jugador
    tablero2 = copy.deepcopy(variables.coord_tab) #Tablero máquina
    tablero_disparos = copy.deepcopy(variables.coord_tab) 

    def __init__(self, nombre1, nombre2):
        '''
        Atributos propios de cada partida los hacemos con costructor init:
        nombre1: string
        nombre2: string
        '''
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def coord_aleatorias_barcos(self):
        '''Método para inicializar el tablero asignando posiciones aleatorias a los barcos,
        devuelve una lista con tuplas formadas por las posiciones max y min de cada barco
        [(x1,x2,y1,y2),........] (cada tupla pertenece a un barco)'''
        #Colocamos el primer barco
        lista_salida = []
        for clave, valor in self.barcos.items():
            
            dim_barco = clave
            contador_barcos = 0
            while contador_barcos < valor:
                #La orientacion puede ser N/S/E/O (1,2,3,4)
                orientacion = random.randint(1,4)
                #Necesito dos puntos para hacer una recta :)
                pos_x1 = random.randint(0,9)
                pos_y1 = random.randint(0,9)

                if orientacion == 1:
                    pos_x2 = pos_x1
                    pos_y2 = pos_y1 + dim_barco - 1
                    
                elif orientacion == 2:
                    pos_x2 = pos_x1
                    pos_y2 = pos_y1 - dim_barco - 1

                elif orientacion == 3:
                    pos_x2 = pos_x1 + dim_barco - 1
                    pos_y2 = pos_y1

                elif orientacion == 2:
                    pos_x2 = pos_x1 - dim_barco - 1
                    pos_y2 = pos_y1 

                #Comprobamos si las posiciones máximas se salen del tablero
                if (0<=pos_x2<= 9) and (0<=pos_y2<=9):
                    #Guardo las posiciones en una lista de tuplas de la forma (x1,x2,y1,y2)
                    lista_salida.append((pos_x1,pos_x2,pos_y1,pos_y2))
                    contador_barcos = contador_barcos + 1
        return lista_salida

    def colocar_barcos_tablero(self,tablero):
        '''Con la función anterior ya sabemos las posiciones máximas y mínimas de los barcos
        ahora vamos a sustituir en el tablero los 0 por 1 en todos los puntos donde haya barco'''

        for elemento in self.coord_aleatorias_barcos():
            for i in range (elemento[0], elemento[1]):
                for j in range (elemento[2], elemento[3]):
                    tablero[j][i] = 1

        return tablero    

    def disparo(x,y):
        '''Le pasamos las coordenadas y si había un barco (en el tablero del oponente)
        en la posición que le hemos pasado ponemos una B en el tablero de disparos 
        y si no había barco sustituímos ponemos una A'''

     






