def update_kiln(kiln: KilnState, feed_rate: float, dt: float):
    # Heat input
    heat_in = kiln.fuel_rate * 50

    # Heat loss (material + environment)
    heat_out = feed_rate * 2 + (kiln.temperature - 300) * 0.1

    # Temperature update
    kiln.temperature += (heat_in - heat_out) * dt * 0.1

    # Efficiency curve (peaks near 1450°C)
    optimal_temp = 1450
    kiln.efficiency = max(0, 1 - abs(kiln.temperature - optimal_temp) / 500)

    return kiln