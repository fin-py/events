import time
import urllib.request


def _get_status_code(url):
    with urllib.request.urlopen(url) as res:
        return res.status


def get_status_code(cor_name, n):
    url = f"https://httpbin.org/delay/{n}"
    http_status = _get_status_code(url)
    print(f"{cor_name}: {http_status}")


def main():
    get_status_code("cor1", 2)
    get_status_code("cor2", 5)


start = time.time()
main()
print(f"time: {time.time() - start}")
