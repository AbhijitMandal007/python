# develope python program to compute statistical measueres using numpy

import numpy as np
# Given Data
marks = np.array([78,85,92,67,88,73,95,81,76,89])
temperature = np.array([28.5,30.2,29.8,31.4,27.9,32.1,30.5])
sales = np.array([12500,13800,14200,11900,15100,14750,16000])

# function for statistic
def statistic(name,data):
    print("\n",name)
    print("Data:",data)
    print("Mean:",np.mean(data))
    print("Median:",np.median(data))
    print("Standard_deviation:",round(np.std(data),2))
    print("Maximum:",np.max(data))
    print("Minimum:",np.min(data))

# Display function
statistic("marks",marks)
statistic("temperature",temperature)
statistic("sales",sales)