user_input = input().split()
polish_stack = []

while len(user_input) > 0:
    cur_element = user_input.pop(0)
    if cur_element.isdigit():
        polish_stack.append(int(cur_element))
    else:
        match cur_element:
            case "+":
                polish_stack.append(polish_stack.pop(-2) + polish_stack.pop(-1))
            case "-":
                polish_stack.append(polish_stack.pop(-2) - polish_stack.pop(-1))
            case "*":
                polish_stack.append(polish_stack.pop(-2) * polish_stack.pop(-1))
            case "/":
                polish_stack.append(polish_stack.pop(-2) // polish_stack.pop(-1))
            case "~":
                polish_stack.append(-polish_stack.pop(-1))
            case "!":
                elem = polish_stack.pop()
                factorial = 1
                for i in range(2, elem + 1):
                    factorial *= i
                polish_stack.append(factorial)
            case "#":
                elem = polish_stack.pop(-1)
                polish_stack.extend([elem, elem])
            case "@":
                c = polish_stack.pop()
                b = polish_stack.pop()
                a = polish_stack.pop()
                polish_stack.extend([b, c, a])

print(polish_stack[0])

# Вот только стоило сказать, что я поверил в людей из яндекса, что они не будут усложнять... И они усложнили.