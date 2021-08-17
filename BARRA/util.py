import pandas as pd
import numpy as np
import scipy.optimize as sc_opt


# 计算半衰期系数
def halflife(half_life = 63, length = 252):
    t = np.arange(length)
    w = 2 **(t/half_life) / sum(2 ** (t/half_life))
    return(w)

