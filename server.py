import socket

class Sock(object):
	def __init__(self, hostname="", port=12345):
		self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._server.bind((hostname, port))
		conn, addr = self._server.listen(5)
		self._conn = conn
		self.addr = addr
	def send(self, message):
		self._conn.sendall(message)
	def receive(self):
		return str(self._conn.recv(1024), 'utf8')
	def disconnect(self):
		self._conn.close()
