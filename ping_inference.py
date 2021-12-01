"""
ping_inference.py

Sample script to run inference on some dates.
"""

from datetime import timedelta, date

import logging
import requests

### SETTING UP LOGGING ###
logging.basicConfig(
    level=logging.WARNING,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

if __name__ == "__main__":
    start_date = date(2020, 2, 1)
    end_date = date(2020, 5, 31)
    prev_dt = start_date
    for n in range(7, int((end_date - start_date).days) + 1, 7):
        curr_dt = start_date + timedelta(n)
        curr_dt.strftime("%m/%d/%Y")
        # command = f'python main.py --mode=inference --start={prev_dt.strftime("%m/%d/%Y")} --end={curr_dt.strftime("%m/%d/%Y")}'
        # print(command)
        # subprocess.run(command, shell=True)

        # Make command
        req_url = "http://localhost:8001/predict"
        params = {
            "start": prev_dt.strftime("%m/%d/%Y"),
            "end": curr_dt.strftime("%m/%d/%Y"),
        }
        print(f"Making inference request for {params}")

        response = requests.post(req_url, json=params)
        print(f"Response: {response.json()}")

        prev_dt = curr_dt
