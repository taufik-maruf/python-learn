# MANIPULASI SET PART 1
# Data pada set bersifat acak, tidak selalu urut, namun tidak ada duplikat

# Add (Menambahkan data)
# Catatan: Set merupakan data unique, sehingga tidak boleh ada duplikat
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.add('Melon')
print(set_buah)

# Clear (Menghapus seluruh data)
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.clear()
print(set_buah)

# Copy (Membuat salinan data)
set_buah1 = {'Jeruk','Apel','Anggur'}
set_buah2 = set_buah1
set_buah3 = set_buah1.copy()

set_buah2.add('Melon')
set_buah3.add('Kiwi')
print(set_buah1)
print(set_buah3)

# Update (Menambahkan data antar SET)
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel1.update(parcel2) # Data akan menjadi 1, namun data 'Apel' hanya akan tetap ada 1
print(parcel1)

# Pop (Menghapus data secara acak pada sebuah set)
parcel = {'Anggur','Apel','Jeruk'}
buah = parcel.pop()
print(buah)
print(parcel)

# Remove (Menghapus data tertentu)
parcel = {'Anggur','Apel','Jeruk'}
parcel.remove('Apel')
print(parcel)
