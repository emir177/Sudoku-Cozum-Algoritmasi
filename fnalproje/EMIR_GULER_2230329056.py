# verilen 9x9 sudokuyu çözen algoritma
def kontrol(girdi, satir, sutun, num):
    # satirda tekrar eden sayi var mi kontrol eder
    for i in range(9):
        if girdi[satir][i] == num:
            return False

    # sutunda tekrar eden sayi var mi kontrol eder 
    for i in range(9):
        if girdi[i][sutun] == num:
            return False

    # 3x3 luk kareleri kontrol eder
    basl_satir = (satir // 3) * 3
    basl_sutun = (sutun // 3) * 3
    for i in range(3):
        for j in range(3):
            if girdi[basl_satir + i][basl_sutun + j] == num:
                return False

    return True

# cozum icin backtracking algoritmasi
def cozum(girdi):
    for satir in range(9):
        for sutun in range(9):
            if girdi[satir][sutun] == 0:
                for num in range(1, 10):
                    if kontrol(girdi, satir, sutun, num):
                        girdi[satir][sutun] = num

                        if cozum(girdi):
                            return True

                        girdi[satir][sutun] = 0

                return False

    return True

# sudokuyu yazdiran fonksiyon
def print_(girdi):
    for satir in girdi:
        print(" ".join(str(num) for num in satir))


# ornek
sudoku = [
    [0, 8, 0, 0, 6, 0, 0, 0, 0],
    [0, 5, 0, 7, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 8, 6, 3, 9],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 7, 8, 0, 0, 0, 3, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 9, 5],
    [3, 9, 0, 0, 4, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 4, 1, 5, 0, 0, 0, 0]
]

if cozum(sudoku):
    print("Çözüm:")
    print_(sudoku)
else:
    print("Çözüm yok!")
