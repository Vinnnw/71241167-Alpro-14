try:
    file1_name = input("Masukkan nama file pertama: ")
    file2_name = input("Masukkan nama file kedua: ")

    with open(file1_name, 'r') as file1:
        isi1 = file1.read().lower().split()

    with open(file2_name, 'r') as file2:
        isi2 = file2.read().lower().split()

    set1 = set(isi1)
    set2 = set(isi2)

    hasil = set1.intersection(set2)

    print("\nKata-kata yang muncul di kedua file:")
    print(hasil if hasil else "Tidak ada kata yang sama di kedua file.")

except FileNotFoundError:
    print("File tidak ditemukan. Pastikan nama file sudah benar.")

except Exception as e:
    print("Terjadi kesalahan:", e)
