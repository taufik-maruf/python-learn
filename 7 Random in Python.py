import random

nilai_acak = random.randint(1,10)   # Menampilkan nilai acak antara 1 sampai 10 (angka berupa integer)
print(nilai_acak)

float_random = random.random()      # Menampilkan nilai acak dari 0 sampai 1 dengan tipe float
print(float_random)

# MEMBUAT PILIHAN RANDOM (YES/NO/MAYBE)

decision = random.randint(1,3)  # Variabel decision berisi angka random dari 1 sampai 3 dengan format integer

if decision == 1:
    print('YES')
if decision == 2:
    print('NO')
if decision == 3:
    print('MAYBE')
