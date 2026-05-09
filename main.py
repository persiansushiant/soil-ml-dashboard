import pandas as pd

import matplotlib.pyplot as plt
df = pd.read_csv("soil_data.csv")
soil_counts = (
    df["soil_type"]
    .value_counts()
)

plt.pie(
    soil_counts.values,
    labels=soil_counts.index,
    autopct="%1.1f%%"
)

plt.title("Soil Types")

plt.show()