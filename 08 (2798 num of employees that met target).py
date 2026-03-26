hours = [0,1,2,3,4]
target = 2

hours_met = []
for hour in hours:
    if hour >= target:
        hours_met.append(hour)

print(len(hours_met))
print(hours_met)

# efektivnější:
"""
    count = 0
    
    for i in hours:
        if i >= target:
            count += 1
    return count
"""