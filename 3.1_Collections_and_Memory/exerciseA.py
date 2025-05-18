count = int(input())

bool_letters = True

for _ in range(count):
    shout = str(input())
    if shout.startswith("а") or shout.startswith("б") or shout.startswith("в"):
        pass
    else:
        bool_letters = False

if bool_letters:
    print("YES")
else:
    print("NO")