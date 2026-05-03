@app.post("/process")
def process(feed_rate: float):
    global kiln

    kiln = update_kiln(kiln, feed_rate, 0.1)

    clinker = feed_rate * kiln.efficiency * 0.65

    return {
        "clinker": clinker,
        "temperature": kiln.temperature
    }