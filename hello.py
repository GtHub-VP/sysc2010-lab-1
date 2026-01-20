import math as mt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("Libraries Imported Successfully!")

# Create a Small Series
data = pd.Series([1, 3, 5, np.nan, 6, 8])
print(data)

# 5.1 Generating and Visualizing Synthetic Signals
t = np.arange(0, 1, 0.002)
sin = 5 * np.sin(20 * np.pi * t)
plt.plot(t, sin)
plt.title(" Task5_1.png")
plt.xlabel(" Time (s) ")
plt.ylabel(" Amplitude ")
plt.show()

# 5.2 Generating Random Noise
plt.plot(t, sin)
plt.plot(t, (0.25 * (np.random.randn(500))) + sin)
plt.title(" Task5_2.png")
plt.xlabel(" Time (s) ")
plt.ylabel(" Amplitude ")
plt.show()

# 5.3 Saving to / Reading from CSV Files
t = np.arange(0, 120, 1)
var = np.random.randn(120) - 0.5
temp = np.round(36 + var, 1)
data = {" Time (s) ": t, " Temperature (°C) ": temp}
df = pd.DataFrame(data)
df.to_csv("sensor_readings.csv")
ReWr = pd.read_csv("sensor_readings.csv")
ReWr = ReWr.iloc[41:80]
plt.plot( ReWr[" Time (s) "], ReWr[" Temperature (°C) "])
plt.xlabel(" Time (s) ")
plt.ylabel(" Temperature (°C) ")
plt.show()