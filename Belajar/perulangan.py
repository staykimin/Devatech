nilai1 = int(input("Masukkan Nilai 1 : "))
nilai2 = int(input("Masukkan Nilai 2 : "))
operasi = input("+-/*%")
if operasi == "+":
	hasil = nilai1 + nilai2
elif operasi == "-":
	hasil = nilai1 - nilai2
elif operasi == "*":
	hasil = nilai1 * nilai2
elif operasi == "/":
	hasil = nilai1 / nilai2	
elif operasi == "%":
	hasil = nilai1 % nilai2

print(hasil)