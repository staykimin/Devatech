data = {"username":"kimin","password":"1234"}
username = input("Masukkan Username Anda :")
password = input("Masukkan Password Anda :")
x = data["username"]
y = data['password']
if username == x:
	if password == y:
		print("Berhasil Login")
	else:
		print("Password Salah")
else:
	print("Username Salah")