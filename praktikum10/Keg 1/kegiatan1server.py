# nama berkas : servertcp.py
# TCP client : clienttcp.py
import socket
import platform
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 20002))
s.listen(2)
print "Server penjawab otomatis siap"
data = ""
kamus = {"nama":"Ady Prasetya Nugraha",
         "NIM":"L200190173",
         "angkatan":"2019",
         "motto":"LIfe to ride, Ride to jannah",
         "kuliah":"Universitas Muhammadiyah Surakarta"}

while data.lower() != "keluar":
    komm, addr=s.accept()
    while data.lower() !=" keluar":
        data = komm.recv(1024)
        if data.lower() == "keluar":
            komm.send("OK!!")
            s.close()
            print "Pertanyaan:", data
            break
        print "Pertanyaan:", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf perintah tidak ada")
s.close()                  
