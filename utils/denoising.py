import pywt
import math
import numpy as np
import matplotlib.pylab as plt


# 获取近似基线
def get_baseline(data, wavelets_name='sym8', level=5):
    '''

    :param data: signal
    :param wavelets_name: wavelets name in PyWavelets, 'sym8' as default
    :param level: deconstruct level, 5 as default
    :return: baseline signal
    '''
    # 创建小波对象
    wave = pywt.Wavelet(wavelets_name)
    # 分解
    coeffs = pywt.wavedec(data, wave, level=level)
    # 除最高频外小波系数置零
    for i in range(1, len(coeffs)):
        coeffs[i] *= 0
    # 重构
    baseline = pywt.waverec(coeffs, wave)
    return baseline


# 阈值收缩去噪法
def thresholding(data, method='sureshrink', mode='soft', wavelets_name='sym8', level=5):
    '''

    :param data: signal
    :param method: {'visushrink', 'sureshrink', 'heursure', 'minmax'}, 'sureshrink' as default
    :param mode: {'soft', 'hard', 'garotte', 'greater', 'less'}, 'soft' as default
    :param wavelets_name: wavelets name in PyWavelets, 'sym8' as default
    :param level: deconstruct level, 5 as default
    :return: processed data
    '''
    methods_dict = {'visushrink': VisuShrink, 'sureshrink': SureShrink, 'heursure': HeurSure, 'minmax': Minmax}
    # 创建小波对象
    wave = pywt.Wavelet(wavelets_name)

    # 分解 阈值处理
    data_ = data[:]

    (cA, cD) = pywt.dwt(data=data_, wavelet=wave)
    var = get_var(cD)

    coeffs = pywt.wavedec(data=data, wavelet=wavelets_name, level=level)

    for idx, coeff in enumerate(coeffs):
        if idx == 0:
            continue
        # 求阈值thre
        thre = methods_dict[method](var, coeff)
        # 处理cD
        coeffs[idx] = pywt.threshold(coeffs[idx], thre, mode=mode)

    # 重构信号
    thresholded_data = pywt.waverec(coeffs, wavelet=wavelets_name)

    return thresholded_data


# 小波平移不变消噪
def TI(data, step=100, method='heursure', mode='soft', wavelets_name='sym5', level=5):
    '''

    :param data: signal
    :param step: shift step, 100 as default
    :param method: {'visushrink', 'sureshrink', 'heursure', 'minmax'}, 'heursure' as default
    :param mode: {'soft', 'hard', 'garotte', 'greater', 'less'}, 'soft' as default
    :param wavelets_name: wavelets name in PyWavelets, 'sym5' as default
    :param level: deconstruct level, 5 as default
    :return: processed data
    '''
    # 循环平移
    num = math.ceil(len(data)/step)
    final_data = [0]*len(data)
    for i in range(num):
        temp_data = right_shift(data, i*step)
        temp_data = thresholding(temp_data, method=method, mode=mode, wavelets_name=wavelets_name, level=level)
        temp_data = temp_data.tolist()
        temp_data = back_shift(temp_data, i*step)
        final_data = list(map(lambda x, y: x+y, final_data, temp_data))

    final_data = list(map(lambda x: x/num, final_data))

    return final_data


# 平移操作
def right_shift(data, n):
    copy1 = list(data[n:])
    copy2 = list(data[:n])
    return copy1 + copy2


# 逆平移操作
def back_shift(data, n):
    p = len(data) - n
    copy1 = list(data[p:])
    copy2 = list(data[:p])
    return copy1 + copy2


# 获取噪声方差
def get_var(cD):
    coeffs = cD
    abs_coeffs = []
    for coeff in coeffs:
        abs_coeffs.append(math.fabs(coeff))
    abs_coeffs.sort()
    pos = math.ceil(len(abs_coeffs) / 2)
    var = abs_coeffs[pos] / 0.6745
    return var


# 求SureShrink法阈值
def SureShrink(var, coeffs):
    N = len(coeffs)
    sqr_coeffs = []
    for coeff in coeffs:
        sqr_coeffs.append(math.pow(coeff, 2))
    sqr_coeffs.sort()
    pos = 0
    r = 0
    for idx, sqr_coeff in enumerate(sqr_coeffs):
        new_r = (N - 2 * (idx + 1) + (N - (idx + 1))*sqr_coeff + sum(sqr_coeffs[0:idx+1])) / N
        if r == 0 or r > new_r:
            r = new_r
            pos = idx
    thre = math.sqrt(var) * math.sqrt(sqr_coeffs[pos])
    return thre


# 求VisuShrink法阈值
def VisuShrink(var, coeffs):
    N = len(coeffs)
    thre = math.sqrt(var) * math.sqrt(2 * math.log(N))
    return thre


# 求HeurSure法阈值
def HeurSure(var, coeffs):
    N = len(coeffs)
    s = 0
    for coeff in coeffs:
        s += math.pow(coeff, 2)
    theta = (s - N) / N
    miu = math.pow(math.log2(N), 3/2) / math.pow(N, 1/2)
    if theta < miu:
        return VisuShrink(var, coeffs)
    else:
        min(VisuShrink(var, coeffs), SureShrink(var, coeffs))


# 求Minmax法阈值
def Minmax(var, coeffs):
    N = len(coeffs)
    if N > 32:
        return math.sqrt(var) * (0.3936 + 0.1829 * math.log2(N))
    else:
        return 0


if __name__ == "__main__":
    pass
