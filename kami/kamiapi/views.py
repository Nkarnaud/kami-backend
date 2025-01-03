from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from kamiapi.business_logic.entities import PlaneEntity
from kamiapi.models import Airplane
from kamiapi.serializers import AirplaneSerializer, AirplaneInputSerializer
from kamiapi.business_logic.services import AirplaneHandler


class AirplaneViewSet(
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Airplane.objects.order_by('-created_at')
    serializer_class = AirplaneSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return AirplaneInputSerializer
        return self.serializer_class

    def create(self, request) -> Response:
        ser = self.get_serializer(data=request.data)
        if not ser.is_valid():
            return Response({'message': 'Bad Request', 'error': ser.errors}, status=status.HTTP_400_BAD_REQUEST)
        data = ser.data
        plane_entity = PlaneEntity(**data)
        airplane_handler = AirplaneHandler(plane_entity)
        airplane = airplane_handler.create_plane()
        return Response(AirplaneSerializer(airplane).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk) -> Response:
        return super().retrieve(request, pk)

    def list(self, request):
        return super().list(request)

    @action(['GET'], detail=False)
    def get_plane(self, request):
        query_params = request.query_params.get("plane_id")
        if not query_params.isnumeric():
            return Response({"message": "Please input only an integer"}, status=status.HTTP_400_BAD_REQUEST)
        airplane = AirplaneHandler.find_by_id(query_params)
        if not airplane:
            return Response({"message": "No Plan found!"}, status=status.HTTP_400_BAD_REQUEST)
        ser = AirplaneSerializer(airplane)
        return Response(ser.data, status=status.HTTP_200_OK)
