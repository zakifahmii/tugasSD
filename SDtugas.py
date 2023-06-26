# Revisi Tugas Kelompok Struktur Data
# Kelompok 4
import sys as prog

def garis():
    print("------------------------------------------------")
    
def main():
    print("================================================")
    print("                 Program Matriks")
    print("            Mata Kuliah Struktur Data")
    print("================================================")
    
    print("Pilihlah program yang akan kamu lakukan")
    print("1. Triangular Upper\n2. Triangular Lower\n3. Sparse Array")
    pilih = input("Pilih (1/2/3): ")
    
    garis()
    if pilih == "1":
        def ut(n):
            arr = [[0] * n for _ in range(n)]
            num = 1 
            for a in range(n):
                for b in range(a, n):
                    arr[a][b] = num
                    num += 1
            return arr

        n = int(input("Masukkan Banyak Elemen: "))
        garis()
        hasil = ut(n)
        print("Upper Trigular Array")

        for upper in hasil:
            print(upper)

    elif pilih == "2":
        def ut(n):
            arr = [[0] * n for _ in range(n)]
            num = 1 
            for a in range(n):
                for b in range(a + 1):
                    arr[a][b] = num
                    num += 1
            return arr
        
        n = int(input("Masukkan Banyak Elemen: "))
        garis()
        hasil = ut(n)
        print("Lower Trigular Array")

        for lower in hasil:
            print(lower)

    elif pilih == "3":
        class SparseArray:
            def __init__(self, rows, cols):
                self.rows = rows
                self.cols = cols
                self.data = {}

            def set_value(self, row, col, value):
                if value != 0:
                    self.data[(row, col)] = value

            def get_value(self, row, col):
                return self.data.get((row, col), 0)

            def print_array(self):
                for i in range(self.rows):
                    for j in range(self.cols):
                        print(self.get_value(i, j), end=' ')
                    print()
        
        x = int(input("Masukkan Banyak Elemen Baris: "))
        y = int(input("Masukkan Banyak Elemen Kolom: "))
        spArr = SparseArray(x,y)
        garis()
        print("Masukkan 3 angka kedalam 4 value!")
        matriks = []
        for i in range(x):
            row = []
            for j in range(y):
                elemen = int(input(f"Masukkan elemen matriks [{i}][{j}]: "))
                row.append(elemen)
            matriks.append(row)

        # Menampilkan matriks
        print("Matriks yang diinput:")
        for row in matriks:
            print(row)
        
        # spArr.set_value(matriks)
        spArr.print_array()
        
while True: 
    main() 
    ulang = input("\nIngin membuat matrix lagi?(Y/N): ")
    if ulang == 'Y' or ulang == 'y':
        print("\n")
        continue 
    elif ulang == 'N' or ulang == 'n':
        prog.exit() 
    else: 
        print("Ada Kesalahan!")
        prog.exit() 
