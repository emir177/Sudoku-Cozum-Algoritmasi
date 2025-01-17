# Sudoku-Cozum-Algoritmasi
Projenin amacı girilen 9x9 luk sudokuyu saniyeler içerisinde çözmektir.

İlk olarak ```def(kontrol)``` tanımladım ve bu fonksiyon ile satır sütun ve 3x3 lük karelerde tekrar eden sayı var mı bunu kontrol ettim.

Daha sonrasında backtracking dediğimiz algoritmayı kullandığım ```def(cozum)``` boş hücreleri tespit edip (0) o hücreleri 1 den 9 a kadar sayılarla doldurmasını sağladım.

Ancak seçilen sayı o durumda doğru sayı olsa bile sudoku çözümü yaptığım için ilerleyen çözümlerde geçerli olmayabiliyor. Bu durumda sayı tekrar seçiliyor.

En son kısımda ise sudokuyu yazdıran kısmı yazdım.

