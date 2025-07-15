# MANIPULASI SET PART 2

# Union (Menggabungkan set tanpa mengubah data sumbernya)
# Atau bisa juga dibilang menggabungkan set ke dalam sebuah set baru
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel3 = parcel1.union(parcel2)
print(parcel3)

# Isdisjointn (True/False, True = jika antara kedua set tidak ada data yang sama)
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Kiwi','Melon','Pisang'}
parcel3 = {'Apel','Srikaya','Semangka'}
parcel1_parcel2 = parcel1.isdisjoint(parcel2)
parcel1_parcel3 = parcel1.isdisjoint(parcel3) # False, dikarenakan terdapat data sama yaitu 'Apel'
print(parcel1_parcel2)
print(parcel1_parcel3)

# Issubset (True/False, True = jika seluruh data pada set A terdapat pada set B)
parcel_a = {'Anggur','Apel'}
parcel_b = {'Durian','Semangka','Apel'}
parcel_c = {'Anggur','Kiwi','Apel','Jeruk','Melon'}
parcel_AB = parcel_a.issubset(parcel_b)
parcel_AC = parcel_a.issubset(parcel_c) # True dikarenakan Anggur dan Apel ada pada parcel C
print(parcel_AB)
print(parcel_AC)

# Issuperset (Sama seperti Issupertset hanya saja penulisannya terbalik)
parcel_CA = parcel_c.issuperset(parcel_a)
parcel_CB = parcel_c.issuperset(parcel_b)
print(parcel_CA)
print(parcel_CB)

# Intersection (Menampilkan data yang sama diantara kedua SET)
parcel_A = {'Anggur','Kiwi','Apel','Jeruk','Melon'}
parcel_B = {'Apel','Jeruk','Semangka','Durian','Tomat'}
parcel_C = parcel_A.intersection(parcel_B)
print(parcel_C) # Hasilnya adalah Apel dan Jeruk

# Difference (Kebalikan dari Intersection, menampilkan data yang tidak sama antara SET A dan SET B)
parcel_C = parcel_A.difference(parcel_B)
print(parcel_C) # Hanya menampilkan Anggur, Melon, dan Kiwi dikarenakan data tersebut tidak ada di SET B

# Symmetric Difference (Mengembalikan seluruh data antara SET A dan SET B yang tidak sama/saling bersinggungan)
parcel_C = parcel_A.symmetric_difference(parcel_B)
print(parcel_C)
