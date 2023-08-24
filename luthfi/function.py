def greeting(nama):
    print("Hallo", nama)

    def penjumlahan(A, B):
        hasil = A + B
        return hasil

    greeting("Luthfi")
hasil_penjumlahan = penjumlahan(7, 9)
print("hasil penjumlahan adalah", hasil_penjumlahan)
print(F"hasil penjumlahan adalah {hasil_penjumlahan}")

    #funfsi dengan variable panjang argument(*args)
    def jumlahkan(*args):
        total = 0
        for angka in args:
            total += angka
            return total

            hasil = jumlahkan(12, 30, 40, 50, 5, 3, 7, 700, 1000)
            print(F"hasil penjumlahan: {hasil}")
