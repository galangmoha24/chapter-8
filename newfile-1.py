listku = []
listku_2=0
while True:
    
    angka = int(input("tambah nilai : "))
    listku.append(angka)
    listku_2+=angka
    if angka==0:
    	break

print(listku)
print(f"rata rata={listku_2}")