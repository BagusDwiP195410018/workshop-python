# Flask (Labu)
Dalam melakukan kegiatan ini sebelumnya yang harus diperhatikan adalah harus menggunakan python versi terbaru. 
Dalam membuat environment maka langkah yang harus di lakukan :
    - conda create -n workshopy python=3.10
    - aktifkan dengan : conda active workshopy
    - selanjutnya baru install flask dengan : conda install flask
## Hello
Buat dengan mengimport Flask from flask untuk membuat sebuah tampilan dengan memberikan ucapan hello word
## Menjalankan
flask run
Running on http://127.0.0.1:5000/ tersebut digunakan untuk menjalankan Flask_APP yang telah di buat
 ## Server Terlihat Secara Eksternal
 Akan melihat bahwa server hanya dapat diakses dari komputer sendiri, bukan dari komputer lain dalam jaringan. Ini adalah default karena dalam mode debugging, pengguna aplikasi dapat mengeksekusi kode Python sewenang-wenang di komputer
 ## Apa yang harus dilakukan jika Server tidak Mulai?
 Jika labu python -m gagal atau labu tidak ada, ada beberapa alasan yang mungkin terjadi. Pertama-tama perlu melihat pesan kesalahan.
 ## Flask Versi Lama
 Versi Flask yang lebih lama dari 0.11 perintah flask tidak ada, begitu juga dengan python -m flask. Dalam hal ini Anda memiliki dua opsi: upgrade ke versi Flask yang lebih baru atau lihat Server Pengembangan
 ## Nama Impor Tidak Valid
 Variabel lingkungan FLASK_APP adalah nama modul yang akan diimpor saat labu dijalankan. Jika modul tersebut salah diberi nama, Anda akan mendapatkan kesalahan impor saat memulai (atau jika debug diaktifkan saat menavigasi ke aplikasi).
 ## Mode Debug
 Perintah flask run dapat melakukan lebih dari sekadar memulai server pengembangan. Dengan mengaktifkan mode debug, server akan secara otomatis memuat ulang jika kode berubah, dan akan menampilkan debugger interaktif di browser jika terjadi kesalahan selama permintaan.
 ## Pelepasan HTML
 Saat mengembalikan HTML (tipe respons default di Flask), setiap nilai yang diberikan pengguna yang dirender dalam output harus diloloskan untuk melindungi dari serangan injeksi. 
 HTML Template yang di gunakan 
 from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
## Routing (Rute)
Aplikasi web modern menggunakan URL yang bermakna untuk membantu pengguna.
code yang digunakan
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
## Aturan Variabel
Dapat menambahkan bagian variabel ke URL dengan menandai bagian dengan <nama_variabel>. Fungsi kemudian menerima <variable_name> sebagai argumen kata kunci.