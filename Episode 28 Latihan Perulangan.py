# Latihan perulangan membuat segitiga

sisi = 9

# 1. Menggunakan For

# dummy variable
print("awal dari For")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
    
print("ahir dari For")

# 2. Menggunakan while

print("awal dari while")
count = 1
while True:
    print("*"*count)
    count += 1



    if count > sisi:
        break

print("ahir dari while")

# 3. hanya ganjil saja

print("awal dari while")
count = 1
while True:
    # akan kembali keatas jika ganjil
    if count % 2:
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("ahir dari while")

# 4. hanya ganjil saja

print("awal dari while")
count = 1
spasi = int(sisi/2)
print(spasi)
while True:
    # akan kembali keatas jika ganjil
    if count % 2:
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("ahir dari while")




















