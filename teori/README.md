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
