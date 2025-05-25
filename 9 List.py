example_list = ['Money',1,2,4.5,'Book',True]    # List dapat diisikan berbagai macam tipe data, tidak harus sama semua
print(example_list)

# MENGAMBIL DATA TERTENTU DALAM LIST
print(example_list[0])  # Akan menampilkan data 'Money' dikarenakan list dimulai dari 0
print(example_list[-1])  # Akan menampilkan data True

# MENAMPILKAN DATA DARI LIST SECARA RANDOM
import random
movies = ['Spiderman','Batman','Superman']
random_number = random.randint(0,2)

print(movies[random_number])    # Akan menampilkan secara random Spiderman/Batman/Superman
