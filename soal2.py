# Program Koperasi: Menghitung Kategori Setoran Mingguan

# 1) Meminta tiga angka satu per satu
s1 = int(input("Masukkan setoran pertama: "))
s2 = int(input("Masukkan setoran kedua: "))
s3 = int(input("Masukkan setoran ketiga: "))

# 4) Validasi: jika ada input ≤ 0
if s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("Input tidak valid.")
else:
    # 2) Menjumlahkan semuanya
    total = s1 + s2 + s3

    # 3) Menentukan kategori berdasarkan total
    if total < 300000:
        print("Kategori: Rendah")
    elif total < 600000:
        print("Kategori: Sedang")
    else:
        print("Kategori: Tinggi")

    # Tampilkan total setoran juga (opsional)
    print(f"Total setoran: Rp{total:,}")
