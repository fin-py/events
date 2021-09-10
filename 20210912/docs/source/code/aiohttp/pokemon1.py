import time 

import requests
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%X")


def human_requests():
    for num in range(1,151):
        url = f"https://pokeapi.co/api/v2/pokemon/{num}"
        resp = requests.get(url)
        if resp.status_code == 200:
            pokemon = resp.json()
            logging.info(f"{pokemon['id']}: {pokemon['name']}")

start = time.time()
human_requests()
end = time.time()
logging.info(f"実行結果: time: {end-start}")
