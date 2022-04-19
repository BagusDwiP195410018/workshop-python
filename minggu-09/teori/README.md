# Bab 12 Environment
## Memulai Conda
Untuk memulai conda kita terlebih dahulu membuka conda promt setelah terbuka maka kita bisa melakukan aktivitas yang akan kita lakukan
## Mengelola conda
Tahap awal yang dilakukan jika ingin mengelola conda adalah dengan cara kita melihat versi terlebih dahulu dengan memasukan perintah _conda --version_ lalu selanjutnya mengupdate conda dengan perintah _conda update conda_ ketika sedang berproses kita di berikan pilihan _y dan n_ maka kita pilih _y_ untuk melanjutkan sampai akhir proses selesai.
## Mengelola lingkungan
Untuk menjalankannya kita masukan perintah _conda create --name snowflakes biopython_ tunggu proses berjalan lalu pilihlah _y_ untuk melanjutkan proses tersebut, Untuk mengaktifkan environmentnya kita masukan perintah _conda activate snowflakes_ sebab disini saya menggunakan Os Windows yang menggunakan OS linux atau MacOS menggunakan _source activate snowflakes_. Langkah yang terakhir kita lihat dengan memasukan perintah _conda info --envs_ dan apabila sudah terlist maka proses kita tersebut berhasil
## Mengelola Python
Tahap awal untuk melakukan managing python kita berikan perintah _conda create --name snakes python=3.9_ kemudian kita aktivasi dengan memasukan _conda activate snakes_ kemudian untuk melihat apakah ter verifikasi atau belum kita masukan _conda info --envs_ jika sudah ada maka sudah tersverifikasi
## Mengelola Paket
Untuk mengelola paket kita menggunakan beautifulsoup4 dengan menggunakan perintah _conda search beautifulsoup4_ kemudian baru kita masukan perintah install dengan deklarasi _conda install beautifulsoup4_ setelah itu kita cek dengan memasuka perintah _conda list_ setelah ada maka proses yang sudah kita lakukan telah berhasil