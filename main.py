import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Display first few rows
print(df.head())
