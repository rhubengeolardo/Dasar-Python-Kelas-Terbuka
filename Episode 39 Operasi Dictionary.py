# operator dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surundung"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak 
KEY = "kis"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"faqih":"faqihza si kweren"}) # kalau gak ada di add aja bos
print(data_dict)

# mendelate data pada dictionary
del data_dict["faqih"]
print(data_dict)