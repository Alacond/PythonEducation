petya = int(input())
vasya = int(input())
tolya = int(input())

if tolya < petya > vasya:
    if vasya > tolya:
        first = "Петя"
        second = "Вася"
        third = "Толя"
    else:
        first = "Петя"
        second = "Толя"
        third = "Вася"
elif tolya < vasya > petya:
    if petya > tolya:
        first = "Вася"
        second = "Петя"
        third = "Толя"
    else:
        first = "Вася"
        second = "Толя"
        third = "Петя"
elif vasya < tolya > petya:
    if petya > vasya:
        first = "Толя"
        second = "Петя"
        third = "Вася"
    else:
        first = "Толя"
        second = "Вася"
        third = "Петя"

print(f"{first:>14}")
print(f"{second:>6}")
print(f"{third:>22}")
print((f"   II      I      III"))