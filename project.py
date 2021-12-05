import statistics
import math
data = [60,61,65,63,98,99,90,95,91,96]

mean = statistics.mean(data)
print(mean)



deviations = []

for i in data:
    deviation=i-mean
    deviations.append(deviation)


squared_deviations = []

for s in deviations:
    square =s*s
    squared_deviations.append(square)

variance = statistics.mean(squared_deviations)

std = math.sqrt(variance)
print(std)
print(statistics.stdev(data))