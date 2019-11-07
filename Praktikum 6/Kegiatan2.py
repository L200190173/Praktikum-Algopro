## Program Akun
## Dibuat oleh Ady Prasetya Nugraha L200190173
import random
angka = random.randint(0,1000)
Nama = 'Ady Prasetya Nugraha'
TanggalLahir = '23 Oktober 2001'
NamaSingkat = Nama[0] + '.' + Nama[4] + '.' + Nama[13:20]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[11:15]
Password = Nama[0:3] + str(angka)
