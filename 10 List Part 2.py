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
