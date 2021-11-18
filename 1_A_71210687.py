a = float(input("Masukkan nilai rata-rata UG anda: "))
b = float(input("Masukkan nilai TTS anda: "))
c = float(input("Masukkan nilai TAS anda: "))
print(25*"=")
nilaitotal= (a*70)/100+(b*15)/100+(c*15)/100
if nilaitotal >= 85:
    huruf = "A"
elif nilaitotal >= 80:
    huruf = "-A"
elif nilaitotal >= 75:
    huruf = "B+"
elif nilaitotal >= 70:
    huruf = "B"
elif nilaitotal >= 65:
    huruf = "B-"
elif nilaitotal >= 60:
    huruf = "C+"
elif nilaitotal >= 55:
    huruf = "C"
elif nilaitotal >= 45:
    huruf = "D"
else:
    huruf = "E"
print("Nilai anda:", nilaitotal)
print("Nilai huruf anda: ", huruf)