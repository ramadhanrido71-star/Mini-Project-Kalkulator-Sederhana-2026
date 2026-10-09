# Operasi Kalkulator Sederhana

print("===========================================")
print("======== KALKULATOR SEDERHANA =========")
print("===========================================")

print(" Powered By Mohamed Ridho Sunami ")

print("=============================================")
print("Pilihan Operasi")
print("1. Tambah")
print("2. Kurang")
print("3. Bagi")
print("4. Kali")
print("=============================================")

operasi = int(input("Masukkan pilihan Operasi: "))

if operasi == 1:
    x = int (input("Masukkan Nilai Pertama: "))
    y = int (input("Masukkan Nilai Kedua :"))
    z = x + y 
    print(" Hasilnya adalah : ", x, "+", y, "=", z)
    print("=========================================")

elif operasi == 2:
    x = int (input("Masukkan Nilai Pertama: "))
    y = int (input("Masukkan Nilai Kedua :"))
    z = x - y 
    print(" Hasilnya adalah : ", x, "-", y, "=", z)
    print("=========================================")

elif operasi == 3:
    x = int (input("Masukkan Nilai Pertama: "))
    y = int (input("Masukkan Nilai Kedua :"))
    z = x / y 
    print(" Hasilnya adalah : ", x, "/", y, "=", z)
    print("=========================================")

elif operasi == 4:
    x = int (input("Masukkan Nilai Pertama: "))
    y = int (input("Masukkan Nilai Kedua :"))
    z = x * y 
    print(" Hasilnya adalah : ", x, "*", y, "=", z)
    print("=========================================")

