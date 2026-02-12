#Buat sebuah fungsi bernama hitung(a, b) yang:
#Menerima dua parameter a dan b
#Mengembalikan hasil penjumlahan a + b
#Mengembalikan hasil pengurangan a - b
#Kemudian memanggil fungsi tersebut 
#Menampilkan hasil penjumlahan dan pengurangannya sebagai output

def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b 
    return a + b, a - b 

hasil_jumlah, hasil_kurang = hitung(5, 3) 

print("hasil penjumlahan =", hasil_jumlah)
print("hasil pengurangan =", hasil_kurang)
