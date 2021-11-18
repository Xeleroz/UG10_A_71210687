print(28*"#")
print("Kalkulator Advance Sederhana")
print(28*"#")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan kebawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")
pilihan = int(input("Masukkan menu yang anda pilih: "))
if pilihan == 1:
    a = float(input("Masukkan bilangan yang ingin dibagi: "))
    b = float(input("Masukkan bilangan pembagi: "))
    hasil = (a % b)
    print("Sisa hasil bagi", a, "dibagi dengan", b, "adalah", hasil)
elif pilihan == 2:
    a = float(input("Masukkan bilangan yang ingin dibagi: "))
    b = float(input("Masukkan bilangan pembagi: "))
    hasil = (a // b)
    print("Hasil pembagian", a, "dibagi dengan", b, "adalah", hasil)
elif pilihan == 3:
    x = float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    hasil = (x**(1/3))
    print("Akar kubik dari", x, "Adalah", hasil)
else:
    print("Menu yang anda pilih tidak tersedia")