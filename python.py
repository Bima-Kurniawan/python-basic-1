# PYTHON "HELLO WORLD" & STATEMENT

print("Hello World.")
print("Saya Bima, baru belajar Python.")

# VARIABLES DI PYTHON

""""
1. Nama dari sebuah variabel harus dimulai dengan huruf (a-z, A-Z)
atau karakter garis bawah/underscore (_) dan tidak dapat dimulai dengan angka (0-9).
2. Variabel hanya boleh mengandung karakter alfabet dan bilangan dan underscore
(a-z, A-Z, 0-9, _)
3. Variabel bersifat case-sensitive yang mengartikan bahwa
variabel TINGGI, tinggi, dan Tinggi merujuk pada tiga variabel berbeda.
"""
angka1 = 2
Angka_2 = 11
Kata = "Halo Dunia"
angka1, Angka_2 = 2,11
pembuka = "Selamat Pagi"; Penutup = "Salam Sejahtera"

# COMMENTS DI PYTHON

# perintah pada baris ini tidak mempengaruhi program
'''
perintah ini tidak akan dieksekusi oleh Python
dan perintah ini juga tidak akan dieksekusi
perintah ini juga tidak akan dieksekusi
'''
print("jadi # digunakan untuk membuat comment pada Python")

# TIPE DATA DI PYTHON
"""
str : Tipe data teks yang dapat berupa huruf, kata, frasa, kalimat atau 
paragraf yang diapit oleh ‘ atau “

Contoh:
“a”; ‘b’; ‘saya’; “Belajar Python”; “Kita makan nasi goreng”

list : Urutan bilangan dan teks yang diapit oleh kurung siku 
dan masing-masing elemennya dipisahkan dengan koma.

Contoh:
[-9.52, None, True, “saya”]

Tuple : Urutan bilangan dan teks yang diapit oleh kurung biasa dan 
masing-masing elemennya dipisahkan dengan koma.

Contoh:
(-9.52, None, True, “saya”)

set : 	
Urutan bilangan dan teks yang diapit oleh kurung biasa dan 
masing-masing elemennya dipisahkan dengan koma. Setiap elemennya bernilai unik.

Contoh:
{1, 4, 4, 3} → {1, 3, 4}
"""
text = "Belajar Python di DQLab."
print(list(text))
print(tuple(text))
print(set(text))

# MENGGUNAKAN LIBRARY DI PYTHON

import math
import numpy as np 
import pandas as pd
import seaborn as sns

