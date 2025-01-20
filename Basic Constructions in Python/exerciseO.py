varTimeHours = int(input())
varTimeMinutes = int(input())
varEstimateMinutes = int(input())

varResultMinutes = (varTimeMinutes + varEstimateMinutes) % 60
varResultHours = (varTimeHours + (varTimeMinutes + varEstimateMinutes) // 60) % 24

print(f"{varResultHours:0>2}:{varResultMinutes:0>2}")