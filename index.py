while True:
    nilai = int(input("Masukkan Nilai: "))

    if 80 <= nilai <= 100:
        print("Nilai Kamu A")
    elif 70 <= nilai < 80:
        print("Nilai Kamu B")
    elif 60 <= nilai < 70:
        print("Nilai Kamu C")
    elif 50 <= nilai < 60:
        print("Nilai Kamu D")
    elif 0 <= nilai < 50:
        print("Nilai Kamu E")
    else:
        print("Nilai tidak valid. Pastikan nilai antara 0 dan 100.")
    
    pilihan = input("Apakah kamu ingin melanjutkan? (y/n): ")
    if pilihan == "y":
        continue
    elif pilihan == "n":
        print("Oke, tidak melanjutkan. Berikut piramida bintang:")
        max = 5

        # Bagian atas piramida
        for i in range(max):
            # Print spaces
            for j in range(max - i - 1):
                print(" ", end="")
            # Print stars
            for k in range(2 * i + 1):
                print("*", end="")
            print()

        # Bagian bawah piramida
        for i in range(max - 2, -1, -1):
            # Print spaces
            for j in range(max - i - 1):
                print(" ", end="")
            # Print stars
            for k in range(2 * i + 1):
                print("*", end="")
            print()

        break
