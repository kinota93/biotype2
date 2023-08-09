# 時系列データにおけるピーク信号検出

## 平滑化の係数表

## １階微分の５点以降の係数の求め方

## Savitzky-Golay アルゴリズム
## 堅牢なピーク検出アルゴリズム（Zスコアを使用）[[cf.](https://stackoverflow.com/questions/22583391/peak-signal-detection-in-realtime-timeseries-data/43512887#43512887)]

## Persistent Topology for Peak Detection [[cf.](https://www.sthu.org/blog/13-perstopology-peakdetection/index.html)] 
- scipy.signal.find_peaks [[cf.](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html)]
- ***scipy.signal.find_peaks(x, height=None, threshold=None, distance=None, prominence=None, width=None,wlen=None, rel_height=0.5, plateau_size=None)***[[src](https://github.com/scipy/scipy/blob/v1.9.3/scipy/signal/_peak_finding.py#L723-L1003)]
  The function `scipy.signal.find_peaks`, as its name suggests, is useful for this. But it's important to understand well its parameters width, threshold, distance and **above all prominence** to get a good peak extraction [[cf.](https://stackoverflow.com/questions/1713335/peak-finding-algorithm-for-python-scipy)]. The concept of **prominence** is "the useful concept" to keep the good peaks, and discard the noisy peaks. The idea is: *The higher the prominence, the more "important" the peak is*.
- What is [(topographic) prominence?](https://en.wikipedia.org/wiki/Topographic_prominence) It is "the minimum height necessary to descend to get from the summit to any higher terrain", as it can be seen here:

![img](https://i.stack.imgur.com/c2xE7.png)

References:

1. [Overview of the peaks dectection algorithms available in Python]([MonsieurV/py-findpeaks: Overview of the peaks dectection algorithms available in Python (github.com)](https://github.com/MonsieurV/py-findpeaks))

2. [Comparison of public peak detection algorithms for MALDI mass spectrometry data analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2631518/)

3. 