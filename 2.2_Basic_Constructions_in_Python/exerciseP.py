name1 = 'Петя'
speed1 = int(input())

name2 = 'Вася'
speed2 = int(input())

name3 = 'Толя'
speed3 = int(input())

if speed1 < speed2:
    speed1, speed2 = speed2, speed1
    name1, name2 = name2, name1
if speed1 < speed3:
    speed1, speed3 = speed3, speed1
    name1, name3 = name3, name1
if speed2 < speed3:
    speed2, speed3 = speed3, speed2
    name2, name3 = name3, name2

print(f"{name1:>14}")
print(f"{name2:>6}")
print(f"{name3:>22}")
print((f"   II      I      III"))