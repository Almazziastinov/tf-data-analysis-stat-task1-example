import pandas as pd
import numpy as np


chat_id = 635124229 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x_39 = x - 39 
    cur_sum = 0 
    for i in range(len(x)):
        cur_sum+=np.log(abs(x_39[i]))
    mean_ = cur_sum / len(x)
    return mean_ # Ваш ответ
