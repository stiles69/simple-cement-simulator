from fastapi import FastAPI
from threading import Thread
import time

app = FastAPI()

running = False

state = PlantState(
    time=0,
    feed_rate=100,
    clinker_output=0,
    energy_used=0,
    kiln=KilnState(temperature=800, efficiency=0.5, fuel_rate=50)
)

@app.get("/state")
def get_state():
    return state

@app.post("/control")
def control(feed_rate: float = None, fuel_rate: float = None):
    if feed_rate is not None:
        state.feed_rate = feed_rate
    if fuel_rate is not None:
        state.kiln.fuel_rate = fuel_rate
    return {"status": "ok"}

@app.post("/step")
def step():
    global state
    state = step_plant(state, 0.1)
    return state

def run_loop():
    global running, state
    while running:
        state = step_plant(state, 0.1)
        time.sleep(0.1)

@app.post("/run")
def run():
    global running
    running = True
    Thread(target=run_loop).start()
    return {"status": "running"}

@app.post("/stop")
def stop():
    global running
    running = False
    return {"status": "stopped"}