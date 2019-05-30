import numpy as np
import matplotlib.pyplot as plt
from utils.denoising import get_baseline, thresholding, TI

# you can test functions here
if __name__ == "__main__":
    ecg = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    disnoise = TI(ecg, method='heursure', mode='soft', wavelets_name='sym5', level=1)
    print(disnoise)
    baseline = get_baseline(data=ecg, wavelets_name="sym5", level=1)
    print(baseline)
