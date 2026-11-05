"""Regla mínima, independiente del hardware, que prioriza la parada.

Los adaptadores de cada robot deben aplicar una parada física. Esta función solo
indica si se autoriza una nueva orden de movimiento y se puede probar sin Pi.
"""

from __future__ import annotations


def movement_allowed(
    *,
    emergency_stop: bool,
    network_connected: bool,
    obstacle_cm: float | None,
    minimum_obstacle_cm: float,
) -> bool:
    """Deniega movimiento si falta información fiable o hay un riesgo declarado."""
    if emergency_stop or not network_connected:
        return False
    if obstacle_cm is None or obstacle_cm <= 0:
        return False
    if minimum_obstacle_cm < 0:
        raise ValueError("minimum_obstacle_cm no puede ser negativo")
    return obstacle_cm > minimum_obstacle_cm
