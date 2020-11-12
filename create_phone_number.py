# Mendeklarasi fungsi create_phone_number
def create_phone_number(phone) :

    if len(phone) != 10 : # Conditional untuk menentukan apakah panjang phone number memenuhi syarat (panjang 10) atau tidak, bila tidak, maka akan return False karena jumlah angka harus 10
        return False
    else :
        phonestr = list(map(str, phone)) # mengubah setiap element di list phone menjadi str
        result = '' # pembuatan list kosong untuk nantinya berperan sebagai container hasil penggabungan string list phone
        for i in phonestr :
            result += i # penggabungan dilakukan untuk setiap element pada phonestr dan hasilnya akan disimpan di str result

        return '(' + result[:3] + ')' + ' ' + result[3:6] + '-' + result[6:] # mengembalikan nilai result dan digabung dengan string (, ), dan -. kemudian dengan menggunakan slicing untuk menempatkan symbol symbol tersebut di lokasi yang sudah ditentukan dalam string


print(create_phone_number([1,2,3,4,5,6,7,7,9,0]))
