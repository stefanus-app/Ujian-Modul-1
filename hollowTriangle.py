# Mendefinisikan fungsi segitiga
def hollowTriangle(height) :
    # Looping untuk membuat index
    for i in range(height) :

        _first  = (height-1) - i # menentukan point pertama pemberian hash
        _last   = (height-1) + i # menentukan point akhir pemberian hash

        # Looping untuk kolom
        for j in range((height*2)-1) : # height di kali 2 agar bisa menjadi segitiga sama kaki, kemudian dikurang angka 1 agar sisa akhir tidak usah diproses, dengan demikian space awalan dan akhiran menjadi sama
            if i != height-1 : # bila index tidak sama dengan tinggi segitiga, maka akan menggunakan '_' bila kolom tidak berada pada point _first dan _last
                if j == _first or j == _last :
                    print('#', end ='')
                else :
                    print('_', end ='')
            else : # bila index berada pada index paling akhir (height-1), maka seluruh kolom akan di print menggunakan '#' tanpa ada '_'
                if _first <=  j <= _last :
                    print('#', end ='')
                else :
                    print('', end ='')
        print()

hollowTriangle(1)
print()
hollowTriangle(2)
print()
hollowTriangle(3)
print()
hollowTriangle(4)
print()
hollowTriangle(5)
print()
hollowTriangle(6)
