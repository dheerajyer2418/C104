import csv
from collections import Counter
with open('HeightWeight.csv', newline = '') as f: 
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)): 
    n_num = file_data[i][1]
    new_data.append(float(n_num))
#getting the mean
n = len(new_data)
new_data.sort()
#using floor division to get the nearest whole number
#floor is shown by //
if n % 2 == 0: 
    #getting the first number
    median1 = float(new_data[n//2])
    #getting the second number
    median2 = float(new_data[n//2-1])

    #getting mean of those numebrs
    median = (median1 + median2)/2
else: 
    median = new_data[n//2]
    print(n)
print("Median is: " + str(median))
total = 0
for x in new_data:
    total += x
mean = total/n
print("mean/averages is: " + str(mean))
#calculating mode
data = Counter(new_data)
mode_data_for_range = {
    "50-60": 0, 
    "60-70": 0,
    "70-80": 0
}
for height, occurrence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurrence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurrence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurrence
mode_range, mode_occurrence = 0,0
for range, occurrence in mode_data_for_range.items():
    if occurrence > mode_occurrence: 
        mode_range, mode_occurrence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence
mode = float((mode_range[0] + mode_range[1]) / 2) 
print(f"Mode is -> {mode:2f}")


