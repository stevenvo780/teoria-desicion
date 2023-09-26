import matplotlib.pyplot as plt
from collections import defaultdict

# Definir el espacio de estados y las acciones
states = ['Ganar', 'Perder', 'Neutral']
actions = ['Invertir en A', 'Invertir en B', 'Invertir en C', 'No Invertir']

# Definir la función de utilidad
utility = {'Ganar': 100, 'Perder': -50, 'Neutral': 0}

# Definir la función de transición
transition = {
    'Invertir en A': {'Ganar': 0.7, 'Perder': 0.2, 'Neutral': 0.1},
    'Invertir en B': {'Ganar': 0.5, 'Perder': 0.4, 'Neutral': 0.1},
    'Invertir en C': {'Ganar': 0.4, 'Perder': 0.3, 'Neutral': 0.3},
    'No Invertir': {'Neutral': 1.0},
}

# Calcular la utilidad esperada para cada acción
expected_utility = {}

for action in actions:
    expected_utility[action] = sum(
        transition[action][state] * utility[state] for state in transition[action])

print(expected_utility)

# Gráfico para representar la utilidad esperada
plt.figure(figsize=(10, 6))
plt.bar(expected_utility.keys(), expected_utility.values(),  # type: ignore
        color='blue')
plt.xlabel('Acciones')
plt.ylabel('Utilidad Esperada')
plt.title('Utilidad Esperada por Acción')
plt.show()
