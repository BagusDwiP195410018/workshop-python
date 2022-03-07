<<<<<<< HEAD
*** Pada materi ini menjelaskan tentang :
beberapa fungsi yang dapat di gunakan untuk mengolah data seperti queueu
queue dalam arti singkatnya yaitu untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, keluar pertama");
selain itu ada list comprehensions
yaitu untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat suburutan dari elemen-elemen yang memenuhi kondisi 
ada juga del 
pernyataan del. Ini berbeda dari metode pop() yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan menetapkan daftar kosong ke irisan).
Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: yaitu tuple.
=======
# 6. module
Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .py ditambahkan. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai dari variabel global
## 6.1 lebih lanjut
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul.
## kompilasi file python
Untuk mempercepat pemuatan modul, Python menyimpan versi kompilasi dari setiap modul di direktori __pycache__ di bawah nama module.version.pyc, di mana versi mengkodekan format file yang dikompilasi; biasanya berisi nomor versi Python. 
## Fungsi dir()
Fungsi bawaan dir() digunakan untuk mengetahui nama yang didefinisikan oleh modul. Ini mengembalikan daftar string yang diurutkan
## Paket
Paket adalah cara menyusun namespace modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul AB menunjuk submodule bernama B dalam paket bernama A. Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari harus khawatir tentang nama variabel global 
## Mengimpor  Dari Paket
Sekarang apa yang terjadi ketika pengguna menulis dari sound.effects import * Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke sistem file, menemukan submodul mana yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor sub-modul mungkin akan sulit
>>>>>>> 72cc5da (pertemuan)
