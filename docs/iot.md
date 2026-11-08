# IoT e interfaz local en tiempo real

**Mínimo de H3/H4:** la interfaz debe funcionar en la red local del taller, actualizar el estado al menos cada segundo mientras el robot está activo y mostrar la marca temporal de la última lectura. Una app nativa no es necesaria; una web adaptable a móvil es suficiente.

- Protocolo y justificación: `HTTP + WebSocket` en la red local. HTTP sirve para el estado inicial y las órdenes; WebSocket permite actualización en tiempo real sin recargar la página.
- Diagrama de red, dirección local y puerto **sin secretos**: `http://<ip-local-del-robot>:8000` y puerto `8000` para el backend; el cliente se conecta desde un navegador del portátil o móvil del taller.
- Cliente: `navegador local del equipo` en móvil o portátil; URL local tipo `http://<ip-local>:8000`.

| Mensaje / endpoint | Origen → destino | Datos y unidades | Frecuencia | Validación y error |
| --- | --- | --- | --- | --- |
| Estado de misión y enlace | Robot → interfaz | estado, hora, conexión | ≤1 s | mostrar lectura antigua si se pierde enlace |
| Distancia frontal | Robot → interfaz | cm y hora | ≤1 s | marcar lectura inválida si no se recibe dato fiable |
| IA local y API externa | Robot → interfaz | decisión local, riesgo externo, latencia, error | por evento | la explicación externa no debe sustituir a la local |
| Inicio supervisado | Interfaz → robot | `INICIO` | por evento | validar estado y usuario antes de aceptar |
| Parada | Interfaz → robot | `PARADA` | por evento | prioridad máxima sobre cualquier otra orden o llamada |

## Seguridad y fallo de red

La interfaz manda órdenes con un nivel de autorización explícito. La parada local tiene prioridad absoluta sobre cualquier otra acción, y la pérdida de enlace debe llevar a un estado seguro en menos de 2 segundos. También se contempla la condición en la que la API externa no responde: el panel marca `API_NO_DISPONIBLE` y la decisión local se conserva.

| Ensayo | Fecha y commit | Esperado | Observado (s) | Evidencia |
| --- | --- | --- | --- | --- |
| Frecuencia de telemetría | 2026-11-08 | ≤1 s entre actualizaciones | pendiente de ensayo | panel local de monitorización |
| Orden `PARADA` | 2026-11-08 | robot inmóvil y sin reanudar | pendiente de ensayo | registro del panel y observación en taller |
| Pérdida de enlace | 2026-11-08 | estado seguro en ≤2 s | pendiente de ensayo | monitor y registro de red |
| API externa no responde | 2026-11-08 | panel indica error; decisión local intacta | pendiente de ensayo | log de error y telemetría |
