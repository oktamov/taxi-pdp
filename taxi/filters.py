import django_filters

from .models import Driver


class DriverFilter(django_filters.FilterSet):
    from_place = django_filters.CharFilter(field_name="from_place", lookup_expr="icontains")
    to_place = django_filters.CharFilter(field_name="to_place", lookup_expr="icontains")

    class Meta:
        model = Driver
        fields = ["from_place", "to_place", "date"]

