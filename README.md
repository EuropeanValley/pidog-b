# Proyecto de Robótica y automatización · Equipo

> Completar esta portada durante H1. Este repositorio pertenece a **un equipo de cinco** y reúne código, configuración reproducible, decisiones, pruebas y evidencias de los cuatro hitos. No contiene las respuestas de la prueba final.

| Dato | Valor |
| --- | --- |
| Equipo | `POR_COMPLETAR` |
| Plataforma | `PiDog V2` / `PiCar-X` |
| Integrantes (usuario GitHub) | `@...`, `@...`, `@...`, `@...`, `@...` |
| Raspberry Pi (modelo, RAM) | `POR_COMPLETAR` |
| Robot HAT (revisión) | `POR_COMPLETAR` |
| Misión elegida | `POR_COMPLETAR` |
| Ruta de IA local | `Visión` / `LLM + RAG` |
| Modelo externo por API | `POR_COMPLETAR` |
| Interfaz IoT | `POR_COMPLETAR` |
| Estado actual | `H1 / H2 / H3 / H4` |

## Primeros pasos

1. Crear el equipo en Classroom 50 y clonar el **repositorio de ese equipo**. No trabajar en el repositorio plantilla.
2. Completar esta portada y [equipo y roles](docs/equipo.md). Registrar el material **real** en [hardware](docs/hardware.md); la foto de la caja o una guía no sustituyen el inventario.
3. Copiar `config/robot.example.toml` a `config/robot.local.toml` y completar los valores sin guardar contraseñas. La copia local está ignorada por Git.
4. Escribir el procedimiento de [instalación](docs/instalacion.md) y comprobarlo en la Raspberry Pi del equipo.
5. Crear tareas mediante Issues, trabajar en ramas cortas y revisar los cambios con Pull Requests. Consultar [CONTRIBUTING.md](CONTRIBUTING.md).
6. Para **H1 (9 de noviembre)**, entregar el documento en [`docs/arquitectura.md`](docs/arquitectura.md) y registrar el commit en [su ficha](docs/hitos/H1.md). Para los hitos siguientes, enlazar código, ensayos y resultados en [H2](docs/hitos/H2.md), [H3](docs/hitos/H3.md) y [H4](docs/hitos/H4.md).

La misión que orienta H3 y H4 se describe en el [reto final de inspección autónoma](docs/reto_final.md). La integración mínima combina un modelo **local**, una API externa que acepte **imagen y texto**, y una web/app de red local con telemetría y `INICIO`/`PARADA`.

## Mapa del repositorio

| Ruta | Uso |
| --- | --- |
| `src/robotica/platforms/` | Adaptador del kit elegido: actuadores, sensores y Robot HAT. |
| `src/robotica/mission/` | Máquina de estados y lógica de misión. |
| `src/robotica/ai/` | Inferencia local y cliente de API externa; no guardar credenciales. |
| `src/robotica/iot/` | API, telemetría y panel web o móvil. |
| `src/robotica/safety.py` | Contrato mínimo de bloqueo del movimiento ante riesgo. |
| `config/` | Ejemplo público de configuración; valores locales ignorados. |
| `tests/` | Pruebas ejecutables sin robot; las pruebas físicas se registran en `docs/pruebas.md`. |
| `docs/` | Arquitectura, instalación, decisiones, bitácora, pruebas e hitos. |
| `data/` | Muestras pequeñas, anónimas y con procedencia documentada. |
| `media/` | Capturas pequeñas; vídeos grandes mediante enlace institucional estable. |

## Comprobaciones locales

Desde la raíz del repositorio:

```bash
python3 -m compileall -q src
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Estas comprobaciones no sustituyen las pruebas en el robot. La acción de GitHub solo ejecuta código independiente del hardware; el montaje, la IA real, los sensores y la seguridad se demuestran en taller.

## Evidencia de avance

En cada entrega dejar: enlace al commit o Pull Request, vídeo o fotos fechadas, tabla de ensayos con **resultado observado** (incluidos fallos), limitaciones y contribución de cada integrante. La [bitácora](docs/bitacora.md) se actualiza al terminar cada sesión. La evaluación la determina el docente con la guía oficial; un check verde de CI solo indica que pasa la comprobación técnica mínima.

## Reglas de uso

- No subir claves, contraseñas, `.env`, imágenes del sistema, datos personales ni vídeos pesados.
- No permitir movimiento autónomo fuera de la zona de pruebas; mantener parada local y supervisión.
- La inferencia de IA declarada como **local** debe ejecutarse en la Raspberry Pi del robot y poder demostrarse sin salida a Internet.
- La API externa genera un informe multimodal; jamás manda órdenes directas a motores. Guardar la clave fuera de Git y documentar cuándo se requiere Internet.

La guía del PiCar-X y los manuales de SunFounder son material de consulta; cada equipo verifica la revisión exacta de su hardware antes de cablear o alimentar. El equipo PiDog documenta su propio montaje y calibración con el manual específico.
