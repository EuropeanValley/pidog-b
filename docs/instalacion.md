# Instalación reproducible

Escribir el procedimiento **realmente seguido** para volver a preparar otra tarjeta microSD del mismo equipo. Indicar versiones, fecha y procedencia de los paquetes; no pegar contraseñas.

1. Modelo de Pi, imagen de Raspberry Pi OS y versión: `Raspberry Pi 5 16GB RAM | Raspberry Pi OS (64bit) 6.18`.
2. Activación de SSH/red y nombre del equipo: `Conexión SSH y por Raspberry Connect configurada | bperro`.
3. Conexión y alimentación segura de la Robot HAT: `HAT instalado, da alimentación a la Raspberry por cable o con la batería del robot`.
4. Entorno Python, dependencias fijadas y origen de librerías SunFounder: `A día 05/11/2026, se usan las dependecias y la versión de Python instaladas por la guía oficial` [Link](https://docs.sunfounder.com/projects/pidog/en/latest/python/python_start/install_all_modules).
5. Copia de `config/robot.example.toml` a `config/robot.local.toml`: `POR_COMPLETAR`.
6. Comandos de arranque del robot y del panel: `A día 05/11/2026, usan los scripts de ejemplo proporcionados por la guía para probar las distintas partes del robot`.
7. Comandos de parada y recuperación de errores: `POR_COMPLETAR`.

## Comprobación tras instalar

| Paso | Comando / acción | Resultado esperado | Resultado observado y fecha |
| --- | --- | --- | --- |
| Pi conectada | Comprobar si está iluminada la LED a lado del botón de encendido. | LED iluminada. | LED iluminada (`05/11/2026`). |
| HAT responde | Mirar si el HAT se ilumina y si del interruptor ON/OFF que hay en este depende que le llegue alimentación a la Raspberry Pi. | LEDs iluminados en el HAT y la Raspberry Pi se enciende tras poner el interruptor en ON. | HAT iluminada y Raspberry Pi recibe alimentación tras poner el interruptor en ON (`05/11/2026`). |
| Sensor leído | Probar a ejecutar el script de prueba proporcionado de ejemplo para cada sensor. [Link a scripts](https://docs.sunfounder.com/projects/pidog/en/latest/python/py_easy_coding.html) | Respuesta del sensor que se desea probar. | Todos los sensores devuelven respuesta (`05/11/2026`). |
| Actuador limitado | Entrar en modo calibración en el SSH mediante `cd ~/pidog/examples` + `sudo python3 0_calibration.py`. | Capacidad de mover todo los servos listados en el panel de control. | Todos los servos responden correctamente a los inputs (`05/11/2026`). |
| IA local | `POR COMPLETAR` | | |
| Interfaz local | Intentar conexión SSH en Visual Studio a la máquina en la red local. | Conexión exitosa a la máquina sin cable. | Conexión establecida con exito (`05/11/2026`). |

Si algo depende de un portátil, de Internet o de una clave, explicarlo. La demo final de IA local debe funcionar sin salida a Internet.
