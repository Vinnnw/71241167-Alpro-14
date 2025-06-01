n = int(input("Masukkan jumlah kategori: "))
data_aplikasi = {}

for i in range(n):
    nama_kategori = input(f"\nMasukkan nama kategori ke-{i+1}: ")
    print(f"Masukkan 5 nama aplikasi di kategori '{nama_kategori}':")
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input(f"  Nama aplikasi ke-{j+1}: ")
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = aplikasi

print("\n--- Daftar Aplikasi per Kategori ---")
for kategori, apps in data_aplikasi.items():
    print(f"{kategori}: {apps}")

set_list = [set(apps) for apps in data_aplikasi.values()]

aplikasi_semua_kategori = set_list[0]
for s in set_list[1:]:
    aplikasi_semua_kategori = aplikasi_semua_kategori.intersection(s)

print("\n--- Aplikasi yang muncul di SEMUA kategori ---")
if aplikasi_semua_kategori:
    print(aplikasi_semua_kategori)
else:
    print("Tidak ada aplikasi yang muncul di semua kategori.")

gabungan_semua = set()
semua_kemunculan = {}

for apps in data_aplikasi.values():
    for app in apps:
        gabungan_semua.add(app)
        semua_kemunculan[app] = semua_kemunculan.get(app, 0) + 1

unik_satu_kategori = {app for app, count in semua_kemunculan.items() if count == 1}

print("\n--- Aplikasi yang hanya muncul di SATU kategori ---")
if unik_satu_kategori:
    print(unik_satu_kategori)
else:
    print("Tidak ada aplikasi yang hanya muncul di satu kategori.")

if n > 2:
    dua_kategori = {app for app, count in semua_kemunculan.items() if count == 2}
    print("\n--- Aplikasi yang muncul TEPAT di dua kategori ---")
    if dua_kategori:
        print(dua_kategori)
    else:
        print("Tidak ada aplikasi yang muncul tepat di dua kategori.")
