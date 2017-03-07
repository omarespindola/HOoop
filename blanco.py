class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial_b, tiempo_final_b):
        #TODO: completar con la inicializacion de los parametros del objeto
	self.amplitud = amplitud
	self.tiempo_inicial_b = tiempo_inicial_b
	self.tiempo_final_b = tiempo_final_b
        pass

    def reflejar(self, senal, tiempo_inicial, tiempo_final):

        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
	
        if tiempo_inicial<tiempo_inicial_b and tiempo_final>tiempo_final_b:
		return 1
	elseif tiempo_inicial>tiempo_inicial_b and tiempo_inicial>tiempo_final_b:
		return 2
	elseif tiempo_inicial<tiempo_inicial_b and tiempo_final>tiempo_final_b:
		return 3
	else: 
		return 4
        
        
