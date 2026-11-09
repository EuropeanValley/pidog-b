# Inventario y conexiones verificadas

**Fecha de inventario:** `2026-11-08` · **Responsables:** `@foreverprogramming`, `@jorgee12-19`

| Componente | Modelo / revisión / cantidad real | Estado y prueba realizada | Foto o referencia |
| --- | --- | --- | --- |
| Robot base | `PiDog V2` | Montado y revisado; estabilidad y alineación comprobadas | `pendiente` |
| Raspberry Pi y RAM | `Raspberry Pi 5, 16 GB RAM` | Base de cómputo y control; conectada a la HAT y operativa | `pendiente` |
| Robot HAT | `SunFounder PiDog HAT (kit PiDog V2)` | Alimentación y puertos verificados en instalación | `pendiente` |
| Cámara | `Cámara CSI del kit / cámara PiDog` | Probar adquisición de imagen y encuadre en la zona de inspección | `pendiente` |
| Baterías y cargador | `Batería del robot + cargador compatible` | Comprobado el arranque y alimentación segura | `pendiente` |
| microSD / SO | `microSD 64 GB + Raspberry Pi OS 64-bit` | Sistema operativo instalado y probado | `pendiente` |
| Sensores adicionales | `Sensor frontal ultrasónico + IMU` | Lecturas validadas y uso en la lógica de seguridad | `pendiente` |

## Mapa eléctrico y mecánico

El PiDog V2 usa la Raspberry Pi conectada a la HAT de control, que distribuye la alimentación y expone los puertos para servos, sensores y cámara. La seguridad se implementa a nivel lógico y físico: si la lectura es inválida, hay pérdida de enlace o se supera el umbral de riesgo, el robot debe pasar a `PARADA`.

| Puerto / pin | Tensión | Componente | Señal / librería | Comprobación |
| --- | --- | --- | --- | --- |
| GPIO / bus I2C | 3.3V / 5V (según módulo) | IMU y sensores | lectura/toma de datos | comprobado en arranque y sistema de seguridad |
| CSI | 3.3V + señal serial | Cámara | captura de imagen | pendiente de validación en robot |
| Servo headers | 5V y PWM | patas / servos | control por software | ajuste mecánico y pruebas de movimiento |
| Ultrasonido frontal | 5V | sensor de distancia | lectura digital/analógica | lectura integrada en la lógica de decisión |
| Alimentación HAT | 7.4V / 5V según kit | batería + HAT | distribución a Pi y servos | validado en arranque |

## Calibración y límites

- Procedimiento de centrado/ajuste de servos o dirección: posicionar servos en `HOME`, comprobar alineación del chasis y ajustar longitudes o ángulos para mantener postura estable antes de cada ensayo.
- Velocidad y ángulos máximos ensayados: velocidad reducida para pruebas iniciales; ángulos de giro y estabilidad limitados para evitar caídas o pérdida de equilibrio.
- Distancia de parada medida: objetivo de parada y reanuda con margen de seguridad por encima del umbral de riesgo; se valida con lecturas frontales del sensor antes del bloque.
- Acción local para detener el robot: bloqueo de movimiento por lógica de seguridad y parada física del actuador si se supera el riesgo o se pierde la conexión.
- Lugar y condiciones de las pruebas: suelo despejado y delimitado, con iluminación estable y zona libre de obstáculos no previstos.
