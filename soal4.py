# Program: Jadwal Per Hari Prodi (Versi Multi Mata Kuliah)

def jadwal_hari(hari):
    """
    Menampilkan 1 atau lebih mata kuliah berdasarkan nama hari.
    """
    jadwal = {
        "Senin": ["Teknik Digital", "Pemrograman Python"],
        "Selasa": ["Pengantar IoT"],
        "Rabu": ["Bahasa Inggris"],
        "Kamis": ["Pemrograman Python", "Pengantar IoT"],
        "Jumat": ["Teknik Digital"]
    }

    # Normalisasi input agar tidak case sensitive
    hari_cap = hari.capitalize()

    if hari_cap in jadwal:
        daftar = jadwal[hari_cap]
        teks_matkul = "\n- ".join(daftar)
        return f"Jadwal hari {hari_cap}:\n- {teks_matkul}"
    else:
        return "Tidak ada jadwal pada hari tersebut."


# Contoh pemanggilan
print(jadwal_hari("Senin"))
print(jadwal_hari("rabu"))
print(jadwal_hari("Minggu"))
