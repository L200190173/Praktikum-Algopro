import socket
import platform
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 20001))
s.listen(2)
print "Progam server"
data = ""
kamus = {"machine":platform.machine(),
         "release":platform.release(),
         "system":platform.system(),
         "version":platform.version(),
         "node":platform.node(),
         "quit":"OK"}

while data.lower() != "quit":
    komm, addr=s.accept()
    while data.lower() != "quit":
        data = komm.recv(1024)
        if data.lower() == 'quit':
            komm.send(kamus[data])
            print "Pertanyaan:", data
            s.close()
            break
        print "Pertanyaan:", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf perintah tidak ada")
                  
s.close()                  
