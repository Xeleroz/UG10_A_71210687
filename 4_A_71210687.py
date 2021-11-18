a = input("Masukkan artikel yang ingin dipindai: ")
b = input("Masukkan nama klub favorit anda: ")
c = input("Masukkan skor yang ingin dicari: ")
if c in a and b in a:
    print("Hasil pencarian ditemukan")
elif b in a:
    print("Hanya kata {} yang ditemukan pada artikel ini".format(b))
elif c in a:
    print("Hanya skor {} yang ditemukan pada artikel ini".format(c))
else:
    print("Hasil pencarian {} dan {} tidak ditemukan".format(b,c))