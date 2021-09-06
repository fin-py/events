import time 

import requests
from logzero import logger 

def human_requests():
    for num in range(1,151):
        url = f"https://pokeapi.co/api/v2/pokemon/{num}"
        resp = requests.get(url)
        if resp.status_code == 200:
            pokemon = resp.json()
            logger.info(f"{pokemon['id']}: {pokemon['name']}")

if __name__ == '__main__':
    start = time.time()
    human_requests()
    end = time.time()
    logger.info(end-start)
