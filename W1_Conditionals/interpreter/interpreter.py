expression = input("Expression: ").strip() # takes out the spaces

x, y, z = expression.split() # splits up the equation into parts

x, z, = int(x), int(z) # makes x and z integers

match y:   # assigns operator value to y
    case "+": result = x + z
    case "-": result = x - z
    case "*": result = x * z
    case "/": result = x / z
    case _:   print("Invalid operator")

print(f"{float(result):.1f}")  # ensures just 1 decimal place 3 is "3.0"
