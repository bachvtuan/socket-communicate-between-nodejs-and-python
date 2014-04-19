import socket

if __name__ == "__main__":
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(('127.0.0.1', 7000))

  client.sendall("Hello")
  data = client.recv(1024)
  client.close()

  print 'Received', repr(data)