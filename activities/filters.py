import django_filters

from .models import Activities


class ActivitiesFilter(django_filters.FilterSet):
    contract_number = django_filters.CharFilter(lookup_expr="icontains")
    action_code = django_filters.CharFilter(lookup_expr="icontains")
    contacted_person = django_filters.CharFilter(lookup_expr="icontains")
    from_date = django_filters.DateFilter(
        field_name="date_created", lookup_expr="gte", label="Start Date"
    )
    to_date = django_filters.DateFilter(
        field_name="date_created", lookup_expr="lte", label="End Date"
    )

    class Meta:
        model = Activities
        fields = [
            "contract_number",
            "action_code",
            "contacted_person",
            "from_date",
            "to_date",
        ]
