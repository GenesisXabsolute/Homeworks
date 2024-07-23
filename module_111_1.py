import requests
import numpy as np
import pandas as pd

r = requests.get('https://github.com/timeline.json')
print(r.status_code)
print(r.headers)
print(r.text)

a = np.arange(4)
print('a = ', a)

b = np.arange(12).reshape(2, 6)
print('b = ', b)

c = np.ones(4)
print('c = ', c)

s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print(s)
print()
s = pd.Series(np.linspace(0, 1, 5))
print(s)
