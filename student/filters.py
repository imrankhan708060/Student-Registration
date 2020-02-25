import django_filters
from . models import Student


class NameFilter(django_filters.FilterSet):

    class Meta:
        model=Student
        fields={
            "First_name":['icontains'],
        }