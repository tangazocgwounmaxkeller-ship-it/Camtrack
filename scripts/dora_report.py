import csv
import statistics
import sys
from datetime import date, datetime


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main(path: str, months: int = 10) -> None:
    rows = load(path)
    lead_times = [
        (date.fromisoformat(r["deploiement"]) - date.fromisoformat(r["commit_valide"])).days
        for r in rows
    ]
    failures = [r for r in rows if r["incident"] == "oui"]
    recoveries = [
        (
            datetime.fromisoformat(r["retablissement"])
            - datetime.fromisoformat(r["debut_incident"])
        ).total_seconds()
        / 3600
        for r in failures
    ]
    print(f"Fréquence de déploiement : {len(rows) / months:.1f} par mois")
    print(
        f"Délai de livraison : moyenne {statistics.mean(lead_times):.1f} j, "
        f"médiane {statistics.median(lead_times):.1f} j"
    )
    print(f"Taux d'échec des changements : {len(failures) / len(rows):.0%}")
    print(f"Temps de rétablissement moyen : {statistics.mean(recoveries):.1f} h")


if __name__ == "__main__":
    main(sys.argv[1])
