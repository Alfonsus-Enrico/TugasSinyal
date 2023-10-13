import matplotlib.pyplot as plt
import numpy as np

def fft2D(image):
    M, N = image.shape
    F = np.zeros((M, N), dtype=complex)

    for u in range(M):
        for v in range(N):
            F[u, v] = 0
            for x in range(M):
                for y in range(N):
                    F[u, v] += image[x, y] * np.exp(-2j * np.pi * (u * x / M + v * y / N))

    return F

# Buat gambar 2D sederhana
N = 256
x = np.linspace(0, 1, N, endpoint=False)
y = np.linspace(0, 1, N, endpoint=False)
X, Y = np.meshgrid(x, y)
image = np.sin(2 * np.pi * 5 * X) * np.sin(2 * np.pi * 10 * Y)

# Hitung FFT 2D menggunakan fungsi yang diimplementasikan
fft_result = fft2D(image)

# Plot gambar asli
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Gambar Asli')

# Plot magnitude FFT
magnitude = np.abs(fft_result)
plt.subplot(1, 2, 2)
plt.imshow(np.log(magnitude + 1), cmap='viridis')
plt.title('Magnitude FFT')

plt.tight_layout()
plt.show()
