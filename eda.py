import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set()

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

df_train = pd.read_csv("train.csv")   # if in same folder
df_test = pd.read_csv("test.csv")

print(df_train.shape)
print(df_train.head())