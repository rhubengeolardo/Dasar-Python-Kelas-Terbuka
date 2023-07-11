## ----- LIST ----

# Kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

# Kumpulan data string
data_string = ["ucup","otong","odah"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan data campuran
data_campuran = [1,"bala-bala",2,"cireng",True,"otong",False]
print(data_campuran)

## Cara alternatif membuat list
data_range = list(range(0,10,2)) # range(start,stop,step)
print(data_range)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**10 for i in range(0,10)]
print(list_pake_for)

for i in range(0,10):
    data = i**2
    
# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)








