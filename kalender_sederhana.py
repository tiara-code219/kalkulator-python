import os
os.system("cls")

while True:
    print("\nPilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    
    operasi = input("Masukkan pilihan (1/2/3/4/5): ")
    
    if operasi == "5":
        print("Keluar dari program.")
        break 

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    if operasi == "1":
        hasil = angka1 + angka2
        print("Hasil penjumlahan:", hasil)
    elif operasi == "2":
        hasil = angka1 - angka2
        print("Hasil pengurangan:", hasil)
    elif operasi == "3":
        hasil = angka1 * angka2
        print("Hasil perkalian:", hasil)
    elif operasi == "4":
        if angka2 == 0:
            print("Tidak bisa dibagi nol")
        else:
            hasil = angka1 / angka2
            print("Hasil pembagian:", hasil)
    else:
        print("Pilihan tidak valid.")
