# EMG Signal Analysis Using Python

A complete signal-processing pipeline for analysing electromyogram (EMG)
signals — from synthetic signal generation through filtering, feature
extraction, frequency-domain analysis, time-frequency analysis, and
envelope/phase extraction via the Hilbert transform.

Built as a **Signals and Systems (BECE202L)** mini project at the School of
Electronics Engineering (SENSE), VIT Chennai.

> EMG signals measure the electrical activity of muscles and are widely used
> in diagnosing neuromuscular disorders, monitoring muscle fatigue, and
> driving prosthetic/robotic control systems. This repo implements and
> documents a full processing pipeline that turns a noisy raw signal into
> clinically interpretable features.

---

## Table of Contents

- [Overview](#overview)
- [Pipeline](#pipeline)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [Applications](#applications)
- [Future Work](#future-work)
- [References](#references)
- [Authors](#authors)

---

## Overview

Analysing real EMG signals is difficult because they are noisy, irregular,
and affected by variables like electrode placement and skin conductivity.
This project builds a synthetic EMG signal (to keep the pipeline
self-contained and reproducible) and runs it through a processing chain that
mirrors how real EMG data would be handled:

1. **Signal generation** — synthetic EMG built from two sinusoids (100 Hz,
   150 Hz) plus Gaussian noise.
2. **Filtering** — 4th-order Butterworth bandpass (20–250 Hz) to isolate the
   physiological EMG frequency range.
3. **Rectification & smoothing** — absolute value, then moving-average / RMS
   smoothing to reveal the activation envelope.
4. **Time-domain feature extraction** — MAV, RMS, Zero Crossings (ZC), Slope
   Sign Changes (SSC).
5. **Frequency-domain analysis** — FFT, Power Spectral Density, Mean
   Frequency (MNF), Median Frequency (MDF).
6. **Time-frequency analysis** — Short-Time Fourier Transform (STFT) /
   spectrogram.
7. **Hilbert transform** — amplitude envelope and instantaneous frequency.

## Pipeline

```
Generate EMG Signal
        │
        ▼
  Bandpass Filtering  (20–250 Hz Butterworth)
        │
        ▼
    Rectification       (|signal|)
        │
        ▼
      Smoothing          (Moving Average / RMS)
        │
        ▼
  Feature Extraction     (MAV, RMS, ZC, SSC)
        │
        ▼
Time-Domain Analysis (FFT)
        │
        ▼
Frequency-Domain Analysis (STFT)
        │
        ▼
Hilbert Transform Analysis (Envelope, Instantaneous Frequency)
        │
        ▼
   Graph Visualization
```

## Repository Structure

```
emg-signal-analysis/
├── src/
│   └── emg_analysis.py      # Full pipeline, organized into reusable functions
├── docs/
│   └── abstract.md          # Project abstract
├── results/                 # Generated plots 
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

```bash
git clone https://github.com/<your-username>/emg-signal-analysis.git
cd emg-signal-analysis
pip install -r requirements.txt
```

### Dependencies

| Library      | Version  | Purpose                                                     |
|--------------|----------|---------------------------------------------------------------|
| NumPy        | ≥1.19    | Array operations, synthetic signal generation                 |
| SciPy        | ≥1.5     | Filtering (`butter`, `filtfilt`), STFT, Hilbert transform      |
| Matplotlib   | ≥3.3     | Time-domain, frequency-domain, and spectrogram visualization  |

## Usage

Run the full pipeline (prints extracted features to the console and displays
the plots):

```bash
python src/emg_analysis.py
```

Or import individual stages into your own analysis:

```python
from src.emg_analysis import (
    generate_emg_signal,
    butter_bandpass_filter,
    rectify,
    rms_smooth,
    extract_time_domain_features,
    fft_analysis,
    stft_analysis,
    hilbert_analysis,
)

fs = 1000
t, emg_signal = generate_emg_signal(fs=fs, duration=1.0)
filtered = butter_bandpass_filter(emg_signal, 20, 250, fs)
rectified = rectify(filtered)

features = extract_time_domain_features(rectified, filtered)
print(features)
```

To save figures to disk instead of displaying them interactively, call
`plot_all(..., save_dir="results")`.

## Methodology

| Stage | Technique | Purpose |
|---|---|---|
| Signal generation | Sinusoids (100 Hz, 150 Hz) + Gaussian noise | Simulate real muscle activity for a reproducible pipeline |
| Filtering | 4th-order Butterworth bandpass (20–250 Hz), zero-phase (`filtfilt`) | Remove baseline drift and high-frequency noise while retaining EMG-relevant frequencies |
| Rectification | Absolute value | Convert to non-negative amplitude representation |
| Smoothing | Moving average and RMS over a sliding window | Reveal the activation envelope / trend |
| Feature extraction | MAV, RMS, ZC, SSC | Quantify activation intensity, power, and rate of change |
| Frequency analysis | FFT, PSD, MNF, MDF | Identify dominant frequencies; MNF/MDF shifts indicate fatigue |
| Time-frequency analysis | STFT (Hanning window, spectrogram) | Track how frequency content evolves over time |
| Envelope/phase | Hilbert transform → amplitude envelope, instantaneous frequency | Real-time-style tracking of activation strength and frequency shifts |

## Results

Example output from a single run (synthetic signal, `fs = 1000 Hz`, 1 second
of data, `seed = 0`):

| Feature | Value |
|---|---|
| Mean Absolute Value (MAV) | 0.3469 |
| Root Mean Square (RMS) | 0.4121 |
| Zero Crossings (ZC) | 206 |
| Slope Sign Changes (SSC) | 254 |
| Mean Frequency, MNF (FFT) | 112.41 Hz |
| Median Frequency, MDF (FFT) | 100.00 Hz |
| Mean Frequency (STFT) | 206.58 Hz |
| Average Amplitude Envelope | 0.5449 |
| Mean Instantaneous Frequency | 100.14 Hz |

These values fall within the expected ranges for healthy, moderately active
muscle (no signs of fatigue, spasticity, or atrophy), validating that the
pipeline reproduces theoretically expected EMG behaviour. Exact numbers will
vary slightly with the random seed / signal parameters.

The pipeline produces four figure sets:

1. Raw / filtered+smoothed / rectified EMG signal (time domain)
2. Time-domain vs. frequency-domain (FFT) comparison
3. Spectrogram (STFT) showing frequency content over time
4. Amplitude envelope and instantaneous frequency (Hilbert transform)

See `docs/abstract.md` for the full project abstract and the original report
for detailed plots and clinical interpretation of each feature (muscle
fatigue, tremor/spasticity indicators, neuromuscular disease patterns, etc.).

## Applications

- **Medical diagnostics & rehabilitation** — neuromuscular disorder
  diagnosis (e.g., ALS, muscular dystrophy), prosthetic control, physical
  therapy progress tracking.
- **Human-machine interfaces** — gesture-based wearables, exoskeleton
  control.
- **Sports science** — fatigue monitoring and injury-risk prediction.
- **Robotics/AI** — EMG-driven robotic control and movement-pattern
  learning.

## Future Work

- Real-time processing on embedded/wearable hardware with live feedback.
- Machine learning for muscle fatigue classification and pattern
  recognition.
- Wavelet transform / Empirical Mode Decomposition for higher-resolution
  time-frequency analysis.
- Multi-modal biosignal fusion (EMG + ECG + EEG).
- Artifact reduction, adaptive/nonlinear filtering, and electrode
  optimization for real acquisition hardware.

## References

1. De Luca, C. J. (2002). *Surface electromyography: Detection and recording.* DelSys Incorporated.
2. Farina, D., Merletti, R., & Enoka, R. M. (2004). The extraction of neural strategies from the surface EMG. *Journal of Applied Physiology, 96*(4), 1486–1495.
3. Reaz, M. B. I., Hussain, M. S., & Mohd-Yasin, F. (2006). Techniques of EMG signal analysis: Detection, processing, classification, and applications. *Biological Procedures Online, 8*(1), 11–35.
4. Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-Time Signal Processing* (3rd ed.). Pearson.
5. Haykin, S. (2001). *Signals and Systems* (2nd ed.). Wiley.
6. Merletti, R., & Parker, P. A. (2004). *Electromyography: Physiology, Engineering, and Non-Invasive Applications.* Wiley-IEEE Press.
7. Phinyomark, A., Phukpattaranont, P., & Limsakul, C. (2012). Feature reduction and selection for EMG signal classification. *Expert Systems with Applications, 39*(8), 7420–7431.
8. McGill, K. C., & Dorfman, L. J. (1984). High-resolution alignment of sampled waveforms using the Hilbert transform. *IEEE Transactions on Biomedical Engineering, BME-31*(6), 533–537.
9. Shannon, C. E. (1948). A mathematical theory of communication. *The Bell System Technical Journal, 27*(3), 379–423.
10. Campanini, I., Merlo, A., & Degola, P. (2007). Assessment of EMG signal processing techniques in clinical gait analysis. *Gait & Posture, 25*(1), 11–22.
11. Merletti, E., Botter, A., Cescon, C., Minetto, M. A., & Vieira, T. M. (2010). A systematic review of surface electromyography analyses in computer vision applications. *Medical Engineering & Physics, 32*(3), 237–247.
12. Farina, D., & Mesin, L. (2014). Advances in surface electromyography for muscle–computer interface: Experimental perspective and clinical applications. *IEEE Reviews in Biomedical Engineering, 7*, 164–176.

## Authors

- R. Gopikasree (23BEC1013)
- S. Kirthana (23BEC1412)
- Harshitha Senthilkumar (23BEC1428)

School of Electronics Engineering (SENSE), VIT Chennai — BECE202L Signals and Systems
