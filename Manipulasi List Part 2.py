# MANIPULASI LIST PART 2

# Index (Mengembalikan indeks data pertama yang dicari)
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_pertama_sud = list_score.index('Sud')+1
print(score_pertama_sud)

# Insert (Menyisipkan data pada indeks tertentu)
list_score = ['Budi','Sud','Budi','Budi','Sud']
list_score.insert(3,'Sud') # Memasukan nilai 'Sud' pada indeks ke 3
print(list_score)

# Pop (Menghilangkan data pada indeks tertentu)
list_menu = ['Gado-gado','Ayam Goreng','Rendang']
list_menu.pop(1) # Mengeluarkan data pada indeks ke 1 pada list
print(list_menu)

# Remove (Menghilangkan data tertentu secara spesifik)
list_menu = ['Gado-gado','Ayam Goreng','Rendang','Ketoprak']
list_menu.remove('Rendang') # Menghilangkan 'Rendang' dari list
print(list_menu)

# Reverse (Membalik urutan list)
list_menu = ['Gado-gado','Ayam Goreng','Rendang','Ketoprak']
list_menu.reverse()
print(list_menu)

# Sort (Mengurutkan Data)
list_menu = ['Gado-gado','Ayam Goreng','Rendang','Ketoprak']
list_menu.sort() # Secara default hasilnya Ascending
print(list_menu)
list_menu.sort(reverse=True) # Mengurutkan secara Descending
print(list_menu)
