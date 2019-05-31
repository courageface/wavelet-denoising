# wavelet-denoising
在信号处理中，小波去噪是很常见的方式，在此基于Python3、PyWavelets实现了一些小波去噪的方法以便直接使用
1. 阈值收缩去噪法、小波平移不变消噪，同时实现了获取近似基线的函数；
2. 可选择阈值函数('soft', 'hard', 'garotte', 'greater', 'less')、阈值选择方法('visushrink', 'sureshrink', 'heursure', 'minmax')，以及自行选择PyWavelets中的小波和分解层数；
3. 输入序列可为list或numpy.ndarray

Implement some wavelets denoising methods based on Python3 and PyWavelets package
1. Including Threshold shrinkage denoising(tsd), Wavelet translation invariant denoising(ti) and method to get approximate baseline(get_baseline)
2. Support 'soft', 'hard', 'garotte', 'greater', 'less' modes and 'visushrink', 'sureshrink', 'heursure', 'minmax' methods for choosing. Besides, wavelets name and deconstruct level
3. Support list and numpy.ndarray as input

## Install wtdenoise
```sh
git clone https://github.com/courageface/wavelet-denoising.git
cd wavelet-denoising
python setup.py install
```

