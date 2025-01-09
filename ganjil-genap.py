awal = int(input("Masukan Nilai awal: "))
akhir = int(input("Masukan Nilai akhir: "))

print("Bilangan Genap")
for num in range(awal, akhir + 1):
    if num % 2 == 0:
        print(num, end=" ")
        
print("\nBilangan Ganjil")
for num in range(awal, akhir + 1):
    if num % 2 != 0:
        print(num, end=" ")
