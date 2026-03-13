from sklearn import datasets
import pandas as pd

data = datasets.fetch_california_housing()

df = pd.DataFrame(data.data, columns = data.feature_names, index = [f"sample_{i}" for i in range(data.data.shape[0])])
print(df.head())