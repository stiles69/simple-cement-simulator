# Plant Step Function
def step_plant(state: PlantState, dt: float):
    # Update kiln
    state.kiln = update_kiln(state.kiln, state.feed_rate, dt)

    # Clinker production
    state.clinker_output = state.feed_rate * state.kiln.efficiency * 0.65

    # Energy usage
    state.energy_used += state.kiln.fuel_rate * dt

    # Time
    state.time += dt

    return state