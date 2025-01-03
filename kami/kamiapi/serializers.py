from rest_framework import serializers
from kamiapi.models import Airplane
from kamiapi.business_logic.services import AirplaneService


class AirplaneInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250, allow_null=False)
    plane_id = serializers.IntegerField(default=0, allow_null=False)
    number_of_seats = serializers.IntegerField(default=0, allow_null=False)


class AirplaneSerializer(serializers.ModelSerializer):
    tank_capacity = serializers.SerializerMethodField(read_only=True)
    base_fuel_consumption = serializers.SerializerMethodField(read_only=True)
    total_fuel_consumption = serializers.SerializerMethodField(read_only=True)
    flight_duration = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_tank_capacity(obj):
        return  AirplaneService(obj).get_plane_tank_capacity()

    @staticmethod
    def get_base_fuel_consumption(obj):
        return AirplaneService(obj).get_plane_fuel_consumption()

    @staticmethod
    def get_total_fuel_consumption(obj):
        return AirplaneService(obj).total_consumption()

    @staticmethod
    def get_flight_duration(obj):
        return AirplaneService(obj).calculate_flight_duration()

    class Meta:
        model = Airplane
        fields = [
            "name"
            ,"plane_id",
            "number_of_seats",
            "tank_capacity",
            "total_fuel_consumption",
            "base_fuel_consumption",
            "flight_duration",
            "created_at",
            "updated_at"
        ]
