while True:
    try:
        # meminta input pembilang dan penyebut
        pembilang = int(input("Masukkan pembilang: "))
        penyebut = int(input("Masukkan penyebut: "))

        # menghitung hasil pembagian
        hasil = pembilang / penyebut

    # menangani error input bukan angka
    except ValueError:
        print("Input salah! Masukkan angka yang benar.")

    # menangani pembagian dengan nol
    except ZeroDivisionError :
        print("Tidak boleh membagi dengan nol!")

    # jika input benar dan tidak error
    else:
        print(f"Hasil {pembilang} dibagi {penyebut} = {hasil}")
        break  # keluar dari loop

    # selalu tampilkan pesan ini setiap akhir percobaan
    finally:
        print("Coba input lagi jika terjadi kesalahan.\n")

