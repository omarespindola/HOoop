from radar import Radar
from medio import Medio
from blanco import Blanco
from generador import Generador
import datetime
from detector import Detector
import matplotlib.pyplot as plt


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)
    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    #Construir un nuevo genrador de senales
	
    Gen = Generador(amplitud,fase,frecuencia)

    #Construir un detector

    detector = Detector()
	
    #construir un nuevo radar

    radar = Radar(Gen,detector)

    # parametros para un blanco

    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_b = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_b = datetime.datetime(2016, 3, 5, 6)
    
    # Construir un nuevo blanco

    blanco = Blanco(amplitud_de_frecuencia_del_blanco,tiempo_inicial_b,tiempo_final_b)

    lista_blancos = [blanco]

    #Construir un medio

    medio = Medio(lista_blancos)

    #Hago funcionar el radar

    radar.detectar(medio,tiempo_inicial,tiempo_final)
    radar.graficar(medio,tiempo_inicial,tiempo_final)

if __name__ == "__main__":
    main()
