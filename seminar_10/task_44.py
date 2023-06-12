import random
import pandas as pd
import numpy as np

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})
data.head()
OneHotData = pd.DataFrame()
Cols = set(lst)
for value in Cols:
    OneHotData[value] = np.where(data["whoAmI"] == value, 1, 0)
print(OneHotData)
