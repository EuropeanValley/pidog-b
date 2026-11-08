# Instalación reproducible

El procedimiento siguiente refleja la preparación del equipo PiDog V2 utilizada como base para el proyecto y se ha de repetir con la misma lógica si se cambia de microSD o se vuelve a instalar el sistema.

1. Modelo de Pi, imagen de Raspberry Pi OS y versión: `Raspberry Pi 5 con 16 GB RAM; Raspberry Pi OS (64-bit), versión actual de la guía oficial del kit`.
2. Activación de SSH/red y nombre del equipo: `SSH habilitado, conexión en red local configurada y equipo identificado para pruebas del robot`.
3. Conexión y alimentación segura de la Robot HAT: `HAT instalada, toma de corriente gestionada por la HAT y alimentación segura para Raspberry Pi y servos`.
4. Entorno Python, dependencias fijadas y origen de librerías SunFounder: `Se usa el entorno recomendado por la guía oficial del PiDog V2 y las librerías del kit para sensores, servos y cámara` [Link](https://docs.sunfounder.com/projects/pidog/en/latest/python/python_start/install_all_modules).
5. Copia de `config/robot.example.toml` a `config/robot.local.toml`: `revisar la configuración local del equipo, sin incluir claves ni secretos y dejando solo parámetros del robot y la red local`.
6. Comandos de arranque del robot y del panel: `se prueban los scripts de ejemplo del kits para arrancar sensores, servos y sistema de control, y se valida que el panel en red local responde`.
7. Comandos de parada y recuperación de errores: `parada local con orden PUT/PARADA, comprobación de IMU y sensores, y reinicio desde HOME`.

## Comprobación tras instalar

| Paso | Comando / acción | Resultado esperado | Resultado observado y fecha |
| --- | --- | --- | --- |
| Pi conectada | Comprobar que la Raspberry Pi recibe alimentación y que la HAT se activa correctamente. | LED/encendido y estado estable. | Confirmado en la instalación inicial (`05/11/2026`). |
| HAT responde | Comprobar que la HAT alimenta la Pi y que los indicadores de estado responden. | LEDs activos y arranque estable. | Observado con la Raspberry Pi encendida (`05/11/2026`). |
| Sensor leído | Ejecutar scripts de prueba del kit para ultrasonido, IMU y motores. | Respuesta válida de cada sensor y actuador. | Confirmado en pruebas del equipo (`05/11/2026`). |
| Actuador limitado | Ejecutar el script de calibración de servos y comprobar que responden. | Todos los servos responden y la postura se puede centrar. | Validado con ejercicios de ajuste (`05/11/2026`). |
| IA local | Ejecutar la inferencia en la Raspberry Pi sin Internet. | Decisión local devuelta con latencia útil. | Pendiente de validación en robot para la misión final. |
| Interfaz local | Conectarse al equipo desde la red local y comprobar el panel/web. | Conexión estable a la máquina y actualización del estado. | Validado en la red local (`05/11/2026`). |

Si algo depende de un portátil, Internet o de una clave, debe documentarse. La demo final de IA local debe funcionar sin salida a Internet.
