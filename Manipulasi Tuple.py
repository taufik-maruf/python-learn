# TUPLE MANIPULATION

# Count (Menghitung jumlah kemunculan data)
tuple_score = ('Budi','Sud','Budi','Budi','Budi','Sud','Sud')
budi_total = tuple_score.count('Budi') # Menghitung jumlah kemunculan 'Budi' pada data
sud_total = tuple_score.count('sud') # Memiliki sifat case sensitive
print(budi_total)
print(sud_total)

# Index (Mengembalikan indeks pertama dari data yang dicari)
urutan_sud = tuple_score.index('Sud')+1
print(urutan_sud)
