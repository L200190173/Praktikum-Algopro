Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Ady Prasetya Nugraha'
>>> NIM = 173
>>> Tinggi = 1.79
>>> Berat = 55
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # merupakan tipe tuple yang berisi sekumpulan data yang memuat TahunLahir, Berat, Tinggi, NIM, dan Nama dan tipe data tuple tidak dapat diubah
>>> Aku[0]
2001
>>> # menampilkan elemen tuple indeks ke-0 yaitu TahunLahir atau data 2001
>>> a = NIM % 4; Aku[a]
2001
>>> # hasil sisa bagi dari variabel NIM dengan 4 adalah 0 dan disimpan dalam variabel a kemudian Aku[a] akan menjadi Aku[0] dimana akan menampilkan elemen tuple Aku indeks ke-0 atau TahunLahir
>>> type(Aku[a])
<class 'int'>
>>> # elemen tuple Aku indeks ke 0(0 merupakan data dari variabel a) atau TahunLahir adalah 2001 dan merupakan data bertipe integer atau bilangan bulat
>>> Aku[a:4]
(2001, 55, 1.79, 173)
>>> # menampilkan elemen dari tuple Aku mulai dari indeks ke-0 hingga sebelum indeks ke-4 yang berisi TahunLahir, Berat, Tinggi dan NIM
>>> type(Aku[4])
<class 'str'>
>>> # elemen tuple Aku indeks ke-4 merupakan data tipe string karena berisi Nama
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # terjadi tipe eror karena data tipe tuple tidak dapat diubah sedangkan program ingin mengubah elemen tuple indeks ke-0 dari TanggalLahir menjadi 'ok' maka terjadi tipe error
>>> type(Data)
<class 'list'>
>>> # variabel Data merupakan tipe list karena berisi sekumpulan data atau karakter dan data dalam list dapat diubah
>>> type(Data[4])
<class 'str'>
>>> # elemen list indeks ke-4 atau yang berisi Nama merupakan data yang bertipe string karena mengandung karakter
>>> Data[4][5]
'i'
>>> # elemen list indeks ke-4 atau yang berisi Nama kemudian program akan menjadi Nama[5] atau indeks ke-5 dari data yang telah disimpan dalam variabel Nama yaitu huruf n
>>> Data[4][a:6]
'Ady'
>>> # elemen list Data indeks ke-4 yang berisi Nama kemudian program akan menjadi Nama[a:6] dimana a berisi data 0 maka akan menjadi Nama[0:6] yang akan meampilkan elemen list indeks ke-0 hingga sebelum indeks ke-6 yaitu Fakhri
>>> Data[0] = 'ok'; Data
['ok', 55, 1.79, 173, 'Ady Prasetya Nugraha']
>>> # elemen list Data indeks ke-0 diubah dari TanggalLahir menjadi 'ok' dan kemudian program menampilkan data dari list Data
>>> Data[-a]
'ok'
>>> # variabel a berisi data 0 maka program menjadi Data[-0] yang akan menampilkan elemen list Data indeks ke-0
>>> range(a)
range(0, 0)
>>> # varibel a berisi data 0 maka program akan menjadi range(0) dan program akan menampilkan range dari 0 hingga 0 atau jika ditulis dalam program range(0, 0)
>>> 
