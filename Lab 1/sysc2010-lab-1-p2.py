import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

df = pd.read_csv("env_temp_humidity_clean.csv")

print(df.columns)
print("")
print(df.iloc)
print("")
print(df.dtypes)
print("")

print(df.info())
df.describe()

nc = df.select_dtypes(include= "number")
q1 = nc.quantile(0.25)
q3 = nc.quantile(0.75)
iqr = 1.5 * (q3 - q1)

mask = (nc < (q1 - iqr)) | (nc > (q3 + iqr))
out = df[mask.any(axis=1)]
print("")
print("")

print(" Outliers: \n", out)

x = df["timestamp"]
y0 = df["temperature_C"]
y1 = df["humidity_pct"]

seconds = (pd.to_datetime(x).astype("int64") // (6 * 10 ** 10))
start = seconds[0]
seconds -= start
plt.xlabel(" Time (min) ")
plt.ylabel(" Temperature (°C) ")
plt.title ("Temperature (°C) with respect to Time (min)")
plt.plot(seconds, y0)
plt.show()

plt.xlabel(" Time (min) ")
plt.ylabel(" Humidity (g/m^3) ")
plt.title("Humidity (g/m^3) with respect to Time (min)")
plt.plot(seconds, y1)
plt.show()