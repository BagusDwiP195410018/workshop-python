# Menggunakan dataset diabetes
https://www.kaggle.com/datasets/vikasukani/diabetes-data-set
## Beberapa Langkah pengerjaan
Memanipulasi data banyak caranya dan di bawah ini adalah beberapa langkah dalam manipulasi data :
### Manipulasi
    1. import dan pembacaan file

    import pandas as pd
    df=pd.read_csv('diabetes-dataset.csv')
    print(df.head(5))
    
    Perintah tersebut digunakan untuk melakukan import pandas untuk melakukan manipulasi data pada perintah df=pd.read_csv itu adalah perintah untuk membaca file yang berjenis csv yang kemudian diikuti nama file yang akan di tampilkan atau dibaca tersebut dan gunakan print untuk menampilkan data frame tersebut
    2. Melihat jumlah data

    df.shape
    Digunakan untuk mengetahui berapa jumlah dan columns pada data tersebut sehingga dapat diketahui dengan cepat dan tepat

    3. Melihat nama columns

    df.columns
    Digunakan untuk mengetahui nama - nama columns yang digunakan dalam data tersebut

    4. Melihat data dari suatu variabel

    print(df['Glucose'])
    Perintah tersebut digunakan untuk mengetahui data dari variabel yang di panggil sehingga hanya akan memuncul data data dari variabel tersebut

    5. Melihat data dengan 2 variabel

    df[['Age','Glucose']]
    Digunakan untuk melihat data dengan 2 variabel yang berbeda sehingga akan menampilkan 2 data

    6. Mencari mean suatu data

    df['Glucose'].mean()
    Perintah itu digunakan untuk mencari mean suatu data sesuai dengan variabel data yang di panggil