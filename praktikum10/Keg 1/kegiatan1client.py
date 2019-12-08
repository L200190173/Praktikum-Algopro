# nama berkas : clienttcp.py
# TCP server : servertcp.py
import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 20002))
print "Mesin penjawab otomatis sudah siap"
while pesan.lower() != int:
    pesan = raw_input("Pertanyaan: ")
    s.send(pesan)
    if pesan.lower() != "keluar":
        response = s.recv(1024)
        print "Jawaban:", response
    elif pesan.lower() == "keluar":
        respone = s.recv(1024)
        print "Jawaban: OK!!!"
        break
s.close()
                  
