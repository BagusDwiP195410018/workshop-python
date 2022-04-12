# BAB 10 (Standard Library) 
## Operasi sistem
pada bagian ini menyediakan fungsi yang digunakan untuk ber interaksi ke sistem operaso
## File wildcard
untuk bagian file wildcard ini  menyediakan fungsi untuk membuat daftar file dari pencarian wildcard pada direktori
## Argumen baris
Argumen ini disimpan dalam atribut argv modul sys. Hasil keluaran biasanya dari menjalankan python demo.py satu dua tiga di baris perintah
## Pengalihan Output dan Pemberhentian Program
sys juga memiliki atribut untuk stdin, stdout, dan stderr. Berguna untuk memancarkan peringatan dan pesan kesalahan agar terlihat bahkan ketika stdout 
## Pencocokan pola String
Menyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut. Pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan optimal
## Matematika
Modul matematika memberikan akses untuk melakukan perhitungan menggunakan metode - metode dari matematik
## Akses Internet
Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua di antaranya _urllib.request_ guna untuk mengambil data dari URL dan smtplib untuk mengirim email
## Tanggal dan Waktu
Pada modul ini kita bisa menggunakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Modul ini juga mendukung pembagian zonasi waktu
## Data Kompresi
Pengarsipan data umum dan format kompresi secara langsung didukung oleh modul termasuk menggunakan _zlib, gzip, bz2, lzma, zipfile dan tarfile_
## Pengukuran kinerja
Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. Dalam python juga menyediakan alat ukur untuk pengukuran kinerja yang menjawab pertanyaan - pertanyaan sesegera
## Kontrol Kualitas
Pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah dengan menulis tes untuk setiap fungsi saat dikembangkan dan menjalankan tes tersebut sesering mungkin selama proses pengembangan.
## Baterai termasuk
Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kemampuan canggih dan kuat dari paket-paketnya yang lebih besar.
    1. _xmlrpc.client_ dan _xmlrpc.server_ membuat penerapan panggilan prosedur jarak jauh menjadi tugas
    2. Paket email adalah perpustakaan untuk mengelola pesan email
    3. Paket json menyediakan dukungan kuat untuk menguraikan format pertukaran data 
    4. Modul sqlite3 adalah pembungkus untuk perpustakaan database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.
    5. Internasionalisasi didukung oleh sejumlah modul termasuk _gettext, locale, dan paket codec._
# (Bab 11) Standard Library part 2 
Modul ini mencakup yang lebih canggih yang mendukung kebutuhan pemrograman profesional yang jarang ada pada script kecil
## Pemformatan keluar
Modul reprlib menyediakan versi _repr()_ yang disesuaikan untuk tampilan singkat container besar atau bersarang.
## Pembuatan Template
Modul ini terdapat string yang menyertakan kelas Template serbaguna dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna akhir. Sehingga penguna dapat mengeditnya tanpa harus mengubah aplikasi. Formatnya menggunakan nama placeholder namun di tulisan dengan _$_
## Bekerja dengan Tata Letak Rekaman Data Biner
_Struct_ menyediakan fungsi pack() dan unpack() untuk bekerja dengan format record biner dengan panjang variabel.
## Multi - utas
Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima masukan pengguna saat tugas lain berjalan di latar belakang.
## Pencatatan
_Logging_ menawarkan sistem logging berfitur lengkap dan fleksibel. Paling sederhana, pesan log dikirim ke file atau ke _sys.stderr_
## Referensi lemah
Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus) dengan cara menghilangkan referensi terskhir.
## Alat untuk Bekerja dengan Daftar
Struktur data dapat dipenuhi dengan tipe daftar bawaan. Namun, terkadang ada kebutuhan untuk implementasi alternatif dengan pertukaran kinerja yang berbeda.
## Aritmatika Titik Mengambang Desimal
Desimal menawarkan tipe data Desimal untuk aritmatika titik mengambang desimal. Implementasi _float built-in_ dari _floating point biner_ kelas ini sangat membantu untuk :
    1. aplikasi keuangan dan penggunaan lain yang memerlukan representasi desimal 
    2. kontrol atas presisi
    3. kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan
    4. pelacakan tempat desimal yang signifikan
    5. aplikasi di mana pengguna mengharapkan hasil yang sesuai dengan perhitungan yang dilakukan dengan tangan.