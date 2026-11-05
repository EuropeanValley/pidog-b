# Trabajo en equipo y trazabilidad

## Flujo recomendado

1. Abrir una Issue por tarea o fallo, con responsable y criterio de terminado. Asociarla al hito correspondiente en Classroom 50 o en la organización.
2. Crear una rama corta desde `main`, por ejemplo `feature/lectura-ultrasonido` o `fix/parada-red`.
3. Hacer commits pequeños con mensaje claro (`feat: añade lectura de ultrasonidos`, `test: cubre parada por desconexión`). Evitar que una sola persona suba todo el proyecto al final.
4. Abrir Pull Request usando la plantilla. Otro integrante revisa código, pruebas y efecto físico antes de fusionar. Los cambios de alimentación, actuadores o parada requieren también ensayo supervisado.
5. Fusionar en `main` tras CI y revisión. El hito apunta a un commit concreto de `main`; etiquetar opcionalmente `h1`, `h2`, `h3`, `h4` **después** de la entrega.

La persona responsable de integración rota entre hitos. Mantener una tabla de contribuciones en `docs/equipo.md`; una lista de nombres sin evidencias no basta. La autoría de commits ayuda, pero no sustituye explicaciones, revisiones y pruebas realizadas por los cinco integrantes.

## Definición de terminado

- El cambio tiene Issue o motivo documentado, pruebas proporcionadas a su riesgo y resultado real en el robot cuando afecta hardware.
- Las instrucciones de instalación/configuración y el esquema se actualizan si cambian.
- Un fallo conocido se anota en `docs/bitacora.md` o una Issue; no se oculta porque la demo funcione una vez.
- Ninguna prueba deja motores activos al salir por error o al perder conexión.

## Registro de decisiones

Decisiones como ruta de IA, protocolo IoT, sensor adicional o cambio de misión se anotan en `docs/arquitectura.md` con fecha, alternativas y motivo. Así puede verse la evolución entre hitos.
