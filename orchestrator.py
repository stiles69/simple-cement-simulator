def run_cycle():
    raw_output = call_raw_service(feed_rate)
    kiln_output = call_kiln_service(raw_output)
    final_output = call_finish_service(kiln_output)