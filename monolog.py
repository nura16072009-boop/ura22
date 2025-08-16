import sys
import time


def jalanin_lirik():
    # Ubah lirik lagu dan delay hurufnya sesuai yang kalian mau
    lirik = [
        ("Bunga di bulan sepi", 0.20),
        ("Jatuh terdampar", 0.09),
        ("Tersasar", 0.09),
        ("Alasan masih bersama", 0.10),
        ("Bukan karena terlanjur lama", 0.09),
        ("Tapi rasanya", 0.09),
        ("Yang masih sama", 0.09),
    ]

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay = [3.0, 3.3, 4.0, 3.9, 3.6, 2.0, 2.10]
    # Ubah judul lagu
    print("\n== Monolog-Pamungkas ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    # Ganti nama pembuat
    print("// Code by Micola Arighi")


jalanin_lirik()