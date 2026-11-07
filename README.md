# CamTrack
API de suivi de colis de CamTrack SARL (entreprise fictive du cours CI/CD + IaC).

## Lancer l'application
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    flask --app "app:create_app" run --port 8000

## Lancer les tests
    pip install pytest ruff
    ruff check . && pytest -q

Les dossiers `infra/` (Terraform, Ansible) et `monitoring/` (Prometheus) sont
remplis aux niveaux 2 et 3 du cours.
