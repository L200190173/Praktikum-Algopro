import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 20001))
print "Progam komunikasi tentang server"
while pesan.lower() != "quit":
    pesan = raw_input("Pertanyaan: ")
    s.send(pesan)
    if pesan.lower() != int:
        response = s.recv(1024)
        print "Jawaban:", response
    elif pesan.lower() != "quit":
        respone = s.recv(1024)
        print "Jawaban:", response
        break
s.close()
                  
