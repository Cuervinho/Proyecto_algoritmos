# Predicción Ruleta Europea
El problema trata acerca del juego de la ruleta europea donde hay números del 0 hasta el 36 y tres grupos de colores : el rojo , el negro y el verde que es únicamente del 0. El juego trata de realizar apuestas buscando acertar cuál va a ser el próximo número que va a salir y cuál va a ser el color que va a salir  , entonces el proyecto busca sacar una predicción acerca del número que va a salir con base en el historial de números que han salido y además sacar el porcentaje de que salga el color rojo y negro.
La solución encontrada fue tomar la lista de números que salieron anteriormente como una secuencia de números y de esta forma tener una relación entre los números que van saliendo en la ruleta , entonces  tomando el último número de la secuencia y la secuencia misma se buscan los números sucesores a este y se saca una función de probabilidad para todos los números sucesores en cuanto se repitieron como números sucesores y gracias a esto se muestra una interfaz con los números sucesores con mayor probabilidad de salir.

# Ejecución 
Se ejecuta por medio de Python el archivo interfaz.py, el cual le permitira introducir los numeros que le van saliendo. El boton de calculo se habilita despues de las 20 entradas el cual le dara los porcentajes de color y a su vez una predicción de numeros dependiendo de la cantidad de input que haya introducido.

# Ejemplo
![Interfaz](https://i.imgur.com/COUwal9.png)
