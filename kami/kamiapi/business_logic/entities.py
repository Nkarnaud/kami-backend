from dataclasses import dataclass


@dataclass
class PlaneEntity:
    name: str
    plane_id: int
    number_of_seats: int