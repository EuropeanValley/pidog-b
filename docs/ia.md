# IA local y modelo externo: diseño y evaluación

**Ruta elegida:** `visión` · **Fecha de decisión:** `2026-11-08`

## Función en la misión

La IA local procesa la imagen de la cámara del robot para decidir si el estado observado es `OK` o `INCIDENCIA`, usando solo datos adquiridos en la Raspberry Pi del equipo y sin conexión a Internet. La decisión local tiene prioridad sobre cualquier respuesta externa y, si el robot no está en un estado seguro, la misión se bloquea.

## Modelo y datos

- Nombre, versión, licencia y procedencia del modelo: `modelo de visión ligero ejecutado localmente en la Raspberry Pi, con pesos y configuración del equipo`.
- Modelo, pesos y corpus almacenados en: `Raspberry Pi del robot`.
- Datos de entrenamiento/ajuste y de **prueba separada**; procedencia y permisos: `conjunto de muestras y pruebas del entorno de inspección, sin incluir datos personales ni terceros`.
- Si es RAG: documentos, segmentación, recuperación, fuente citada y validación de órdenes: `no aplica en la ruta elegida`.
- Si es visión: clases, condiciones de iluminación/distancia y matriz de confusión: `clases de interés: OK, incidencia, riesgo y ausencia de señal; condiciones de iluminación controladas y captura a distancia útil con margen de seguridad`.

## Medidas en la Raspberry Pi real

| Fecha | Versión | Caso | Salida esperada | Salida observada | Latencia | Estado del robot |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11-08 | Local / prototipo | imagen de prueba | `OK` o `INCIDENCIA` | pendiente de validación en robot | < 2 s objetivo | detenido y seguro |

## Límites y reserva

Si la confianza de la inferencia es baja, la predicción es ambigua, el modelo falla o tarda demasiado, el robot no acepta la acción del sistema como orden de movimiento. La decisión final sigue siendo una salida de estado para la interfaz y la misión, pero la seguridad prevalece: el robot queda detenido.

La comprobación de ejecución local se realiza sin salida a Internet y con la Raspberry Pi del robot como único entorno de cómputo.

## API externa y entrada multimodal

- Proveedor/modelo externo y función: `modelo multimodal capaz de recibir imagen + texto`.
- Origen de la imagen: `cámara del robot, capturada al llegar al punto de inspección`.
- Consulta textual y medida real de distancia incluida (unidad y marca temporal): `texto con distancia frontal, estado local y marca temporal; se incluye la distancia en cm`.
- Campos esperados de la respuesta: `observacion`, `riesgo` (`OK`/`INCIDENCIA`) y `recomendacion`.
- Timeout, reintentos, cuota y respuesta segura ante error: `timeout configurado, fallos conservadores y visualización de API_NO_DISPONIBLE si no responde`.
- Dónde se guarda la credencial **fuera del repositorio**: `variables de entorno del sistema o archivo local de configuración no versionado`.

| Fecha | Caso | Imagen / hash o referencia | Texto y distancia enviada | Modelo | Respuesta resumida | Latencia | Error / contraste con IA local |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-08 | prueba de preparación | `captura del entorno, sin personas` | `distancia frontal + decisión local + marca temporal` | `externo multimodal` | pendiente de validación | objetivo < 10 s | la decisión local se mantiene si la API falla |

La salida de la API sirve como **informe**, no como orden directa a actuadores. Si discrepa de la decisión local, se documenta el desacuerdo y el robot sigue detenido. Se guardan solo metadatos y muestras que no contengan datos personales ni secretos.
