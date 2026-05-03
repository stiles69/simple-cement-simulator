# CORE SIMULATION ENGINE
## DATA MODEL
from dataclasses import dataclass

@dataclass
class MaterialFlow:
    rate_tph: float  # tons per hour

@dataclass
class KilnState:
    temperature: float  # °C
    efficiency: float   # 0–1
    fuel_rate: float    # arbitrary units

@dataclass
class PlantState:
    time: float
    feed_rate: float
    clinker_output: float
    energy_used: float
    kiln: KilnState