import requests
txt = "https://www.merdeka.com/peristiwa/profil-haedar-nashir-ketum-pp-muhammadiyah-periode-2022-2027.html"
temp = requests.get(txt)
print(temp.text)