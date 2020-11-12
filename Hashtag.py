# Deklarasi Fungsi Hastag
def Hashtag (string) :
    if len(string) > 140 : # Selection untuk menentukan apakah jumlah characters string melebihi 140, jika ya, return akan False
        return False

    elif len(string) == 0 :# Selection untuk menentukan apakah jumlah characters string = 0 (string kosong), jika ya, return akan False
        return False

    else : # bila kedua kondisi di atas tidak terpenuhi, maka string sesuai syarat untuk pemberian hashtag di depan
        string = string.title().split() # fungsi title pada string digunakan untuk memberi huruf capital setiap awalan kata, kemudian dilakukan fungsi split agar menjadi list
        string.insert(0, '#') # pemberian hashtag pada list string pada index 0

        return ''.join(string) # menggabungkan list string menjadi str string (tanpa pemisah)

print(Hashtag("Hello there how are you doing"))
print(Hashtag("     Hello     World   "))
print(Hashtag(''))