from django_filters import FilterSet
from .models import Taxi


class TaxiFilter (FilterSet):
    class Meta:
        model = Taxi
        fields = ['type', 'model']