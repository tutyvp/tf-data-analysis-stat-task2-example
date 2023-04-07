import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 460411293 # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:

  alpha = 1 - p
  sum_r2 = np.sum(x*x)
  N = len(x)

  left_q = gamma.ppf(alpha/2, a=N, scale=2/N)
  right_q = gamma.ppf(1-alpha/2, a=N, scale=2/N)

return np.sqrt(sum_r2/44/N/right_q), np.sqrt(sum_r2/44/N/left_q)
