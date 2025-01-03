import pytest

from kamiapi.business_logic.entities import PlaneEntity
from kamiapi.factories import AirplaneFactory
from kamiapi.business_logic.services import AirplaneHandler, AirplaneService


@pytest.mark.django_db
class TestrAirplaneHandler:

    @pytest.mark.parametrize("plane_id, plane_name, max_seat", [
        (21,"AIRBUS", 300),
        (2, "BOING", 700)
    ])
    def test_create(self, plane_id, plane_name, max_seat):
        AirplaneFactory(plane_id=plane_id, name="BOING504")
        plane_entity = PlaneEntity(plane_name, plane_id, max_seat)
        service = AirplaneHandler(plane_entity)
        airplane = service.create_plane()
        assert airplane.name == plane_name
        assert airplane.plane_id == plane_id
        assert airplane.number_of_seats == max_seat

    def test_find_by_id(self):
        plane_id=21
        airplane = AirplaneFactory(plane_id=plane_id, name="BOING504")
        plane_entity = PlaneEntity("BOING504", plane_id, 10)
        service = AirplaneHandler(plane_entity)
        exp_airplane = service.find_by_id(plane_id=plane_id)
        assert airplane.name == exp_airplane.name
        assert airplane.plane_id == exp_airplane.plane_id
        assert airplane.number_of_seats == exp_airplane.number_of_seats

    def test_find_plane_by_id(self):
        AirplaneFactory(plane_id=23, name="BOING504")
        exp_airplane = AirplaneHandler.find_by_id(12)
        assert exp_airplane is None


@pytest.mark.django_db
class TestAirplaneService:

    def test_get_plane_fuel_capacity(self):
        plane = AirplaneFactory.create(name="BOING503", plane_id =2)
        assert AirplaneService(plane).get_plane_tank_capacity() == 400

    def test_get_plane_fuel_consumption(self):
        plane = AirplaneFactory.create(name="BOING503", plane_id=2)
        assert AirplaneService(plane).get_plane_fuel_consumption() == 0.5545

    def test_get_plane_total_consumption(self):
        plane = AirplaneFactory.create(name="BOING503", plane_id=2, number_of_seats=340)
        assert AirplaneService(plane).total_consumption() == 1.2345

    def test_calculate_flight_duration(self):
        plane = AirplaneFactory.create(name="BOING503", plane_id=492, number_of_seats=340)
        assert AirplaneService(plane).calculate_flight_duration() == 17450.5214
