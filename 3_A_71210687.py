a = input("Mendatar/Menurun?: ")
if a == "Mendatar":
    b = int(input("Masukkan kolom: "))
    hasil = b*"#"
    print(hasil)
elif a == "Menurun":
    b = int(input("Masukkan baris: "))
    hasil = (b*("*"+"\n"))
    print(hasil)
else:
    print("Pola tidak dikenali")