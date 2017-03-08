from operator import add

class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la senal
        """

        #TODO reflejar en un medio debe reflejar en todos los blancos de un medio
        #y devolver la senal reflejada
	
	senal_reflejada = [0.0]*len(una_senal)	

	for blanco in self.blancos:
		senal_ref_blanco = blanco.reflejar(una_senal,tiempo_inicial,tiempo_final)	
		senal_reflejada = map(add,senal_reflejada,senal_ref_blanco)
	
	for i in range(len(senal_reflejada)):
		if senal_reflejada[i] == 0.0:
			senal_reflejada[i] = None

	return senal_reflejada
        #pass
