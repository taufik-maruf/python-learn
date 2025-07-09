# LIST MANIPULATION PART 1

# Append (Menambahkan data, namun diletakkan paling akhir)
list_makanan = ['Gado-gado','Ayam Goreng','Rendang']
list_makanan.append('Ketoprak')
print(list_makanan)

# Clear (Menghapus seluruh data pada list)
list_makanan.clear()
print(list_makanan)

# Copy (Menyalin data)
list_makanan1 = ['Gado-gado','Ayam Goreng','Rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1

list_makanan2.append('Ketoprak')
list_makanan3.append('Opor')

print(list_makanan2)
print(list_makanan1)

# Count (Menghitung data tertentu dari sebuah list)
# COUNT BERSIFAT 'CASE SENSITIVE'
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi)
print(score_sud)

# Extend (Menggabungkan List)
list_menu = ['Gado-gado','Ayam Goreng','Rendang']
list_minuman = ['Es Teh','Es Jeruk','Es Campur']
list_menu.extend(list_minuman)
print(list_menu)
