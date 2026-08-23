# EMG Signal Analysis Using Python

<p align="center">

**Biomedical Signal Processing | EMG Analysis | Python | DSP | Feature Extraction**

</p>

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Biomedical%20Signal%20Processing-blue" alt="Biomedical Signal Processing">
  <img src="https://img.shields.io/badge/Language-Python-orange" alt="Python">
  <img src="https://img.shields.io/badge/Signal-EMG-green" alt="EMG">
  <img src="https://img.shields.io/badge/DSP-Signal%20Processing-purple" alt="DSP">
  <img src="https://img.shields.io/badge/Analysis-Time%20%26%20Frequency%20Domain-red" alt="Analysis">
</p>

---

## 📌 Overview

This project presents a complete **Electromyography (EMG) signal-processing pipeline** implemented in Python, covering the processing of an EMG signal from **synthetic signal generation to filtering, feature extraction, frequency-domain analysis, time-frequency analysis, and Hilbert-transform-based analysis**.

The project demonstrates a structured Digital Signal Processing workflow for converting a noisy EMG signal into meaningful features that can be used to study **muscle activation, frequency characteristics, fatigue-related changes, and physiological behaviour**.

The pipeline includes:

* Synthetic EMG signal generation
* Bandpass filtering
* Signal rectification
* Moving-average and RMS smoothing
* Time-domain feature extraction
* FFT and frequency-domain analysis
* Power Spectral Density analysis
* Mean Frequency and Median Frequency
* Short-Time Fourier Transform (STFT)
* Spectrogram generation
* Hilbert transform
* Amplitude envelope extraction
* Instantaneous frequency estimation
* Visualization of processed EMG signals

The project was developed as a **Signals and Systems (BECE202L) mini project at VIT Chennai**.

---

# 💪 About EMG

**Electromyography (EMG)** is a technique used to measure the electrical activity produced by skeletal muscles.

EMG signals are commonly used in:

* Neuromuscular disorder analysis
* Muscle fatigue monitoring
* Rehabilitation
* Prosthetic control
* Human-machine interfaces
* Gesture recognition
* Sports science
* Robotics and assistive technologies

However, EMG signals are inherently noisy and can be affected by factors such as electrode placement, skin conductivity, motion artifacts, and external interference.

Therefore, appropriate signal-processing techniques are required to extract meaningful information from the raw signal.

---

# 🎯 Project Objectives

The primary objectives of this project are:

1. Generate a reproducible synthetic EMG signal.
2. Introduce Gaussian noise to simulate realistic signal conditions.
3. Remove unwanted frequency components using bandpass filtering.
4. Rectify and smooth the EMG signal to obtain its activation envelope.
5. Extract meaningful time-domain features.
6. Analyze the signal in the frequency domain using FFT and PSD.
7. Calculate Mean Frequency and Median Frequency.
8. Analyze changing frequency characteristics using STFT.
9. Extract amplitude envelope and instantaneous frequency using the Hilbert transform.
10. Visualize the complete signal-processing pipeline.
11. Build a reusable Python-based framework for EMG signal analysis.

---

# 🏗️ Signal Processing Pipeline

The complete processing chain is:

```text
                 Synthetic EMG Signal
                         │
                         ▼
              ┌─────────────────────┐
              │   Signal Generation │
              │ 100 Hz + 150 Hz +   │
              │ Gaussian Noise      │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Bandpass Filter   │
              │   20 – 250 Hz       │
              │ Butterworth Filter  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │     Rectification   │
              │       |signal|      │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │      Smoothing      │
              │ Moving Average /    │
              │ RMS Smoothing       │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Feature Extraction  │
              │ MAV / RMS / ZC /    │
              │ SSC                 │
              └──────────┬──────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Time-Domain             Frequency-Domain
         Analysis                 Analysis
              │                     │
              ▼                     ▼
            FFT                    PSD
              │                     │
              ▼                     ▼
          MNF / MDF             Frequency
                                Components
              │
              ▼
        ┌───────────────┐
        │      STFT     │
        │  Spectrogram  │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │ Hilbert       │
        │ Transform     │
        └───────┬───────┘
                │
          ┌─────┴─────┐
          ▼           ▼
      Amplitude    Instantaneous
       Envelope     Frequency
          │           │
          └─────┬─────┘
                ▼
        Graph Visualization
```

The repository implements this complete pipeline from signal generation through final visualization.

---

# 🧩 Signal Generation

To keep the project **self-contained and reproducible**, the EMG signal is synthetically generated rather than relying on external hardware or datasets.

The generated signal consists of:

* A 100 Hz sinusoidal component
* A 150 Hz sinusoidal component
* Gaussian noise

The default configuration uses:

```text
Sampling Frequency = 1000 Hz
Signal Duration    = 1 second
```

This provides a controlled signal on which the complete DSP pipeline can be demonstrated and evaluated.

---

# 🛠️ Tools & Technologies

## Python

Python is used as the primary implementation language because of its extensive scientific-computing and signal-processing ecosystem.

---

## NumPy

**NumPy** is used for:

* Numerical operations
* Array manipulation
* Signal generation
* Mathematical calculations

---

## SciPy

**SciPy** provides the core signal-processing functionality, including:

* Butterworth filter design
* Zero-phase filtering
* STFT
* Hilbert transform
* Signal-processing operations

---

## Matplotlib

**Matplotlib** is used for:

* Time-domain plots
* Frequency-domain plots
* Spectrograms
* EMG envelopes
* Instantaneous-frequency visualization

The repository specifies NumPy, SciPy and Matplotlib as its primary dependencies.

---

# ⚙️ Processing Stages

## 1️⃣ Signal Generation

A synthetic EMG waveform is generated using sinusoidal components and Gaussian noise.

```text
100 Hz sinusoid
       +
150 Hz sinusoid
       +
Gaussian Noise
       ↓
Synthetic EMG Signal
```

This creates a reproducible input for the processing pipeline.

---

# 2️⃣ Bandpass Filtering

A **4th-order Butterworth bandpass filter** is applied between:

```text
Low Cutoff  = 20 Hz
High Cutoff = 250 Hz
```

The filtering stage removes unwanted low-frequency baseline variations and high-frequency noise while retaining the selected EMG frequency range.

Zero-phase filtering using `filtfilt` is used to avoid introducing phase distortion.

---

# 3️⃣ Rectification

After filtering, the signal is rectified using:

```text
Rectified Signal = |EMG Signal|
```

Rectification converts the bipolar EMG waveform into a non-negative representation, making the overall muscle activation level easier to analyze.

---

# 4️⃣ Smoothing

The rectified signal is smoothed using:

* Moving-average smoothing
* RMS-based smoothing

Smoothing reduces rapid fluctuations and reveals the underlying **EMG activation envelope**.

---

# 5️⃣ Time-Domain Feature Extraction

Several commonly used EMG features are extracted.

| Feature | Meaning             |
| ------- | ------------------- |
| **MAV** | Mean Absolute Value |
| **RMS** | Root Mean Square    |
| **ZC**  | Zero Crossings      |
| **SSC** | Slope Sign Changes  |

These features quantify characteristics such as signal amplitude, activation intensity, and waveform variation.

---

## Mean Absolute Value — MAV

MAV represents the average absolute amplitude of the EMG signal.

It provides an indication of the overall muscle activation level.

---

## Root Mean Square — RMS

RMS measures the effective magnitude of the EMG waveform and is commonly used as an indicator of muscle activation intensity.

---

## Zero Crossings — ZC

Zero Crossings count how frequently the signal crosses the zero-amplitude level.

This provides information about the frequency characteristics of the EMG waveform.

---

## Slope Sign Changes — SSC

Slope Sign Changes measure changes in the direction of the signal slope and provide additional information about waveform complexity.

---

# 6️⃣ Frequency-Domain Analysis

The EMG signal is transformed into the frequency domain using the **Fast Fourier Transform (FFT)**.

```text
Time Domain
     │
     ▼
    FFT
     │
     ▼
Frequency Domain
```

FFT analysis helps identify the frequency components contained within the EMG signal.

---

# 7️⃣ Power Spectral Density

Power Spectral Density (PSD) is used to examine how signal power is distributed across different frequencies.

This allows the frequency characteristics of the muscle activity to be studied more effectively.

---

# 8️⃣ Mean Frequency & Median Frequency

Two important frequency-domain features are calculated:

### Mean Frequency — MNF

MNF represents the weighted average frequency of the EMG power spectrum.

### Median Frequency — MDF

MDF is the frequency that divides the total power spectrum into two equal halves.

Changes in MNF and MDF can be used as indicators when studying **muscle fatigue**.

---

# 9️⃣ Short-Time Fourier Transform — STFT

Traditional FFT provides frequency information for the overall signal.

However, EMG signals can vary over time.

Therefore, **Short-Time Fourier Transform (STFT)** is used to observe how the frequency content changes throughout the signal.

The STFT output is visualized using a **spectrogram**.

```text
EMG Signal
    │
    ▼
STFT
    │
    ▼
Frequency vs Time
    │
    ▼
Spectrogram
```

This provides a time-frequency representation of the EMG activity.

---

# 🔟 Hilbert Transform

The Hilbert transform is used to obtain the analytic representation of the EMG signal.

From this representation, the project extracts:

* Amplitude envelope
* Instantaneous frequency

The amplitude envelope provides an estimate of changing signal strength, while instantaneous frequency provides information about frequency variation over time.

---

# 📊 Project Results

For the default synthetic signal configuration (`fs = 1000 Hz`, duration = 1 second, seed = 0), the repository reports:

| Feature                      |         Value |
| ---------------------------- | ------------: |
| Mean Absolute Value (MAV)    |    **0.3469** |
| Root Mean Square (RMS)       |    **0.4121** |
| Zero Crossings (ZC)          |       **206** |
| Slope Sign Changes (SSC)     |       **254** |
| Mean Frequency (MNF)         | **112.41 Hz** |
| Median Frequency (MDF)       | **100.00 Hz** |
| Mean Frequency — STFT        | **206.58 Hz** |
| Average Amplitude Envelope   |    **0.5449** |
| Mean Instantaneous Frequency | **100.14 Hz** |

These are example results from one synthetic-signal run, so exact values can vary with the random seed and signal parameters.

---

# 📈 Visualizations

The project generates four major sets of visualizations:

### 1. EMG Time-Domain Analysis

Displays:

* Raw EMG
* Filtered EMG
* Rectified EMG
* Smoothed EMG

### 2. FFT Analysis

Compares the signal in:

* Time domain
* Frequency domain

### 3. STFT / Spectrogram

Shows the evolution of frequency components over time.

### 4. Hilbert Transform

Displays:

* Amplitude envelope
* Instantaneous frequency

These visualizations make it possible to observe the effect of each stage of the signal-processing pipeline.

---

# 📁 Project Structure

```text
EMG-signal-analysis-using-PYTHON/
│
├── src/
│   └── emg_analysis.py
│
├── docs/
│   └── abstract.md
│
├── results/
│   └── generated plots
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

The main processing pipeline is organized into reusable functions inside `emg_analysis.py`.

---

# 🧰 Installation & Environment

## Requirements

```text
Python 3.7+
pip
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

The repository uses:

```text
NumPy
SciPy
Matplotlib
```

for numerical computation, signal processing, and visualization.

---

# ▶️ Running the Project

Run the complete pipeline using:

```bash
python src/emg_analysis.py
```

The program processes the synthetic EMG signal, calculates the extracted features, and generates the corresponding visualizations.

Individual processing functions can also be imported and used independently:

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
```

The repository is structured so that individual stages can be reused in other EMG analysis applications.

---

# 🔍 Analysis Strategy

The project analyzes the EMG signal at multiple levels.

### Time Domain

Examines:

* Signal amplitude
* RMS
* MAV
* Zero crossings
* Slope sign changes

### Frequency Domain

Examines:

* FFT
* PSD
* MNF
* MDF

### Time-Frequency Domain

Examines:

* STFT
* Spectrogram
* Frequency variation over time

### Analytic Signal Domain

Uses the Hilbert transform to extract:

* Amplitude envelope
* Instantaneous frequency

This multi-domain approach provides a more complete understanding of the EMG signal.

---

# 🧠 Key Concepts Demonstrated

This project provides practical exposure to:

* Biomedical signal processing
* Electromyography
* Digital signal processing
* Synthetic signal generation
* Gaussian noise modelling
* Butterworth filtering
* Zero-phase filtering
* Signal rectification
* Moving-average smoothing
* RMS analysis
* Time-domain feature extraction
* FFT
* Power Spectral Density
* Mean Frequency
* Median Frequency
* STFT
* Spectrogram analysis
* Hilbert transform
* Amplitude envelope extraction
* Instantaneous frequency estimation
* Scientific visualization using Python

---

# 💡 What I Learned

This project demonstrates how a seemingly noisy physiological signal can be transformed into meaningful information through a sequence of DSP operations.

The complete processing chain can be summarized as:

```text
Noisy EMG Signal
       ↓
    Filtering
       ↓
  Rectification
       ↓
    Smoothing
       ↓
Feature Extraction
       ↓
 ┌─────┼──────────┐
 ▼     ▼          ▼
FFT   STFT    Hilbert Transform
 │     │          │
 ▼     ▼          ▼
Freq. Spectrogram Envelope
Analysis          + Frequency
       │
       ▼
Meaningful EMG Features
```

The project highlights the importance of analyzing physiological signals across **time, frequency, and time-frequency domains** rather than relying on a single representation.

---

# 🏥 Applications

The processing techniques demonstrated in this project can be extended to several real-world applications.

### Medical & Rehabilitation

* Neuromuscular disorder analysis
* Rehabilitation monitoring
* Muscle activity assessment
* Prosthetic control

### Human-Machine Interfaces

* Gesture recognition
* Wearable interfaces
* Exoskeleton control
* EMG-based interaction

### Sports Science

* Muscle fatigue monitoring
* Performance analysis
* Injury-risk assessment

### Robotics & AI

* EMG-driven robotic systems
* Movement-pattern recognition
* Intelligent assistive systems

These applications are also identified in the project's original repository documentation.

---

# 🚀 Future Work

The current synthetic-signal pipeline can be extended toward real-world EMG applications.

Potential improvements include:

* Real-time EMG processing on embedded/wearable hardware
* Live muscle-activity feedback
* Machine-learning-based fatigue classification
* EMG pattern recognition
* Wavelet-transform-based analysis
* Empirical Mode Decomposition (EMD)
* Multi-channel EMG analysis
* EMG + ECG + EEG signal fusion
* Adaptive and nonlinear filtering
* Motion-artifact reduction
* Real electrode-based signal acquisition

These directions align with the future-work areas documented in the repository.

---

# 📚 References

* Digital Signal Processing concepts
* Signals and Systems coursework
* SciPy signal-processing framework
* NumPy numerical-computing framework
* Matplotlib visualization framework
* EMG signal-processing literature

---

# ⭐ Project Highlights

* 🔹 Complete **EMG signal-processing pipeline**
* 🔹 Synthetic EMG generation
* 🔹 **20–250 Hz Butterworth bandpass filtering**
* 🔹 Signal rectification and smoothing
* 🔹 **MAV, RMS, ZC and SSC** feature extraction
* 🔹 FFT and frequency-domain analysis
* 🔹 Power Spectral Density analysis
* 🔹 **MNF and MDF** calculation
* 🔹 STFT and spectrogram analysis
* 🔹 Hilbert transform analysis
* 🔹 Amplitude envelope extraction
* 🔹 Instantaneous frequency estimation
* 🔹 Python-based reusable implementation
* 🔹 Visualization of multiple signal representations

---

# 📌 Keywords

`EMG` `Electromyography` `Biomedical Signal Processing` `Digital Signal Processing` `Python` `NumPy` `SciPy` `Matplotlib` `Butterworth Filter` `FFT` `PSD` `STFT` `Spectrogram` `Hilbert Transform` `Feature Extraction` `MAV` `RMS` `Zero Crossing` `Slope Sign Changes` `MNF` `MDF` `Muscle Fatigue` `Signal Analysis`

---

<p align="center">

**Raw Signal → Filtering → Features → FFT → STFT → Hilbert Analysis → EMG Insights**

</p>
