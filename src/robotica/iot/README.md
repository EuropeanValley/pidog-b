# IoT e interfaz

Implementad una interfaz web adaptable a móvil o app sobre la red local. Mientras el robot está activo, debe mostrar **al menos cada segundo** estado, distancia, conexión y hora de la última lectura; también la decisión de IA local y el informe/error de la API externa. Permitid `INICIO`/`PARADA` supervisados y tratad la pérdida de conexión como condición segura. Nunca aceptéis de la web una velocidad o acción fuera de límites sin validarla en el robot. Documentad protocolo, mensajes, frecuencia y control de acceso en `docs/iot.md`.
