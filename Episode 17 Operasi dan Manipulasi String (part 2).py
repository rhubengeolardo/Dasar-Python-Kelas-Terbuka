# operator dalam betuk methods

## merubah case dari string

# meerubah semua ke upper case

salam = "bro"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieezZzZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek apakah semua huruf
# isalnum() <-- huruf dan angka
# isdesimal() <-- angka saja
# ispace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai huruf besar

judul = "It is Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswite() endswith() <--keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))
cek_start = "Sangjangnim Oppa".startswith("sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))
cek_end = "Sangjangnim Oppak".endswith("oppak")
print("end = " + str(cek_end))

## penggabungan komponen join()
pisah =['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
print(5*"=" + "data" + "="*5)

kanan = "surotong".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikannya --> strip()
tengah = tengah.strip("-")
print("'"+tengah+"'")

kanan = kanan.strip(" ")
print("'"+kanan+"'")