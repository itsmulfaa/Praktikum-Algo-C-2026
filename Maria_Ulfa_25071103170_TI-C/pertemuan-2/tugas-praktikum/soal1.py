#soal 1 (function dan validasi data)
def rata_rata(nilai):
    if len(nilai) == 0:
        return "Data kosong"
    else:
        total = sum(nilai)
        jumlah = len(nilai)
        return total / jumlah

nilai_mahasiswa = [80, 75, 90, 60, 85]

hasil = rata_rata(nilai_mahasiswa)
print("Rata-rata nilai mahasiswa : ", hasil)
