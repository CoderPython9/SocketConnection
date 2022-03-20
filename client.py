import socket

class Sock(object):
	def __init__(self, ip, port=12345):
		self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._client.connect((ip, port))
		
	def send(self, message):
		self._client.sendall(message)
	def recv(self):
		return str(self._client.recv(1024), 'utf-8')
	
	
