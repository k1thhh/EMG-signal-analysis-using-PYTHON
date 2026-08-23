# Abstract

This project studies electromyographic (EMG) signals, which are important for
assessing muscle and motor neuron health based on the muscular electrical
activity during contractions. The work applies signals-and-systems concepts to
address noise, irregularity, and structural complexity in EMG signals — using
filtering, feature extraction, and transformation techniques to build a
focused EMG analysis pipeline.

Key steps included synthetic EMG signal generation, bandpass filtering to
reduce noise and isolate muscle-activity frequencies, and rectification with
RMS smoothing to highlight signal trends. Features such as Mean Absolute
Value (MAV) and Zero Crossings (ZC) were extracted to characterize muscle
activation levels and patterns. FFT and Short-Time Fourier Transform (STFT)
were used for frequency and time-frequency analysis, and the Hilbert
Transform was used to examine amplitude envelope and instantaneous
frequency/phase.

The results are consistent with theoretical expectations — effective noise
reduction, clear signal trends, and robust extracted features — confirming
that this pipeline is capable of supporting muscle fatigue monitoring, motor
control applications, and diagnostic assistance.

**Authors:** R. Gopikasree, S. Kirthana, Harshitha Senthilkumar
**Course:** BECE202L — Signals and Systems, School of Electronics Engineering (SENSE), VIT Chennai
