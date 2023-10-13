import matplotlib.pyplot as plt
import numpy as np

# Implementasi fungsi sinc (sinc(x) = sin(pi*x) / (pi*x))
def sinc(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.where(x == 0, 1.0, np.sin(np.pi * x) / (np.pi * x))
    return result

# Implementasi FFT 1D sederhana
def fft1D(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    
    return X

# Definisi periode fungsi kotak kontinu
periods = [0.5, 1, 3]

# Generate data waktu
N = 1024
x = np.linspace(-5, 5, N, endpoint=False)

# Plot fungsi kotak kontinu dengan berbagai periode dan FFT-nya
for T in periods:
    box_signal = sinc(x / T)
    fft_result = fft1D(box_signal)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(x, box_signal)
    plt.title(f'Fungsi Kotak Kontinu (Periode {T} s)')
    
    plt.subplot(2, 1, 2)
    plt.plot(np.abs(fft_result))
    plt.title('Magnitude FFT')
    
    plt.tight_layout()
    plt.show()
