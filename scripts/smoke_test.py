import sys

import requests

CHECKS = [
    ("/health", 200),
    ("/fees?origin=douala&destination=yaounde&weight=2", 200),
]


def main(base_url: str) -> int:
    for path, expected in CHECKS:
        try:
            response = requests.get(base_url + path, timeout=5)
        except requests.RequestException as exc:
            print(f"ECHEC {path} : {exc}")
            return 1
        if response.status_code != expected:
            print(f"ECHEC {path} : {response.status_code} au lieu de {expected}")
            return 1
        print(f"OK {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
