# wavelet-denoising
在信号处理中，小波去噪是很常见的方式，在此基于Python3、PyWavelets实现了一些小波去噪的方法以便直接使用
1. 阈值收缩去噪法(Threshold shrinkage denoising)、小波平移不变消噪(Wavelet translation invariant denoising)，同时实现了获取近似基线的函数；
2. 可选择阈值函数('soft', 'hard', 'garotte', 'greater', 'less')、阈值选择方法('visushrink', 'sureshrink', 'heursure', 'minmax')，以及自行选择PyWavelets中的小波和分解层数；
3. 输入序列可为list或numpy.ndarray
