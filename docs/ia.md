# IA local y modelo externo: diseño y evaluación

**Ruta elegida:** `visión` / `LLM + RAG` · **Fecha de decisión:** `AAAA-MM-DD`

## Función en la misión

Entrada real → inferencia → decisión/estado del robot: `POR_COMPLETAR`.

## Modelo y datos

- Nombre, versión, licencia y procedencia del modelo: `POR_COMPLETAR`.
- Modelo, pesos y corpus almacenados en: `POR_COMPLETAR`.
- Datos de entrenamiento/ajuste y de **prueba separada**; procedencia y permisos: `POR_COMPLETAR`.
- Si es RAG: documentos, segmentación, recuperación, fuente citada y validación de órdenes: `POR_COMPLETAR`.
- Si es visión: clases, condiciones de iluminación/distancia y matriz de confusión: `POR_COMPLETAR`.

## Medidas en la Raspberry Pi real

| Fecha | Versión | Caso | Salida esperada | Salida observada | Latencia | Estado del robot |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Límites y reserva

¿Qué hace el robot con confianza baja, respuesta incorrecta, modelo caído o inferencia demasiado lenta? `POR_COMPLETAR`. Indicar cómo se comprobó que el proceso se ejecuta en la Pi sin salida a Internet.

## API externa y entrada multimodal

- Proveedor/modelo externo y función: `POR_COMPLETAR`. Debe aceptar **imagen + texto** en la misma solicitud; no es el modelo local evaluado arriba.
- Origen de la imagen: cámara del robot; cuándo se captura y cómo se evita incluir personas: `POR_COMPLETAR`.
- Consulta textual y medida real de distancia incluida (unidad y marca temporal): `POR_COMPLETAR`.
- Campos esperados de la respuesta: `observacion`, `riesgo` (`OK`/`INCIDENCIA`) y `recomendacion`.
- Timeout, reintentos, cuota y respuesta segura ante error: `POR_COMPLETAR`.
- Dónde se guarda la credencial **fuera del repositorio** (sin mostrar su valor): `POR_COMPLETAR`.

| Fecha | Caso | Imagen / hash o referencia | Texto y distancia enviada | Modelo | Respuesta resumida | Latencia | Error / contraste con IA local |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

La salida de la API sirve como **informe**, no como orden directa a actuadores. Si discrepa de la decisión local, documentar el desacuerdo y mantener el robot detenido. Guardar solo metadatos y muestras que no incluyan datos personales ni secretos.
