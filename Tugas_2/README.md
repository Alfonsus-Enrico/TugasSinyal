# Tugas 2 Sinyal: Convolution Signal Processing with Native Python

Pada penugasan ini, konvolusi diterapkan tanpa menggunakan library seperti numpy, scipy, dan lain-lain. Berikut hasil syntax yang saya buat 
<p align="center">
<img src="Tugas_2/Convolution.png" /><br>
  <b>Gambar 1.</b> Perbandingan hasil konvolusi menggunakan dan tanpa menggunakan numpy
</p>

# Penjelasan
- Pada line 4 dan 5, sinyal dan kernelnya didefinisikan
- Pada line 11, panjang dari array konvolusi didefinisikan sebagai (panjang sinyal) + (panjang kernel) - 1
- Pada line 12, didefinisikan array kosong dengan panjang sesuai pada line 11.
- Pada line 15-17, digunakan loop untuk melakukan konvolusi.

## Konvolusi
- pada array konvolusi, kernel dirotasi sebesar 180 derajat
- pada setiap pergeseran, hasil perkalian dijumlahkan
- pergeseran terjadi akibat loop yang dilakukan pada index array konvolusi

# Perbandingan
- Line 19 digunakan untuk memperlihatkan array konvolusi menggunakan python native
- LIne 20 digunakan untuk validasi array konvolusi degan menggunakan library numpy
