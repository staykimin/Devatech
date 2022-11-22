nama = input("Masukkan Nama : ")
nilai = input("Masukkan Nilai : ")

if int(nilai) < 50:
	grade = "Tidak Lulus"

elif int(nilai) >= 50 and int(nilai) <= 75:
	grade = "C"

elif int(nilai) > 75 and int(nilai) <= 85:
	grade = "B"

elif int(nilai) > 85 and int(nilai) <= 100:
	grade = "A"
else:
	grade = "Nilai Tidak Sesuai"

if grade == "Tidak Lulus" or grade == "C":
	ket = "Remidial"
elif grade == "Nilai Tidak Sesuai":
	ket = "Nilai Tidak Boleh Lebih Dari 100"
else:
	ket = "Lulus"
	
print("Nama Anda Adalah ",nama)
print("Nilai Anda Adalah ",nilai)
print("Grade Nilai Anda Adalah ",grade)
print("Keterangan Anda Adalah ",ket)
