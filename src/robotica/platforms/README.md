# Adaptador de plataforma

Implementad **solo** el robot recibido: `pidog.py` o `picarx.py`, después de comprobar modelo de Pi y revisión de Robot HAT. Mantened separado el código que habla con la HAT del que decide la misión.

Funciones mínimas a definir en el adaptador: `read_observation()`, `move(command)` y `stop()`. Documentad unidades físicas, intervalos permitidos, calibración y errores de sensor. No supongáis que los pines y API de PiDog V2 y PiCar-X son iguales.
