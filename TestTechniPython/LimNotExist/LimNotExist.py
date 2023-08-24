from sympy import symbols, limit, sqrt, cos, sin

# Definir la variable simbólica x
x = symbols('x')

# Definir la expresión
expression = sqrt(1 - cos(x - 2)**2) / (x - 2)

# Calcular el límite cuando x se acerca a 2 desde la derecha
lim_right = limit(expression, x, 2, dir='+')

# Calcular el límite cuando x se acerca a 2 desde la izquierda
lim_left = limit(expression, x, 2, dir='-')

# Mostrar resultados
print("Límite en el lado derecho de x = 2:", lim_right)
print("Límite en el lado izquierdo de x = 2:", lim_left)