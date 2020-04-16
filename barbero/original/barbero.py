import time
#__CLOUDBOOK:GLOBAL__
client_appears = False

#__CLOUDBOOK:NONSHARED__
clientes = 8

#__CLOUDBOOK:PARALLEL__
def barbero():
	global client_appears
	todos_cortados = 0
	while todos_cortados<clientes:
	#for i in range(20):
		#print("El barbero esta durmiendo",__CLOUDBOOK__["agent"]["id"])
		updated_client = refresh_client()
		#print("Barbero",__CLOUDBOOK__["agent"]["id"],": Ha llegado alguien?",updated_client)
		if updated_client:
			#__CLOUDBOOK:LOCK__	
			#print("Barbero",__CLOUDBOOK__["agent"]["id"],": Barbero se despierta")
			client_appears = False
			print("Barbero",__CLOUDBOOK__["agent"]["id"],": Barbero ha cortado el pelo al cliente, lleva", todos_cortados+1)
			todos_cortados +=1
			#__CLOUDBOOK:UNLOCK__

#__CLOUDBOOK:NONBLOCKING__
def cliente():
	global client_appears
	cortado = False
	while not cortado:
		updated_client = refresh_client()
		#print("Cliente",__CLOUDBOOK__["agent"]["id"],": Hay clientes ya?",updated_client)
		if updated_client:
			#print("Cliente",__CLOUDBOOK__["agent"]["id"],": cliente esperando")
			continue
		else:
			#__CLOUDBOOK:LOCK__
			updated_client = refresh_client()
			if not updated_client:
				client_appears = True
				print("Cliente",__CLOUDBOOK__["agent"]["id"],": cliente se va a cortar el pelo, esta libre el barbero")
				cortado = True
			#__CLOUDBOOK:UNLOCK__

#__CLOUDBOOK:LOCAL__
def refresh_client():
	global client_appears
	x = client_appears
	return x

#__CLOUDBOOK:MAIN__
def main():
	print("Empieza el dia en la barberia")
	print("llamo al barbero")
	barbero()
	for i in range(clientes):
		#time.sleep(1)
		print("Llega el cliente",i)
		cliente()
	print('Ya no llegan mas clientes')
	#__CLOUDBOOK:SYNC__
	print("Cerramos la barberia, hasta mañana")

main()