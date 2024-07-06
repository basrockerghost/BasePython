import numpy as np

Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

Average_calorie_burnage = np.mean(Calorie_burnage)
Average_calorie_burnage = np.std(Calorie_burnage)
Average_calorie_burnage = np.max(Calorie_burnage)
Average_calorie_burnage = np.min(Calorie_burnage)

print(Average_pulse_max)
print(Average_pulse_min)
print(Average_calorie_burnage)