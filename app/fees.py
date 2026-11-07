INTERCITY_FEE = 1500      # FCFA, Douala vers Yaoundé
SAME_CITY_FEE = 1000      # FCFA, même ville
FREE_WEIGHT_KG = 5        # poids inclus dans les frais de base
SURCHARGE_PER_KG = 200    # FCFA par kg au-delà de 5 kg


def delivery_fee(origin: str, destination: str, weight_kg: float) -> int:
    base = SAME_CITY_FEE if origin == destination else INTERCITY_FEE
    extra_kg = max(0, weight_kg - FREE_WEIGHT_KG)
    return base + int(extra_kg * SURCHARGE_PER_KG)
