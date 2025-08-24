# Infografia - Universidad Privada Boliviana 1er parcial A

### Adrian Coello - 77258
### Sebastian Nuñez - 77325

## Descripción

Este repositorio contiene el código base para el proyecto de tipo A.

Este proyecto implementa la funcionalidad base del videojuego Angry Birds. El proyecto contiene código para la mecánica fundamental y los objetos necesarios. Usted deberá completar el código fuente e implementar funcionalidades adicionales.

## Instrucciones


### Cómo ejecutar el proyecto

1. **Clona o descarga el repositorio** en tu computadora.
2. **Abre la carpeta** del proyecto con Visual Studio Code.
3. **Abre una terminal** en VS Code (o en la carpeta del proyecto).
4. **Crea y activa un entorno virtual de Python** (recomendado):
	- En Windows:
	  ```powershell
	  python -m venv .venv
	  .venv\Scripts\activate
	  ```
	- En Mac/Linux:
	  ```bash
	  python3 -m venv .venv
	  source .venv/bin/activate
	  ```
5. **Instala las dependencias necesarias** ejecutando:
	```bash
	pip install arcade pymunk numpy
	```
6. **Ejecuta el juego** con el siguiente comando:
	```bash
	python main.py
	```
	Si usas entorno virtual y Windows, también puedes usar:
	```powershell
	.venv\Scripts\python.exe main.py
	```

El juego se abrirá en una ventana nueva. Si tienes problemas con dependencias, asegúrate de estar usando el entorno virtual y de haber instalado los paquetes correctamente.


### Implementación de mecánicas faltantes

La primera parte refiere a la implementación de mecánicas faltantes, en específico, usted deberá implementar las siguientes funciones en el archivo `game_logic.py`:

 - `get_angle_radians`: Esta funcion recibe 2 puntos (Point2D) y devuelve el ángulo entre los mismos en radianes.
 - `get_distance`: Esta función recibe 2 puntos y devuelve la distancia en pixeles entre ambos puntos.
 - `get_impulse_vector`: Usando las funciones anteriores, esta función recibe 2 puntos y devuelve un vector de impulso (ImpulseVector) con el ángulo y el valor del impulso.

La implementación de las funciones restantes completa la mecánica básica del lanzamiento de un angry bird. Una vez terminada la implementación pruebe y valide el funcionamiento del proyecto. Luego de validar el funcionamiento, pase a la siguiente sección.

### Implementación de características adicionales

Una vez completada la implementación de la mecánica principal, usted deberá implementar las siguientes características como nuevas clases en el archivo `game_object.py`:

#### Yellow bird

Si el usuario hace clic en espacio mientras el Yellow Bird está en vuelo, el mismo incrementará su impulso en la dirección en la que está apuntando por un multiplicador aplicado al impulso inicial. El multiplicador estará definido como un argumento al método de inicialización y deberá tener un valor de 2 por defecto.

#### Blue bird

Si el usuario hace clic en espacio mientras el blue bird está en vuelo, éste se convertirá en 3 blue birds instantáneamente, cada uno con una separación de dirección de 30 grados. Por ejemplo, si en el momento del clic el blue bird tiene una dirección de -10 grados, los 3 blue birds resultantes deberán tener direcciones de 20, -10 y -40 grados respectivamente. La velocidad deberá mantenerse para los 3 pájaros.
