import json

from kamiapi.factories import AirplaneFactory
import pytest


@pytest.mark.django_db
class TestAirplaneViewSet:

    def test_create_airplane_with_wrong_payload_return400(self, client):
        payload = {
            "name": None,
            "plane_id": None,
            "number_of_seats": "asdf"
        }
        resp = client.post('/api/v1/airplanes/', data=json.dumps(payload), content_type='application/json')
        assert resp.status_code == 400
        assert resp.data == {
            'message': 'Bad Request',
            'error': {
            'name': ['This field may not be null.',],
            'plane_id': ['This field may not be null.'],
            'number_of_seats': ['A valid integer is required.']
        }}

    def test_create_airplane(self, client):
        payload = {
            "name": '<NAME>',
            "plane_id": 42053578,
            "number_of_seats": 12
         }
        resp = client.post('/api/v1/airplanes/', data=json.dumps(payload), content_type='application/json')
        assert resp.status_code == 201
        assert resp.data['base_fuel_consumption'] == 14.0436
        assert resp.data['flight_duration'] is not None
        assert resp.data['name'] == "<NAME>"
        assert resp.data['number_of_seats']  == 12
        assert resp.data['plane_id'] == 42053578
        assert resp.data['total_fuel_consumption'] == 14.0676
        assert resp.data['tank_capacity'] == 8410715600

    def test_retrieve_airplane_return_http200(self, client):
        plane = AirplaneFactory.create(
            name="<NAME>",
            plane_id=42053579,
            number_of_seats=8
        )
        resp = client.get(f'/api/v1/airplanes/{plane.id}/')

        assert resp.status_code == 200
        assert resp.data['base_fuel_consumption'] == 14.0436
        assert resp.data['flight_duration'] is not None
        assert resp.data['name'] == "<NAME>"
        assert resp.data['plane_id'] == 42053579
        assert resp.data['total_fuel_consumption'] == 14.0596
        assert resp.data['tank_capacity'] == 8410715800
        assert resp.data['number_of_seats'] == 8

    def test_retrieve_list_airplanes_return_http200(self, client):
        airplanes = AirplaneFactory.create(
            name="<NAM3E>",
            plane_id=420579,
            number_of_seats=8
        )
        airplanes = AirplaneFactory.create(
            name="<NAME1>",
            plane_id=4205579,
            number_of_seats=2
        )
        airplanes = AirplaneFactory.create(
            name="<NAM2E>",
            plane_id=42053579,
            number_of_seats=13
        )

        resp = client.get(f'/api/v1/airplanes/')
        assert resp.status_code == 200
        assert len(resp.data) == 3

    def test_retrieve_airplane_by_plane_id_return_http400(self, client):
        airplanes = AirplaneFactory.create(
            name="<NAME>",
            plane_id=42053579,
            number_of_seats=8
        )
        resp = client.get(f'/api/v1/airplanes/?plane_id={airplanes.plane_id}')
        assert resp.status_code == 200
        assert resp.data[0]['base_fuel_consumption'] == 14.0436
        assert resp.data[0]['flight_duration'] is not None
        assert resp.data[0]['name'] == "<NAME>"
        assert resp.data[0]['plane_id'] == 42053579
        assert resp.data[0]['total_fuel_consumption'] == 14.0596
        assert resp.data[0]['tank_capacity'] == 8410715800
        assert resp.data[0]['number_of_seats'] == 8
