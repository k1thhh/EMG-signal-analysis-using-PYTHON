"""
EMG Signal Analysis Using Python
=================================

Generates a synthetic EMG signal and runs it through a full processing
pipeline: bandpass filtering, rectification, smoothing, time-domain
feature extraction, frequency-domain analysis (FFT), time-frequency
analysis (STFT), and envelope/instantaneous-frequency extraction via
the Hilbert transform.

Pipeline:
    Generate EMG Signal -> Bandpass Filtering -> Rectification -> Smoothing
    -> Feature Extraction -> Frequency Domain Analysis (FFT)
    -> Time Domain Analysis (STFT) -> Hilbert Transform Analysis
    -> Graph Visualization

Authors: R. Gopikasree, S. Kirthana, Harshitha Senthilkumar
Course:  BECE202L - Signals and Systems, VIT Chennai
"""

import numpy as np
from scipy.signal import butter, filtfilt, stft, hilbert
import matplotlib.pyplot as plt


# --------------------------------------------------------------------------
# 1. Signal Generation
# --------------------------------------------------------------------------
def generate_emg_signal(fs=1000, duration=1.0, seed=0):
    """Generate a synthetic EMG signal composed of two sinusoids plus noise.

    emg(t) = 0.5*sin(2*pi*100*t) + 0.3*sin(2*pi*150*t) + 0.2*noise
    """
    np.random.seed(seed)
    t = np.linspace(0, duration, int(fs * duration))
    emg_signal = (
        0.5 * np.sin(2 * np.pi * 100 * t)
        + 0.2 * np.random.randn(t.size)
        + 0.3 * np.sin(2 * np.pi * 150 * t)
    )
    return t, emg_signal


# --------------------------------------------------------------------------
# 2. Filtering
# --------------------------------------------------------------------------
def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    """4th-order Butterworth bandpass filter (zero-phase via filtfilt)."""
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype="band")
    return filtfilt(b, a, data)


# --------------------------------------------------------------------------
# 3. Rectification
# --------------------------------------------------------------------------
def rectify(signal):
    """Full-wave rectification: absolute value of the signal."""
    return np.abs(signal)


# --------------------------------------------------------------------------
# 4. Smoothing
# --------------------------------------------------------------------------
def moving_average(signal, window_size=100):
    return np.convolve(signal, np.ones(window_size) / window_size, mode="same")


def rms_smooth(signal, window_size=100):
    return np.sqrt(
        np.convolve(signal ** 2, np.ones(window_size) / window_size, mode="same")
    )


# --------------------------------------------------------------------------
# 5. Time-Domain Feature Extraction
# --------------------------------------------------------------------------
def extract_time_domain_features(rectified_signal, filtered_signal):
    """Compute MAV, RMS, Zero Crossings (ZC), and Slope Sign Changes (SSC)."""
    mav = np.mean(rectified_signal)
    rms_value = np.sqrt(np.mean(rectified_signal ** 2))
    zero_crossings = ((filtered_signal[:-1] * filtered_signal[1:]) < 0).sum()
    ssc = np.sum(np.diff(np.sign(np.diff(filtered_signal))) != 0)
    return {
        "MAV": mav,
        "RMS": rms_value,
        "ZC": zero_crossings,
        "SSC": ssc,
    }


# --------------------------------------------------------------------------
# 6. Frequency-Domain Analysis (FFT)
# --------------------------------------------------------------------------
def fft_analysis(filtered_signal, fs):
    """Compute FFT magnitude, PSD, Mean Frequency (MNF), Median Frequency (MDF)."""
    n = len(filtered_signal)
    fft_values = np.fft.fft(filtered_signal)
    fft_freqs = np.fft.fftfreq(n, 1 / fs)

    # Keep only positive frequencies
    fft_values = fft_values[: n // 2]
    fft_freqs = fft_freqs[: n // 2]
    fft_magnitude = np.abs(fft_values)

    # Power Spectral Density
    psd = (1 / (fs * n)) * np.abs(fft_values) ** 2
    psd[1:] = 2 * psd[1:]

    mean_frequency = np.sum(fft_freqs * psd) / np.sum(psd)
    median_frequency = fft_freqs[
        np.argsort(psd.cumsum())[np.searchsorted(psd.cumsum(), 0.5 * psd.sum())]
    ]

    return {
        "fft_freqs": fft_freqs,
        "fft_magnitude": fft_magnitude,
        "psd": psd,
        "MNF": mean_frequency,
        "MDF": median_frequency,
    }


# --------------------------------------------------------------------------
# 7. Time-Frequency Analysis (STFT)
# --------------------------------------------------------------------------
def stft_analysis(emg_signal, fs, window="hann", nperseg=200, noverlap=100):
    """Short-Time Fourier Transform for a time-frequency (spectrogram) view."""
    frequencies, times, Zxx = stft(
        emg_signal, fs=fs, window=window, nperseg=nperseg, noverlap=noverlap
    )
    stft_magnitude = np.abs(Zxx)
    mean_frequency = np.sum(frequencies[:, None] * stft_magnitude) / np.sum(
        stft_magnitude
    )
    return {
        "frequencies": frequencies,
        "times": times,
        "stft_magnitude": stft_magnitude,
        "mean_frequency": mean_frequency,
    }


# --------------------------------------------------------------------------
# 8. Hilbert Transform (Envelope + Instantaneous Frequency)
# --------------------------------------------------------------------------
def hilbert_analysis(filtered_signal, fs):
    analytic_signal = hilbert(filtered_signal)
    amplitude_envelope = np.abs(analytic_signal)
    instantaneous_phase = np.angle(analytic_signal)
    instantaneous_frequency = np.diff(np.unwrap(instantaneous_phase)) * (
        fs / (2.0 * np.pi)
    )
    return {
        "amplitude_envelope": amplitude_envelope,
        "instantaneous_frequency": instantaneous_frequency,
        "average_amplitude": np.mean(amplitude_envelope),
        "mean_instantaneous_frequency": np.mean(instantaneous_frequency),
    }


# --------------------------------------------------------------------------
# Plotting helpers
# --------------------------------------------------------------------------
def plot_all(t, emg_signal, filtered_signal, rectified_signal, smoothed_signal_rms,
             fft_result, stft_result, hilbert_result, fs, save_dir=None):
    def _save_or_show(fig, name):
        if save_dir:
            fig.savefig(f"{save_dir}/{name}.png", dpi=150, bbox_inches="tight")
        else:
            plt.show()

    # Raw / Filtered / Rectified
    fig1 = plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, emg_signal)
    plt.title("Raw EMG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(3, 1, 2)
    plt.plot(t, filtered_signal, label="Filtered EMG Signal")
    plt.plot(t, smoothed_signal_rms, label="Smoothed (RMS)", linestyle="--")
    plt.title("Filtered and Smoothed EMG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, rectified_signal)
    plt.title("Rectified EMG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    _save_or_show(fig1, "01_raw_filtered_rectified")

    # Time domain vs Frequency domain
    fig2 = plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(t, emg_signal, label="Original EMG Signal", color="grey", alpha=0.7)
    plt.plot(t, filtered_signal, label="Filtered EMG Signal", color="blue")
    plt.title("Time-Domain EMG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(fft_result["fft_freqs"], fft_result["fft_magnitude"], color="purple")
    plt.title("Frequency-Domain (FFT) EMG Signal")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.xlim([0, 500])
    plt.tight_layout()
    _save_or_show(fig2, "02_time_vs_frequency_domain")

    # Spectrogram
    fig3 = plt.figure(figsize=(12, 8))
    plt.pcolormesh(
        stft_result["times"],
        stft_result["frequencies"],
        stft_result["stft_magnitude"],
        shading="gouraud",
        cmap="inferno",
    )
    plt.colorbar(label="Magnitude")
    plt.title("Spectrogram (STFT) of EMG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.ylim([0, 250])
    _save_or_show(fig3, "03_spectrogram")

    # Amplitude envelope + instantaneous frequency
    fig4 = plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(t, hilbert_result["amplitude_envelope"], color="red")
    plt.title("Amplitude Envelope of EMG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude Envelope")

    plt.subplot(2, 1, 2)
    plt.plot(t[:-1], hilbert_result["instantaneous_frequency"], color="purple")
    plt.title("Instantaneous Frequency of EMG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.ylim(0, 200)
    plt.tight_layout()
    _save_or_show(fig4, "04_envelope_instantaneous_frequency")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    fs = 1000  # Sampling frequency (Hz)

    # 1. Signal generation
    t, emg_signal = generate_emg_signal(fs=fs, duration=1.0, seed=0)

    # 2. Bandpass filter (20-250 Hz, typical EMG range)
    filtered_signal = butter_bandpass_filter(emg_signal, 20, 250, fs)

    # 3. Rectification
    rectified_signal = rectify(filtered_signal)

    # 4. Smoothing
    window_size = 100
    smoothed_signal_ma = moving_average(rectified_signal, window_size)
    smoothed_signal_rms = rms_smooth(rectified_signal, window_size)

    # 5. Time-domain feature extraction
    features = extract_time_domain_features(rectified_signal, filtered_signal)
    print(f"Mean Absolute Value (MAV): {features['MAV']:.4f}")
    print(f"Root Mean Square (RMS): {features['RMS']:.4f}")
    print(f"Zero Crossings (ZC): {features['ZC']}")
    print(f"Slope Sign Changes (SSC): {features['SSC']}")

    # 6. FFT / frequency-domain analysis
    fft_result = fft_analysis(filtered_signal, fs)
    print(f"Mean Frequency (MNF): {fft_result['MNF']:.4f} Hz")
    print(f"Median Frequency (MDF): {fft_result['MDF']:.4f} Hz")

    # 7. STFT / time-frequency analysis
    stft_result = stft_analysis(emg_signal, fs)
    print(f"Mean Frequency (STFT): {stft_result['mean_frequency']:.4f} Hz")

    # 8. Hilbert transform (envelope + instantaneous frequency)
    hilbert_result = hilbert_analysis(filtered_signal, fs)
    print(f"Average Amplitude of Envelope: {hilbert_result['average_amplitude']:.4f}")
    print(
        "Mean Instantaneous Frequency: "
        f"{hilbert_result['mean_instantaneous_frequency']:.4f} Hz"
    )

    # 9. Plots
    plot_all(
        t,
        emg_signal,
        filtered_signal,
        rectified_signal,
        smoothed_signal_rms,
        fft_result,
        stft_result,
        hilbert_result,
        fs,
    )


if __name__ == "__main__":
    main()
