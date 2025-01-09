nilai = int(input("Masukan Nilai: "))

if 85 <= nilai <= 100:
    print("A")
elif 70 <= nilai <= 84:
    print("B")
elif 50 <= nilai <= 69:
    print("C")
elif 0 <= nilai <= 49:
    print("D")
else:
    print("Tidak ada")