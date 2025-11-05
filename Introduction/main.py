import numpy as np

temperature = [32.5, 31.6, 38.0, 60.5]

# totalTemperture = 0;

# for temp in temperature:
#     totalTemperture += temp

# averageTemperture = totalTemperture / len(temperature)

# print(averageTemperture)

totalTemperture = np.array(temperature).mean()
print(totalTemperture)
print(np.__version__)