import pandas as pd
import numpy as np


chat_id = 635124229 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
   logs = np.log(x-39)
   return np.mean(logs) # Ваш ответ
