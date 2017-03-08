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
	
	segSen = len(senal)
	f_muestreo = (tiempo_final - tiempo_inicial).seconds / segSen
	senal_ref = [0.0]*segSen

        if self.tiempo_inicial_b>=tiempo_inicial and self.tiempo_final_b<=tiempo_final:
		t0= (self.tiempo_inicial_b - tiempo_inicial).seconds / f_muestreo	
		t1= (self.tiempo_final_b - self.tiempo_inicial_b).seconds / f_muestreo
		
		for i in range(t0,t1):
			senal_ref[i] = self.amplitud*senal[i]

		return senal_ref

 	elif self.tiempo_inicial_b < tiempo_inicial and self.tiempo_final_b>tiempo_final:
		for i in range(segSen):
			senal_ref[i] = self.amplitud*senal[i]
		return senal_ref

	elif self.tiempo_inicial_b<tiempo_inicial and self.tiempo_final_b<tiempo_final and self.tiempo_final_b>tiempo_inicial:
		t0= 0
		t1= (self.tiempo_final_b - tiempo_inicial).seconds / f_muestreo
		
		for i in range(t0,t1):
			senal_ref[i] = self.amplitud*senal[i]

		return senal_ref

	elif self.tiempo_inicial_b>tiempo_inicial and self.tiempo_inicial_b<tiempo_final and self.tiempo_final_b>tiempo_final:
		t0= (self.tiempo_inicial_b - tiempo_inicial).seconds / f_muestreo	
		t1= segSen
		
		for i in range(t0,t1):
			senal_ref[i] = self.amplitud*senal[i]

		return senal_ref

	else: 
		return senal_ref
        
        
