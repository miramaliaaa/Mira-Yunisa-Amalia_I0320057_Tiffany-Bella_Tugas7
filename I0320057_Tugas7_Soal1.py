#1 program menggunakan fungsi string
def soalsatu(str):
    print(str)
    print("---"*10)

    print("1.Capitalize")
    s = str.capitalize()
    print(s)

    print("\n2.Endswith")
    print("Nama akhir anda ramadhan =", str.endswith("ramadhan"))

    print("\n3.Center")
    s = str.center(29, '=')
    print(s)

    print("\n4.Count")
    a = str.count('f')
    b = str.count('m')
    print ('jumlah huruf f = ', a)
    print ('jumlah huruf m = ', b)

    print("\n5.Upper and Lower")
    upper = str.upper()
    lower = str.lower()
    print('kapital :', upper)
    print('tidak kapital :', lower)


str = input("Masukkan Nama awal dan akhir anda :")
soalsatu(str)