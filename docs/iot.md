# IoT e interfaz local en tiempo real

**Mínimo de H3/H4:** web adaptable a móvil o app que funcione en la red local del taller. Mientras el robot está activo, actualizar el panel **al menos cada segundo** y mostrar marca temporal de la última lectura. Una aplicación nativa no es necesaria.

- Protocolo y justificación (`HTTP`, `WebSocket`, `MQTT`, etc.): `POR_COMPLETAR`.
- Diagrama de red, dirección local y puerto **sin secretos**: `POR_COMPLETAR`.
- Cliente: navegador en portátil/móvil o aplicación; versión y URL local: `POR_COMPLETAR`.

| Mensaje / endpoint | Origen → destino | Datos y unidades | Frecuencia | Validación y error |
| --- | --- | --- | --- | --- |
| Estado de misión y enlace | Robot → interfaz | Estado, hora | ≤1 s | Mostrar lectura antigua si hay desconexión. |
| Distancia frontal | Robot → interfaz | cm y hora | ≤1 s | Señalar lectura inválida. |
| IA local y API externa | Robot → interfaz | Decisión local, informe/riesgo externo, latencias, error | Por evento | No sobrescribir la decisión local con la externa. |
| Inicio supervisado | Interfaz → robot | `INICIO` | Por evento | Validar estado y usuario antes de aceptar. |
| Parada | Interfaz → robot | `PARADA` | Por evento | Prioridad sobre cualquier misión o llamada API. |

## Seguridad y fallo de red

Especificar autorización de órdenes, límite de velocidad, timeout/heartbeat y prioridad de parada. Registrar el ensayo real de pérdida de enlace y tiempo hasta la parada. Una interfaz accesible desde fuera del taller requiere decisión y configuración expresas del docente; la versión mínima funciona en red local.

| Ensayo | Fecha y commit | Esperado | Observado (s) | Evidencia |
| --- | --- | --- | --- | --- |
| Frecuencia de telemetría | | ≤1 s entre actualizaciones | | |
| Orden `PARADA` | | Robot inmóvil | | |
| Pérdida de enlace | | Estado seguro en ≤2 s | | |
| API externa no responde | | Panel indica error; decisión local intacta | | |
