# Examen Final del curso Desarrollo de Proyectos
El examen final del curso constó de seis ejercicios y son los siguientes:

#### Ejercicio 01
Realice una Calculadora Básica con en QtDesigner y Python:

![imgEjer01](Recursos/Ejer01.jpg)

#### Ejercicio 02
Realice una Interface grafica en QtDesigner y Python para controlar cargas conectadas a un microcontrolador ARDUINO:

![imgEjer02_Parte1](Recursos/Ejer02_1.png)


![imgEjer02_Parte2](Recursos/Ejer02_2.png)

#### Ejercicio 03
A la aplicación anterior, incorporar la librería de conversión de texto a voz [pyttsx]. También la librería de reconocimiento de voz [speech_recognition u otra], para realizar un sistema domótico de tal forma que obedezca comandos de voy y mencione verbalmente la acción a realizar:

![imgEjer03](Recursos/Ejer03.png)

#### Ejercicio 04
Graficar una o más señales analógicas del Arduino en una GUI (Uso de QwtPlot en QtDesigner).

#### Ejercicio 05
Diseñar una tarjeta de adquisición de datos con Arduino y Python, con una GUI, que permita controlar salidas digitales, entradas digitales, entradas analógicas, salidas analógicas, etc.

#### Ejercicio 06
Aplicación Libre.

---
## Soluciones
Aquí solo mostraré capturas de como los programas ya está funcionando y detrás se apareciará un poco el código realizado. Además...
### Instrucciones de uso de cada aplicativo
Es probable que también quieras probar mis aplicaciones, pero es necesario dar ciertas indicaciones para que puedas probarlas, ya que no están libres de errores, lo cual es entendible ya que solo tuve 3 días para hacerlas y usando una librería que recién había aprendido de una semana. xD (Y eso que las de reconocimiento de voz las aprendí en el momento. :laughing:)

Así que más o menos, después de la "breve descripción" de cada solución se hablaré un poco a detalle de como usarlo. Por último, mencionar que el código de los programas no han sido comentados debido al corto plazo de entrega.

#### Solución 01
Se usó el QtDesigner solo para el diseño de la ventana, sin funcionalidad alguna. Toda la lógica de funcionamiento fue tipeado a pura lógica del programador, o sea yo ;3, y a pensado vagamente sin considerar todas las posibles "trabas" que pudieran haber para que el programa no funcionase, es por ello, que por ejemplo, los paréntesis no tengan utilidad y que solo se puedan hacer operaciones de dos en dos, como `27.345+12.65`.

![imgSln1Ejer01](Recursos/Sln01_Ejer01.png)

#### Solución 02


![imgSln2Ejer02](Recursos/Sln02_Ejer02_1.png)
![imgSln2Ejer02](Recursos/Sln02_Ejer02_2.png)

#### Solución 03


![imgSln3Ejer03](Recursos/Sln03_Ejer03_1.png)
![imgSln3Ejer03](Recursos/Sln03_Ejer03_2.png)

Cada acción es individual, no hay acciones mixtas, por lo que cada acción a realizar será comandado después de presionar el botón "Escuchar". Repito la orden dada por voz es explícitamente una única acción a realizar.

Para el control de encendido o apagado de cada led se menciona la palabra 'control' o 'verde' seguido del número de led a controlar, los comandos exactos son:

'controller 1' | 'controller uno' | 'controla uno' | 'controla 1' | 'controlar 1' | 'controlla uno' | 'controlla 1' | 'verde uno' | 'verde 1'

**Recordar que el número depende del led que desee controlar.**
_Notita: Se escogió el comando 'verde' por el color del led usado en Proteus._

#### Solución 04 y Solución 05
No desarrolladas...
##### Soluciones faltantes?: Si, hay ejercicios que no resolví pero probablemente sean realizados en un futuro como proyectos separados.
Ejercicio 04 y Ejercicio 05 fueron los únicos faltantes.

#### Soluciones 06
Para el caso del sexto ejercicio, ya que era "Aplicativo Libre", **se presentaron dos soluciones para compensar un poco** la falta de las anteriores dos soluciones.
El primero es un reproductor multimedia bastante funcional, se ha probado con los siguientes formatos:

|**Video**|**Audio**|**Imagen**|
|---------|---------|----------|
|.mp4     |.mp3     |.jpg      |
|.avi     |.wav     |.png      |
|.mkv     |         |.gif      |
|.wmv     |         |.ico      |

![imgSln1Ejer06](Recursos/Sln01_Ejer06.png)
![imgSln2Ejer06](Recursos/Sln02_Ejer06.png)

---
## Ejecutables!!
Por último, cabe mencionar, que en la carpeta "Ejecutables", encontrarás los programas en .exe para que directamente los pruebes, aunque no están todos, debido a que se usaron librerías de reconocimiento de voz, es probable de que estas no se puedan compilar, tampoco no le he buscado una solución alternativa ya que estaba a contrareloj con el examen y es muy probable que estos archivos ya no los modifique.

Pero eso no quita el hecho de que no haga más o similares, y mucho mejor trabajados. :smile:
