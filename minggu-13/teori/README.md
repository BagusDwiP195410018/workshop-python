# 10 Minutes to Pandas
## pandas
Pandas adalah sebuah library di Python yang berlisensi BSD dan open source yang menyediakan struktur data dan analisis data yang mudah digunakan. Pandas biasa digunakan untuk membuat tabel, mengubah dimensi data, mengecek data, dan lain sebagainya.

Pandas library termasuk salah satu library yang paling populer di antara banyak Python library. Pandas library sering digunakan karena kemampuannya untuk mengelola data berbentuk tabel (lebih lanjut disebut dengan dataframe) dimana sebagian besar data science project menggunakan data berbasis tabel.

## Menginstall Pandas
Pandas secara default tidak tersedia pada modul standar disaat pertama kali instalasi Python dan kita diharuskan untuk melakukan instalasi terlebih dahulu sebelum menggunakan. Untuk dapat menginstall pandas, kita bisa menjalankan perintah dengan menggunakan pip ataupun bisa menggunakan Anaconda

Dengan menggunakan pip:
`pip install pandas`

Dengan menggunakan library Anaconda, kita bisa menginstallnya dengan perintah berikut,
`conda install pandas`

Jika sudah berhasil melakukan instalasi Pandas, kita dapat menggunakannya untuk melakukan manipulasi data dengan cara import modul tersebut pada projek yang akan kita buat.
```python
import pandas as pd
import numpy as np
```

### Series
Seriesadalah array berlabel satu dimensi yang mampu menampung semua tipe data (bilangan bulat, string, angka floating point, objek Python, dll.). Label sumbu secara kolektif disebut sebagai indeks . Metode dasar untuk membuat Seri adalah dengan memanggil:
```python 
s = pd.Series(data, index=index)
```

Indeks yang diteruskan adalah daftar label sumbu. Jadi, ini terbagi menjadi beberapa kasus tergantung pada data apa itu :
Dari ndarray
Jika datandarray, indeks harus sama panjangnya dengan data . Jika tidak ada indeks yang dilewati, indeks akan dibuat dengan nilai .[0, ..., len(data) - 1]
```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])

s
Out[4]: 
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```

Data frame merupakan tabel/data tabular dengan array dua dimensi yaitu baris dan kolom. Struktur data ini merupakan cara paling standar untuk menyimpan data. Setiap kolom pada data frame merupakan objek dari Series, dan baris terdiri dari elemen yang ada pada Series.

Membuat DataFrame dengan melewatkan kamus objek yang dapat diubah menjadi struktur seperti seri:
```python 
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)


df2
Out[10]: 
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
```

Kolom yang dihasilkan DataFramememiliki tipe d yang berbeda :
```python
df2.dtypes
Out[11]: 
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```

Jika Anda menggunakan IPython, penyelesaian tab untuk nama kolom (serta atribut publik) diaktifkan secara otomatis. Berikut adalah subset dari atribut yang akan diselesaikan:
df2.<TAB>  # noqa: E225, E999
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.columns
df2.align              df2.copy
df2.all                df2.count
df2.any                df2.combine
df2.append             df2.D
df2.apply              df2.describe
df2.applymap           df2.diff
df2.B                  df2.duplicated

## Viewing data
Berikut adalah cara melihat baris atas dan bawah:
```python
df.head()
Out[13]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401

df.tail(3)
Out[14]: 
                   A         B         C         D
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```

Menampilkan indeks, kolom:
```python
df.index
Out[15]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

df.columns
Out[16]: Index(['A', 'B', 'C', 'D'], dtype='object')
```
DataFrame.to_numpy()memberikan representasi NumPy dari data yang mendasarinya. Perhatikan bahwa ini bisa menjadi operasi yang mahal ketika Anda DataFramememiliki kolom dengan tipe data yang berbeda, yang menghasilkan perbedaan mendasar antara pandas dan NumPy: NumPy array memiliki satu dtype untuk seluruh array, sedangkan pandas DataFrames memiliki satu dtype per column . Saat Anda memanggil DataFrame.to_numpy(), pandas akan menemukan dtype NumPy yang dapat menampung semua dtypes di DataFrame. Ini mungkin berakhir menjadi object, yang membutuhkan casting setiap nilai ke objek Python.

Untuk df, DataFramedari semua nilai floating-point kami, DataFrame.to_numpy()cepat dan tidak memerlukan penyalinan data:
```python
df.to_numpy()
Out[17]: 
array([[ 0.4691, -0.2829, -1.5091, -1.1356],
       [ 1.2121, -0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949,  1.0718],
       [ 0.7216, -0.7068, -1.0396,  0.2719],
       [-0.425 ,  0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784,  0.525 ]])
```

Untuk df2, DataFramedengan beberapa tipe d, DataFrame.to_numpy()relatif mahal:
```python
df2.to_numpy()
Out[18]: 
array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
      dtype=object)
      ```

describe()menunjukkan ringkasan statistik cepat dari data Anda:
```python
df.describe()
Out[19]: 
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.073711 -0.431125 -0.687758 -0.233103
std    0.843157  0.922818  0.779887  0.973118
min   -0.861849 -2.104569 -1.509059 -1.135632
25%   -0.611510 -0.600794 -1.368714 -1.076610
50%    0.022070 -0.228039 -0.767252 -0.386188
75%    0.658444  0.041933 -0.034326  0.461706
max    1.212112  0.567020  0.276232  1.071804
```
Mentransfer data Anda:
```python
df.T
Out[20]: 
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
```

Mengurutkan menurut sumbu:
```python
df.sort_index(axis=1, ascending=False)
Out[21]: 
                   D         C         B         A
2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
2013-01-02 -1.044236  0.119209 -0.173215  1.212112
2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
2013-01-04  0.271860 -1.039575 -0.706771  0.721555
2013-01-05 -1.087401  0.276232  0.567020 -0.424972
2013-01-06  0.524988 -1.478427  0.113648 -0.673690
```

Mengurutkan berdasarkan nilai:
```python
df.sort_values(by="B")
Out[22]: 
                   A         B         C         D
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
```

##  Selection
Meskipun ekspresi Python / NumPy standar untuk pemilihan dan pengaturan intuitif dan berguna untuk pekerjaan interaktif, untuk kode produksi, kami merekomendasikan metode akses data panda yang dioptimalkan, .at, .iat, .locdan .iloc.

### Getting
Memilih satu kolom, yang menghasilkan a Series, setara dengan 
```python
df.A:

df["A"]
Out[23]: 
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849
2013-01-04    0.721555
2013-01-05   -0.424972
2013-01-06   -0.673690
Freq: D, Name: A, dtype: float64
Memilih melalui [], yang mengiris baris:
```

```python
df[0:3]
Out[24]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804

df["20130102":"20130104"]
Out[25]: 
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```

### Selection by label
Apakah salinan atau referensi dikembalikan untuk operasi pengaturan, mungkin bergantung pada konteksnya. Ini kadang-kadang disebut dan harus dihindari. Lihat Mengembalikan Tampilan versus Salinan .chained assignment

pandas menyediakan serangkaian metode untuk memiliki pengindeksan berbasis label murni . Ini adalah protokol berbasis inklusi yang ketat. Setiap label yang diminta harus ada dalam indeks, atau a KeyErrorakan dinaikkan. Saat mengiris, baik batas awal DAN batas berhenti disertakan , jika ada dalam indeks. Bilangan bulat adalah label yang valid, tetapi merujuk ke label dan bukan posisi .

Atribut .locadalah metode akses utama. Berikut ini adalah input yang valid:

* Label tunggal, misalnya 5or 'a'(Catatan yang 5diinterpretasikan sebagai label indeks. Penggunaan ini bukan merupakan posisi bilangan bulat di sepanjang indeks.).

* Daftar atau larik label .['a', 'b', 'c']

* Objek irisan dengan label 'a':'f'(Perhatikan bahwa bertentangan dengan irisan Python biasa, awal dan akhir disertakan, saat ada dalam indeks! Lihat Mengiris dengan label .

* Sebuah array boolean.

* A callable, lihat Seleksi Berdasarkan Callable .

### Selection by position
pandas menyediakan serangkaian metode untuk mendapatkan pengindeksan berbasis bilangan bulat murni . Semantik mengikuti pemotongan Python dan NumPy dengan cermat. Ini adalah 0-basedpengindeksan. Saat mengiris, batas awal disertakan , sedangkan batas atas dikecualikan . Mencoba menggunakan non-integer, bahkan label yang validIndexError akan menaikkan .
Atribut .ilocadalah metode akses utama. Berikut ini adalah input yang valid:

* Sebuah bilangan bulat misalnya 5.
* Daftar atau larik bilangan bulat .[4, 3, 0]
* Sebuah objek irisan dengan ints 1:7.
* Sebuah array boolean.
* A callable, lihat Seleksi Berdasarkan Callable .

Pilih melalui posisi bilangan bulat yang diteruskan:
```python
df.iloc[3]
Out[32]: 
A    0.721555
B   -0.706771
C   -1.039575
D    0.271860
Name: 2013-01-04 00:00:00, dtype: float64
```

Dengan irisan bilangan bulat, bertindak mirip dengan NumPy/Python:
```python
df.iloc[3:5, 0:2]
Out[33]: 
                   A         B
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
```

Dengan daftar lokasi posisi bilangan bulat, mirip dengan gaya NumPy/Python:
```python
df.iloc[[1, 2, 4], [0, 2]]
Out[34]: 
                   A         C
2013-01-02  1.212112  0.119209
2013-01-03 -0.861849 -0.494929
2013-01-05 -0.424972  0.276232
```
Untuk mengiris baris secara eksplisit:
```python
df.iloc[1:3, :]
Out[35]: 
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
```

Untuk mengiris kolom secara eksplisit:
```python
df.iloc[:, 1:3]
Out[36]: 
                   B         C
2013-01-01 -0.282863 -1.509059
2013-01-02 -0.173215  0.119209
2013-01-03 -2.104569 -0.494929
2013-01-04 -0.706771 -1.039575
2013-01-05  0.567020  0.276232
2013-01-06  0.113648 -1.478427
```
Untuk mendapatkan nilai secara eksplisit:
```python
df.iloc[1, 1]
Out[37]: -0.17321464905330858
```
Untuk mendapatkan akses cepat ke skalar (setara dengan metode sebelumnya):
```python
df.iat[1, 1]
Out[38]: -0.17321464905330858
```

### Boolean indexing
Menggunakan nilai kolom tunggal untuk memilih data:
```python
df[df["A"] > 0]
Out[39]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```
Memilih nilai dari DataFrame tempat kondisi boolean terpenuhi:
```python
df[df > 0]
Out[40]: 
                   A         B         C         D
2013-01-01  0.469112       NaN       NaN       NaN
2013-01-02  1.212112       NaN  0.119209       NaN
2013-01-03       NaN       NaN       NaN  1.071804
2013-01-04  0.721555       NaN       NaN  0.271860
2013-01-05       NaN  0.567020  0.276232       NaN
2013-01-06       NaN  0.113648       NaN  0.524988
```
Menggunakan isin()metode penyaringan:
```python
df2 = df.copy()

df2["E"] = ["one", "one", "two", "three", "four", "three"]

df2
Out[43]: 
                   A         B         C         D      E
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804    two
2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three

df2[df2["E"].isin(["two", "four"])]
Out[44]: 
                   A         B         C         D     E
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
```

### Setting
Menyetel kolom baru secara otomatis menyelaraskan data dengan indeks:
```python
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

s1
Out[46]: 
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
df["F"] = s1
```
Menetapkan nilai menurut label:
```python
df.at[dates[0], "A"] = 0
```
Menetapkan nilai berdasarkan posisi:
```python
df.iat[0, 1] = 0
```
Pengaturan dengan menetapkan dengan array NumPy:
```python
df.loc[:, "D"] = np.array([5] * len(df))
```
Hasil dari operasi pengaturan sebelumnya:
```python
df
Out[51]: 
                   A         B         C  D    F
2013-01-01  0.000000  0.000000 -1.509059  5  NaN
2013-01-02  1.212112 -0.173215  0.119209  5  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0
2013-01-05 -0.424972  0.567020  0.276232  5  4.0
2013-01-06 -0.673690  0.113648 -1.478427  5  5.0
```
Operasi wheredengan pengaturan:
```python
df2 = df.copy()

df2[df2 > 0] = -df2

df2
Out[54]: 
                   A         B         C  D    F
2013-01-01  0.000000  0.000000 -1.509059 -5  NaN
2013-01-02 -1.212112 -0.173215 -0.119209 -5 -1.0
2013-01-03 -0.861849 -2.104569 -0.494929 -5 -2.0
2013-01-04 -0.721555 -0.706771 -1.039575 -5 -3.0
2013-01-05 -0.424972 -0.567020 -0.276232 -5 -4.0
2013-01-06 -0.673690 -0.113648 -1.478427 -5 -5.0
```

## Missing data
pandas terutama menggunakan nilai np.nanuntuk mewakili data yang hilang. Ini secara default tidak termasuk dalam perhitungan. Lihat bagian Data yang Hilang .

Pengindeksan ulang memungkinkan Anda untuk mengubah/menambah/menghapus indeks pada sumbu tertentu. Ini mengembalikan salinan data:
```python
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])

df1.loc[dates[0] : dates[1], "E"] = 1

df1
Out[57]: 
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5  NaN  1.0
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  NaN
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  NaN
```
Untuk menghapus setiap baris yang memiliki data yang hilang:
```python
df1.dropna(how="any")
Out[58]: 
                   A         B         C  D    F    E
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
Mengisi data yang hilang:

df1.fillna(value=5)
Out[59]: 
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5  5.0  1.0
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  5.0
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  5.0
```
Untuk mendapatkan topeng boolean di mana nilainya adalah nan:
```python
pd.isna(df1)
Out[60]: 
                A      B      C      D      F      E
2013-01-01  False  False  False  False   True  False
2013-01-02  False  False  False  False  False  False
2013-01-03  False  False  False  False  False   True
2013-01-04  False  False  False  False  False   True
```
Nilai yang dianggap "missing"
Karena data datang dalam berbagai bentuk dan bentuk, panda bertujuan untuk fleksibel dalam menangani data yang hilang. Meskipun NaNmerupakan penanda nilai hilang default untuk alasan kecepatan dan kenyamanan komputasi, kita harus dapat dengan mudah mendeteksi nilai ini dengan data dari berbagai jenis: floating point, integer, boolean, dan objek umum. Namun, dalam banyak kasus, Python Noneakan muncul dan kami juga ingin mempertimbangkan bahwa "hilang" atau "tidak tersedia" atau "NA".
Untuk mempermudah pendeteksian nilai yang hilang (dan di berbagai tipe d array), pandas menyediakan fungsi isna()and notna(), yang juga merupakan metode pada objek Seri dan DataFrame:
```python
df2["one"]
Out[7]: 
a    0.469112
b         NaN
c   -1.135632
d         NaN
e    0.119209
f   -2.104569
g         NaN
h    0.721555
Name: one, dtype: float64

pd.isna(df2["one"])
Out[8]: 
a    False
b     True
c    False
d     True
e    False
f    False
g     True
h    False
Name: one, dtype: bool

df2["four"].notna()
Out[9]: 
a     True
b    False
c     True
d    False
e     True
f     True
g    False
h     True
Name: four, dtype: bool

df2.isna()
Out[10]: 
     one    two  three   four   five
a  False  False  False  False  False
b   True   True   True   True   True
c  False  False  False  False  False
d   True   True   True   True   True
e  False  False  False  False  False
f  False  False  False  False  False
g   True   True   True   True   True
h  False  False  False  False  False
```

## Operations
### Operasi biner yang fleksibel
Dengan operasi biner antara struktur data panda, ada dua poin penting yang menarik:

* Perilaku penyiaran antara objek yang lebih tinggi (mis. DataFrame) dan berdimensi lebih rendah (mis. Seri).

* Data yang hilang dalam perhitungan.

Kami akan mendemonstrasikan bagaimana mengelola masalah ini secara mandiri, meskipun dapat ditangani secara bersamaan.

### Stats
Operasi pada umumnya mengecualikan data yang hilang.

Melakukan statistik deskriptif:
```python
df.mean()
Out[61]: 
A   -0.004474
B   -0.383981
C   -0.687758
D    5.000000
F    3.000000
dtype: float64
```
Operasi yang sama pada sumbu lainnya:
```python
df.mean(1)
Out[62]: 
2013-01-01    0.872735
2013-01-02    1.431621
2013-01-03    0.707731
2013-01-04    1.395042
2013-01-05    1.883656
2013-01-06    1.592306
Freq: D, dtype: float64
```
Beroperasi dengan objek yang memiliki dimensi berbeda dan membutuhkan penyelarasan. Selain itu, panda secara otomatis menyiarkan sepanjang dimensi yang ditentukan:
```python
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

s
Out[64]: 
2013-01-01    NaN
2013-01-02    NaN
2013-01-03    1.0
2013-01-04    3.0
2013-01-05    5.0
2013-01-06    NaN
Freq: D, dtype: float64

df.sub(s, axis="index")
Out[65]: 
                   A         B         C    D    F
2013-01-01       NaN       NaN       NaN  NaN  NaN
2013-01-02       NaN       NaN       NaN  NaN  NaN
2013-01-03 -1.861849 -3.104569 -1.494929  4.0  1.0
2013-01-04 -2.278445 -3.706771 -4.039575  2.0  0.0
2013-01-05 -5.424972 -4.432980 -4.723768  0.0 -1.0
2013-01-06       NaN       NaN       NaN  NaN  NaN
```

### Apply
Menerapkan fungsi ke data:
```python
df.apply(np.cumsum)
Out[66]: 
                   A         B         C   D     F
2013-01-01  0.000000  0.000000 -1.509059   5   NaN
2013-01-02  1.212112 -0.173215 -1.389850  10   1.0
2013-01-03  0.350263 -2.277784 -1.884779  15   3.0
2013-01-04  1.071818 -2.984555 -2.924354  20   6.0
2013-01-05  0.646846 -2.417535 -2.648122  25  10.0
2013-01-06 -0.026844 -2.303886 -4.126549  30  15.0

df.apply(lambda x: x.max() - x.min())
Out[67]: 
A    2.073961
B    2.671590
C    1.785291
D    0.000000
F    4.000000
dtype: float64
```

### Histogramming
Lihat selengkapnya di Histogram dan Diskritisasi .
```python
s = pd.Series(np.random.randint(0, 7, size=10))

s
Out[69]: 
0    4
1    2
2    1
3    2
4    6
5    4
6    4
7    6
8    4
9    4
dtype: int64

s.value_counts()
Out[70]: 
4    5
2    2
6    2
1    1
dtype: int64
```

## Metode 
Seri dilengkapi dengan sekumpulan metode pemrosesan string dalam str atribut yang memudahkan pengoperasian pada setiap elemen larik, seperti pada cuplikan kode di bawah ini. Perhatikan bahwa pencocokan pola pada strumumnya menggunakan ekspresi reguler secara default (dan dalam beberapa kasus selalu menggunakannya). Lihat lebih lanjut di Metode String Bervektor .
```python
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])

s.str.lower()
Out[72]: 
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: object
```

## Merge
### Concat
pandas menyediakan berbagai fasilitas untuk dengan mudah menggabungkan objek Seri dan DataFrame dengan berbagai jenis logika yang ditetapkan untuk indeks dan fungsionalitas aljabar relasional dalam kasus operasi tipe gabungan/gabung.

Lihat bagian Penggabungan .

Menggabungkan objek panda bersama dengan concat():
```python
df = pd.DataFrame(np.random.randn(10, 4))

df
Out[74]: 
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495

# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]

pd.concat(pieces)
Out[76]: 
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495
```


### Join
Penggabungan gaya SQL. Lihat bagian Penggabungan gaya database .
```python
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

left
Out[79]: 
   key  lval
0  foo     1
1  foo     2

right
Out[80]: 
   key  rval
0  foo     4
1  foo     5

pd.merge(left, right, on="key")
Out[81]: 
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
```
Contoh lain yang dapat diberikan adalah:
```python
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})

left
Out[84]: 
   key  lval
0  foo     1
1  bar     2

right
Out[85]: 
   key  rval
0  foo     4
1  bar     5

pd.merge(left, right, on="key")
Out[86]: 
   key  lval  rval
0  foo     1     4
1  bar     2     5
```

## Grouping
Dengan "mengelompokkan menurut" kami mengacu pada proses yang melibatkan satu atau lebih dari langkah-langkah berikut:

* Membagi data menjadi beberapa kelompok berdasarkan beberapa kriteria
* Menerapkan fungsi ke setiap grup secara mandiri
*Menggabungkan hasil ke dalam struktur data

Lihat bagian Pengelompokan .
```python
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)


df
Out[88]: 
     A      B         C         D
0  foo    one  1.346061 -1.577585
1  bar    one  1.511763  0.396823
2  foo    two  1.627081 -0.105381
3  bar  three -0.990582 -0.532532
4  foo    two -0.441652  1.453749
5  bar    two  1.211526  1.208843
6  foo    one  0.268520 -0.080952
7  foo  three  0.024580 -0.264610
```

Mengelompokkan dan kemudian menerapkan sum()fungsi ke grup yang dihasilkan:
```python
df.groupby("A").sum()
Out[89]: 
            C         D
A                      
bar  1.732707  1.073134
foo  2.824590 -0.574779
Pengelompokan berdasarkan beberapa kolom membentuk indeks hierarkis, dan sekali lagi kita dapat menerapkan sum()fungsinya:

df.groupby(["A", "B"]).sum()
Out[90]: 
                  C         D
A   B                        
bar one    1.511763  0.396823
    three -0.990582 -0.532532
    two    1.211526  1.208843
foo one    1.614581 -1.658537
    three  0.024580 -0.264610
    two    1.185429  1.348368
```

## Reshaping
Lihat bagian Hierarchical Indexing and Reshaping .

### Stack
```python
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)


index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

df2 = df[:4]

df2
Out[95]: 
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431
Metode stack()"memampatkan" level di kolom DataFrame:

stacked = df2.stack()

stacked
Out[97]: 
first  second   
bar    one     A   -0.727965
               B   -0.589346
       two     A    0.339969
               B   -0.693205
baz    one     A   -0.339355
               B    0.593616
       two     A    0.884345
               B    1.591431
dtype: float64
``` 

Dengan DataFrame atau Seri "bertumpuk" (memiliki a MultiIndexsebagai index), operasi kebalikan dari stack()adalah unstack(), yang secara default membongkar level terakhir :
```python 
stacked.unstack()
Out[98]: 
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431

stacked.unstack(1)
Out[99]: 
second        one       two
first                      
bar   A -0.727965  0.339969
      B -0.589346 -0.693205
baz   A -0.339355  0.884345
      B  0.593616  1.591431

stacked.unstack(0)
Out[100]: 
first          bar       baz
second                      
one    A -0.727965 -0.339355
       B -0.589346  0.593616
two    A  0.339969  0.884345
       B -0.693205  1.591431
```

### Tabel 
Lihat bagian tentang Tabel Pivot .
```python
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)


df
Out[102]: 
        A  B    C         D         E
0     one  A  foo -1.202872  0.047609
1     one  B  foo -1.814470 -0.136473
2     two  C  foo  1.018601 -0.561757
3   three  A  bar -0.595447 -1.623033
4     one  B  bar  1.395433  0.029399
5     one  C  bar -0.392670 -0.542108
6     two  A  foo  0.007207  0.282696
7   three  B  foo  1.928123 -0.087302
8     one  C  foo -0.055224 -1.575170
9     one  A  bar  2.395985  1.771208
10    two  B  bar  1.552825  0.816482
11  three  C  bar  0.166599  1.100230
```
Kami dapat membuat tabel pivot dari data ini dengan sangat mudah:
```python
pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
Out[103]: 
C             bar       foo
A     B                    
one   A  2.395985 -1.202872
      B  1.395433 -1.814470
      C -0.392670 -0.055224
three A -0.595447       NaN
      B       NaN  1.928123
      C  0.166599       NaN
two   A       NaN  0.007207
      B  1.552825       NaN
      C       NaN  1.018601
```

### Seri 
pandas memiliki fungsionalitas yang sederhana, kuat, dan efisien untuk melakukan operasi pengambilan sampel ulang selama konversi frekuensi (misalnya, mengubah data kedua menjadi data 5 menit). Ini sangat umum, tetapi tidak terbatas pada, aplikasi keuangan. Lihat bagian Deret Waktu .
```python
rng = pd.date_range("1/1/2012", periods=100, freq="S")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

ts.resample("5Min").sum()
Out[106]: 
2012-01-01    24182
Freq: 5T, dtype: int64
Representasi zona waktu:

rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")

ts = pd.Series(np.random.randn(len(rng)), rng)

ts
Out[109]: 
2012-03-06    1.857704
2012-03-07   -1.193545
2012-03-08    0.677510
2012-03-09   -0.153931
2012-03-10    0.520091
Freq: D, dtype: float64

ts_utc = ts.tz_localize("UTC")

ts_utc
Out[111]: 
2012-03-06 00:00:00+00:00    1.857704
2012-03-07 00:00:00+00:00   -1.193545
2012-03-08 00:00:00+00:00    0.677510
2012-03-09 00:00:00+00:00   -0.153931
2012-03-10 00:00:00+00:00    0.520091
Freq: D, dtype: float64
```

Mengonversi ke zona waktu lain:
```python
ts_utc.tz_convert("US/Eastern")
Out[112]: 
2012-03-05 19:00:00-05:00    1.857704
2012-03-06 19:00:00-05:00   -1.193545
2012-03-07 19:00:00-05:00    0.677510
2012-03-08 19:00:00-05:00   -0.153931
2012-03-09 19:00:00-05:00    0.520091
Freq: D, dtype: float64
```

Mengonversi antara representasi rentang waktu:
```python
rng = pd.date_range("1/1/2012", periods=5, freq="M")

ts = pd.Series(np.random.randn(len(rng)), index=rng)

ts
Out[115]: 
2012-01-31   -1.475051
2012-02-29    0.722570
2012-03-31   -0.322646
2012-04-30   -1.601631
2012-05-31    0.778033
Freq: M, dtype: float64

ps = ts.to_period()

ps
Out[117]: 
2012-01   -1.475051
2012-02    0.722570
2012-03   -0.322646
2012-04   -1.601631
2012-05    0.778033
Freq: M, dtype: float64

ps.to_timestamp()
Out[118]: 
2012-01-01   -1.475051
2012-02-01    0.722570
2012-03-01   -0.322646
2012-04-01   -1.601631
2012-05-01    0.778033
Freq: MS, dtype: float64
```

Konversi antara periode dan stempel waktu memungkinkan beberapa fungsi aritmatika yang nyaman digunakan. Dalam contoh berikut, kami mengonversi frekuensi triwulanan dengan tahun yang berakhir pada bulan November menjadi pukul 9 pagi pada akhir bulan setelah akhir kuartal:
```python
prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")

ts = pd.Series(np.random.randn(len(prng)), prng)

ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9

ts.head()
Out[122]: 
1990-03-01 09:00   -0.289342
1990-06-01 09:00    0.233141
1990-09-01 09:00   -0.223540
1990-12-01 09:00    0.542054
1991-03-01 09:00   -0.688585
Freq: H, dtype: float64
```

## Categoricals
pandas dapat menyertakan data kategorikal dalam file DataFrame. Untuk dokumen lengkap, lihat pengantar kategoris dan dokumentasi API .
```python
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)

Mengonversi nilai mentah menjadi tipe data kategoris:

df["grade"] = df["raw_grade"].astype("category")

df["grade"]
Out[125]: 
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): ['a', 'b', 'e']
Ganti nama kategori menjadi nama yang lebih bermakna (penugasan ke Series.cat.categories()sudah ada!):

df["grade"].cat.categories = ["very good", "good", "very bad"]
```

Susun ulang kategori dan tambahkan kategori yang hilang secara bersamaan (metode di bawah Series.cat()mengembalikan yang baru Seriessecara default):
```python
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)


df["grade"]
Out[128]: 
0    very good
1         good
2         good
3    very good
4    very good
5     very bad
Name: grade, dtype: category
Categories (5, object): ['very bad', 'bad', 'medium', 'good', 'very good']
```

Penyortiran adalah per urutan dalam kategori, bukan urutan leksikal:
```python
df.sort_values(by="grade")
Out[129]: 
   id raw_grade      grade
5   6         e   very bad
1   2         b       good
2   3         b       good
0   1         a  very good
3   4         a  very good
4   5         a  very good
```
Pengelompokan menurut kolom kategoris juga menunjukkan kategori kosong:
```python
df.groupby("grade").size()
Out[130]: 
grade
very bad     1
bad          0
medium       0
good         2
very good    3
dtype: int64
```

## Plotting
Lihat Merencanakan dokumen.

Kami menggunakan konvensi standar untuk mereferensikan matplotlib API:
```python
import matplotlib.pyplot as plt

plt.close("all")
Metode close()ini digunakan untuk menutup jendela gambar:

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

ts.plot();
```