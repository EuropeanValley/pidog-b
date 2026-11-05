# Reto final · Inspección autónoma · 17 de diciembre de 2026

**Cuándo:** jueves 17 de diciembre, 18:30–20:30. Cada equipo dispone de un turno de unos 20 minutos y **dos intentos**. El docente fijará las medidas finales de la pista, la iluminación y los estímulos después del ensayo del 15 de diciembre. El objetivo es demostrar el robot real, no una simulación ni una reproducción de vídeo.

## Misión común

1. Desde una **web adaptable a móvil o una app**, una persona supervisora ordena `INICIO`; el robot comienza sin teleoperación continua.
2. El robot avanza por su circuito, lee un sensor frontal y **se detiene antes de un obstáculo**. Reanuda cuando el docente lo retira.
3. Llega al puesto de inspección, toma una **imagen de su cámara** y una **medida real de distancia**. Ejecuta un **modelo local en la Raspberry Pi** que produce una decisión `OK`/`INCIDENCIA`. Esa decisión determina un estado final seguro; el robot queda detenido. Esta parte debe funcionar **sin salida a Internet**.
4. Una vez restablecido Internet, envía por **API** la imagen capturada y una **consulta textual que incluye la distancia y el estado local** a un modelo externo capaz de procesar imagen y texto en la misma solicitud. Muestra el informe recibido en la web/app. La respuesta externa no puede mandar movimientos al robot.
5. La web/app muestra en tiempo real **estado, hora, distancia, decisión local, resultado externo y conexión**; recibe `PARADA`. El docente comprueba además la parada local y la respuesta a la pérdida de enlace.

## Movimiento según plataforma

| PiCar-X | PiDog V2 |
| --- | --- |
| Seguir una pista de unos 2–2,5 m con curva suave mediante el módulo de escala de grises, detenerse ante el bloque y terminar en una bahía marcada. | Caminar unos 0,8–1,2 m sin caer, cambiar de orientación unos 30–45°, detenerse ante el bloque y terminar en postura estable. No se exige seguir una línea ni saltar. |

Los valores son referencias de diseño; se congelarán después de probar el material real. La pista se coloca en el suelo y los dos equipos de cada plataforma usan las mismas condiciones.

## Mínimos verificables

| Capacidad | Evidencia durante el turno |
| --- | --- |
| **IA local** | Modelo/pesos o corpus en la Pi; resultado y latencia de dos casos, con Internet desconectado. Puede ser visión local o LLM + RAG local. Una regla fija sobre el nombre de archivo o un servicio en la nube no acredita este requisito. |
| **API externa multimodal** | Dos solicitudes HTTPS reales al modelo elegido, una por cada imagen tomada en el turno, cada una con imagen **y** texto; log de hora, modelo, latencia, solicitud sin secretos y respuesta estructurada (`observacion`, `riesgo`, `recomendacion`). La medida de distancia procede del sensor, no de un valor escrito a mano. |
| **IoT** | Web móvil o app en la red local con actualización **al menos cada segundo** mientras el robot está activo; `INICIO` y `PARADA` supervisados; resultados local/externo y marcas temporales visibles. No se exige app nativa ni publicar el servidor en Internet. |
| **Seguridad** | Obstáculo sin colisión; parada local y remota; pérdida de enlace provoca estado seguro en **≤2 s** durante el ensayo. Una respuesta externa tardía o errónea no activa motores. |
| **Reproducibilidad** | Código Python, esquema y configuración sin secretos, instrucciones de instalación, tres ensayos previos, logs de los dos intentos y aportaciones de los cinco integrantes. |

La consulta externa tiene un timeout configurado (referencia de ensayo: **10 s**). Si falla, el panel muestra `API_NO_DISPONIBLE` y conserva la decisión local. No se envían imágenes de personas. Las claves se guardan fuera de Git, por ejemplo en variables de entorno de la Raspberry Pi. Si la red o las credenciales facilitadas por la universidad fallan para todos, el docente repetirá esa subprueba en condiciones equivalentes.

## Recursos que debe tener cada equipo

Kit PiDog V2 o PiCar-X montado, Raspberry Pi y Robot HAT compatibles, alimentación, cámara, sensor frontal de distancia y código Python de control. El PiCar-X usa además el módulo de escala de grises; el PiDog requiere servos calibrados y marcha estable. Necesitáis acceso a la red local, un móvil o portátil para abrir el panel y credenciales con cuota para un modelo externo que acepte imagen y texto. **Micrófono, altavoz, app nativa y LLM local grande son ampliaciones**, no mínimos. Registrad el modelo exacto de Pi/RAM y probad que el modelo local elegido cabe y responde con latencia útil.

Completad la evidencia en [`docs/hitos/H4.md`](hitos/H4.md), [`docs/ia.md`](ia.md), [`docs/iot.md`](iot.md) y [`docs/pruebas.md`](pruebas.md). El docente comunicará la ficha de puntuación y los estímulos concretos de la prueba.
