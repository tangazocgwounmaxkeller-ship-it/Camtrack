import pytest

from app.fees import delivery_fee


@pytest.mark.parametrize(
    "origin,destination,weight,expected",
    [
        ("douala", "douala", 2, 1000),
        ("douala", "yaounde", 2, 1500),
        ("douala", "yaounde", 5, 1500),   # 5 kg : pas de supplément
        ("douala", "yaounde", 8, 2100),   # 3 kg de supplément
    ],
)
def test_delivery_fee(origin, destination, weight, expected):
    assert delivery_fee(origin, destination, weight) == expected
