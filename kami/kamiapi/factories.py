from factory.django import DjangoModelFactory

from kamiapi.models import Airplane


class AirplaneFactory(DjangoModelFactory):

    class Meta:
        model= Airplane