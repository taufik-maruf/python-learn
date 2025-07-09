# Mengakses List dan Tuple Part 2
bulan_pembelian = ('Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember')

# Tugas 1
# Menampilkan Bulan Mei, Juni, Juli, Agustus (Mengambil Index 4-7)
pertengahan_tahun = bulan_pembelian[4:8]
print(pertengahan_tahun)

# Tugas 2
# Menampilkan Bulan Januari, Februari, Maret, April, Mei
awal_tahun = bulan_pembelian[:5]
print(awal_tahun)

#Tugas 3
# Menampilkan Bulan September, Oktober, November, Desember
akhir_tahun = bulan_pembelian[8:]
print(akhir_tahun)

#Tugas 4
# Menggunakan Index Negatif untuk Menampilkan September, Oktober, November
print(bulan_pembelian[-4:-1])
