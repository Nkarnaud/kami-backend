from dataclasses import dataclass
from typing import Optional

import math

from kamiapi.business_logic.entities import PlaneEntity
from kamiapi.models import Airplane


@dataclass
class AirplaneHandler:
    plane: PlaneEntity

    def create_plane(self) -> Airplane:
        print(self.plane.plane_id)
        print(self.plane.name)
        airplane, _ = Airplane.objects.update_or_create(
            plane_id=self.plane.plane_id,
            defaults=dict(
                name=self.plane.name,
                number_of_seats=self.plane.number_of_seats
            )
        )
        return airplane

    @staticmethod
    def find_by_id(plane_id) -> Optional[Airplane]:
        if airplane := Airplane.objects.filter(plane_id=plane_id).first():
            return airplane
        else:
         return None


@dataclass
class AirplaneService:
    airplane: Airplane
    Tank_capacity: int = 200

    def get_plane_tank_capacity(self) -> int:
        return self.airplane.plane_id * self.Tank_capacity

    def get_plane_fuel_consumption(self) -> float:
        return round(math.log(self.airplane.plane_id) * 0.80, 4)

    def total_consumption(self) -> float:
        return round(self.get_plane_fuel_consumption() + (self.airplane.number_of_seats * 0.002), 4)

    def calculate_flight_duration(self) -> float:
        total_consumption = self.total_consumption()
        if total_consumption > 0:
            return round(self.get_plane_tank_capacity() / total_consumption, 4)

        return 0
