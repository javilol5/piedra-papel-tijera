Práctica curso Programación para IA
===================================

Extender el código disponible en `05_RPS_More_AI.py` con la funcionalidad necesaria para
implementar la variante lagarto - Spock del juego piedra, papel o tijeras.

[Práctica curso Programacion para IA](#práctica-curso-programacion-para-ia)
  - [Solución](#solución)
  - [Refactorizaciones](#refactorizaciones)
  - [Testing](#testing)


## Solución

Solución propuesta en [`RPS_spock_lizard.py`](.src/../src/RPS_spock_lizard.py)

## Refactorizaciones

Es necesario refactorizar la función `assess_game()` para conseguir una solución abierta a la extensión y cerrada a la modificación, o principio Open/Closed (OCP) de SOLID.

La inclusión de nuevas categorías en el juego original produce una extensión de la estructura `if-elif-else` que deriva en código cableado, o cierto [input kludge antipattern](https://sourcemaking.com/antipatterns/input-kludge).

Podría haber optado por eliminar la cláusula `if-elif-else` implementando polimorfismo de clase, pero he optado por expresar en el diccionario `Victories` -que ya estaba implementado en el código inicial- las reglas de la lógica del juego de manera declarativa, para mejorar la legibilidad del código. 

No es una solución 100% OCP puesto que si las categorías del juego aumentan no sería viable extender el diccionario, pero confiemos en que la serie _Big Bang Theory_ no goce de una secuela y aumenten el juego con nuevas acciones ;) 

Para ello, he extendido el comportamiento del tipo enumerado `GameAction` simulando la diferencia de conjuntos en la función `minus(excluded_actions)`. Podría haber usado el tipo `set` de Python pero rompia la interfaz `list` necesaria en la función `get_random_computer_action()`. 

He refactorizado la función `get_random_computer_action()` para reutilizarla en `get_winner_action(game_action)`.

Finalmente, he encapsulado la lógica el juego en la clase `Game`. He decidido no usar una clase con métodos estáticos para poder generar distintas instancias del juego. 


## Testing

En todo proceso de refactorización de código es necesario incluir un conunto de casos test en aquellos comportamientos más susceptibles de presentar defectos.

Aunque no he practicado TDD estricta (que es como suelo codificar), he incluído casos test para eliminar defectos del código cuando he estimado que la lógica estaba completada.

Es necesario contar con `pytest` instalado en el entorno virtual.

Para seleccionar sólo los casos test de la lógica extendida: 

```bash
$ pytest -v -m lizard
$ pytest -v -m spock
```

## AIML

He simplicado la salida por consola de la app al mensaje:

`"%s wins %s. You lost!" %(computer_action.name, user_action.name)`

Es posible implementar las salidas de la aplicación de una manera más explícita usando un fichero `.aiml` y accediendo a los elementos XML con el módulo `xml.etree.ElementTree`. Implementaré esta extensióm a lo largo de esta semana.