nilai = input('Masukkan Nilai : ')
if int(nilai) < 50:
	print("D")
elif int(nilai) >= 50 and int(nilai) <= 65:
	print("C")
elif int(nilai) > 65 or int(nilai) < 85:
	print("B")
else:
	print("Tidak Diketahui")

