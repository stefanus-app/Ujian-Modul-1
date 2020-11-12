# Deklarasi Variable
num     = [5, 3, 2, 8, 1, 4]
odd     = [] # untuk menampung nilai odd yang sudah diurutkan berdasarkan kecil ke besar
even    = [] # untuk menampung nilai even yang sudah diurutkan berdasarkan besar ke kecil
result_odd  = [] # untuk menampung nilai odd yang sudah diurutkan berdasarkan kecil ke besar sesuai dengan posisi odd pada list num
result_even = [] # untuk menampung nilai even yang sudah diurutkan berdasarkan besar ke kecil sesuai dengan posisi even pada list num

# Memisah antara even dan odd list untuk diurutkan
for i in num :
    if i%2==0 : # Kondisi dimana bila tidak tersisa ketika dibagi dua mala i akan di append ke list even
        even.append(i)
    else : # Kondisi dimana bila tersisa ketika dibagi dua mala i akan di append ke list odd
        odd.append(i)

odd.sort() # sort dari kecil ke besar
even.sort(reverse=True) # sort dari besar ke kecil

# looping untuk menampung hasil odd ke result odd sesuai dengan posisi angka odd pada list num
for i in range(len(num)) :
    check = num[i] # check adalaah variable yang digunakan untuk melakukan pengecekan apakah value dalam check odd atau even
    if check % 2 != 0 :
        result_odd.append(odd[0]) # melakukan append element list odd pada index 0 ketika check adalah nilai odd
        odd.pop(0) # penghapusan element pada index 0 pada list odd. sehingga tidak akan ada pengecekan ulang untuk variable yang sama
    else :
        result_odd.append(' ') # bila check merupakan even, maka akan dilakukan append ' ' pada result odd

# looping untuk menampung hasil even ke result even sesuai dengan posisi angka even pada list num
for i in range(len(num)) :
    check = num[i] # check adalaah variable yang digunakan untuk melakukan pengecekan apakah value dalam check odd atau even
    if check % 2 == 0 :
        result_even.append(even[0]) # melakukan append element list even pada index 0 ketika check adalah nilai even
        even.pop(0) # penghapusan element pada index 0 pada list even. sehingga tidak akan ada pengecekan ulang untuk variable yang sama
    else :
        result_even.append(' ') # bila check merupakan odd, maka akan dilakukan append ' ' pada result even

print(result_odd)
print(result_even)
