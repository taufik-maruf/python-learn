movies = ['Batman','Spiderman','Superman']

total = len(movies) # Menghitung panjang data/banyaknya data
print(f'Total Judul:{total}')   # Akan menampilkan total = 3

# MENAMBAHKAN DATA
movies.append('Iron-man')       # Menambahkan data pada list dan meletakan pada posisi terakhir
total = len(movies)
print(f'Total Judul:{total}')   # Total akan menjadi 4
print(movies)                   # Menampilkan list terbaru (terdapat tambahan 'Iron-man')

movies.insert(1,'Thor')         # Menambahkan data baru ke dalam list ke 1, sehingga list sisanya tergeser
print(movies)                   # Hasil --> ['Batman', 'Thor', 'Spiderman', 'Superman', 'Iron-man']

del(movies[0])                  # Akan menghapus daftar dengan indeks ke 0
print(movies)                   # Hasil --> ['Thor', 'Spiderman', 'Superman', 'Iron-man']

# MENGHAPUS HINGGA TERSISA 1
del(movies[1])
del(movies[1])
del(movies[1])
print (movies)                  # Data hanya akan tersisa 'Thor' saja

# CATATAN TAMBAHAN
# pada penghapusan dilakukan berkali-kali pada indeks ke 1 dikarenakan setelah dihapus data akan bergeser
# Jadi tidak bisa menggunakan del(movies[1/2/3])

# MENCOBA MENGHAPUS LANGSUNG TANPA MENULIS BEBERAPA BARIS KODE
movies = ['Batman', 'Thor', 'Spiderman', 'Superman', 'Iron-man']
del(movies[1:5])
print(movies)
# Dapat Menggunakan seperti ini ternyata

# ATAU
movies = ['Batman', 'Thor', 'Spiderman', 'Superman', 'Iron-man']
del(movies[1:len(movies)])
print(movies)
# Bisa juga menggunakan ini, akan menghapus data dari indeks 1 hingga terakhir dengan lebih fleksibel
