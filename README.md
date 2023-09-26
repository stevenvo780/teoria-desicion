
# Teoría de la Decisión y Experimento en Python

## Introducción

La teoría de la decisión es una rama de la matemática aplicada que trata sobre cómo los agentes deben tomar decisiones óptimas en una situación dada. Este README.md explica los conceptos clave y ofrece un experimento en Python relacionado con la inversión en un portfolio de acciones.

## Conceptos Clave

1. **Espacio de Estados**: Conjunto de todos los posibles estados del mundo. En nuestro experimento, son {Ganar, Perder, Neutral}.
2. **Acciones**: Conjunto de todas las acciones posibles que un agente puede tomar. En este caso, son {Invertir en A, Invertir en B, Invertir en C, No Invertir}.
3. **Función de Utilidad**: Función que asigna un valor numérico a cada estado para representar la "satisfacción" del agente. Aquí, U(Ganar) = 100, U(Perder) = -50, y U(Neutral) = 0.
4. **Función de Transición**: Función que toma un estado y una acción y devuelve una distribución de probabilidad sobre los estados futuros. En nuestro experimento, cada acción tiene su propia función de transición.

### Fórmula para la Utilidad Esperada

El objetivo es encontrar una acción que maximice la utilidad esperada, que se calcula como sigue:

\```
a*= argmax_a Σ(s'* P(s' | s, a) * U(s'))
\```

## Experimento en Python

### Descripción

El experimento involucra la elección de invertir en tres diferentes acciones (A, B, C) o no invertir. Cada acción tiene una probabilidad diferente de ganar, perder o mantenerse neutral.

### Código

El código Python utiliza la biblioteca `matplotlib` para la visualización y `collections.defaultdict` para almacenar las funciones de transición y utilidad. Calcula la utilidad esperada para cada acción y la representa gráficamente.

### Resultados

Los resultados muestran que "Invertir en A" tiene la utilidad esperada más alta, seguido de "Invertir en B" y "Invertir en C". "No Invertir" tiene una utilidad esperada de 0.

## Conclusión

Según la teoría de la decisión, la acción óptima sería "Invertir en A", ya que tiene la utilidad esperada más alta.
