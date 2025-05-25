# LUCKY NUMBER
import random

lucky_num = random.randint(1,100)

fortune_num = random.randint(1,3)
fortune_txt = ''

if fortune_num == 1:
    fortune_txt = 'This year you\'ll be Lucky'
elif fortune_num == 2:
    fortune_txt = 'This year just like another year'
elif fortune_num == 3:
    fortune_txt = 'This year will be tough'

print(f'{fortune_txt}. Your Lucky number is: {lucky_num}')

# EXPLANATION
# ELIF --> jika pada statement pertama tidak sesuai akan melakukan pengecekan pada ELIF, namun jika sesuai maka seuruh ELIF akan diabaikan
# ELIF sangat membantu untuk mempercepat eksekusi kode
# Jika semua menggunakan IF maka semua statement akan dilakukan pengecekan dahulu
