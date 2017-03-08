class Detector(object):

    def __init__(self):
	pass

    def detectar(self,senal, senal_ref):
	if max(senal_ref)>max(senal):
		print "Se detecto un objeto"
        else:
		print "No se detecto nada en este intervalo de tiempo"
	
	return 1
