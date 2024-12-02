# Program utama
print("Selamat Datang Di Aplikasi Konversi!")
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}!")

while True:
    # Menu Konversi
    print("Menu Konversi:")
    print("1. Suhu")
    print("2. Panjang")
    print("3. Waktu")
    pilihan = input("Pilih jenis konversi (1/2/3): ")

    # Proses Konversi Suhu
    if pilihan == '1':
        print("Konversi Suhu:")
        print("a. Celcius ke Farenheit")
        print("b. Celcius ke Kelvin")
        print("c. Celcius ke Reamur")
        sub_pilihan = input("Pilih konversi (a/b/c): ")
        celcius = float(input("Masukkan suhu dalam Celcius: "))

        if sub_pilihan == 'a':
            hasil = (celcius * 9/5) + 32
            print(f"{celcius} °C = {hasil} °F")
        elif sub_pilihan == 'b':
            hasil = celcius + 273.15
            print(f"{celcius} °C = {hasil} K")
        elif sub_pilihan == 'c':
            hasil = celcius * 4/5
            print(f"{celcius} °C = {hasil} °R")
        else:
            print("Pilihan tidak valid.")

    # Proses Konversi Panjang
    elif pilihan == '2':
        print("Konversi Panjang:")
        print("a. KM ke M")
        print("b. M ke CM")
        print("c. CM ke MM")
        sub_pilihan = input("Pilih konversi (a/b/c): ")

        if sub_pilihan == 'a':
            km = float(input("Masukkan panjang dalam KM: "))
            hasil = km * 1000
            print(f"{km} KM = {hasil} M")
        elif sub_pilihan == 'b':
            m = float(input("Masukkan panjang dalam M: "))
            hasil = m * 100
            print(f"{m} M = {hasil} CM")
        elif sub_pilihan == 'c':
            cm = float(input("Masukkan panjang dalam CM: "))
            hasil = cm * 10
            print(f"{cm} CM = {hasil} MM")
        else:
            print("Pilihan tidak valid.")

    # Proses Konversi Waktu
    elif pilihan == '3':
        print("Konversi Waktu:")
        print("a. Hari ke Jam")
        print("b. Jam ke Menit")
        print("c. Menit ke Detik")
        sub_pilihan = input("Pilih konversi (a/b/c): ")

        if sub_pilihan == 'a':
            hari = float(input("Masukkan waktu dalam Hari: "))
            hasil = hari * 24
            print(f"{hari} Hari = {hasil} Jam")
        elif sub_pilihan == 'b':
            jam = float(input("Masukkan waktu dalam Jam: "))
            hasil = jam * 60
            print(f"{jam} Jam = {hasil} Menit")
        elif sub_pilihan == 'c':
            menit = float(input("Masukkan waktu dalam Menit: "))
            hasil = menit * 60
            print(f"{menit} Menit = {hasil} Detik")
        else:
            print("Pilihan tidak valid.")

    else:
        print("Pilihan tidak valid.")

    lagi = input("Apakah Anda ingin melakukan perhitungan lagi? (ya/tidak): ")
    if lagi.lower() != 'ya':
        break

print("Terima kasih telah menggunakan aplikasi Baden Dan Adit!")

# Cetak pola berlian langsung
size = 5
for i in range(size):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))
for i in range(size - 1, -1, -1):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))

    #Link Repository Github: https://github.com/Denngrh/UTS-algoritma
    #Link Video Youtube: https://youtu.be/VZnkbEH9g9A?si=IBBaQuYICDg7U2SF