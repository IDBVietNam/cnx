import django_filters

from .models import TelesalesV2


class TelesalesV2Filter(django_filters.FilterSet):
    call_status = django_filters.CharFilter(lookup_expr="iexact")
    call_reason = django_filters.CharFilter(lookup_expr="icontains")
    call_result = django_filters.CharFilter(lookup_expr="icontains")
    mobile_number = django_filters.CharFilter(lookup_expr="icontains")
    id_card_number = django_filters.CharFilter(lookup_expr="icontains")
    call_id = django_filters.CharFilter(lookup_expr="icontains")
    contract_number = django_filters.CharFilter(lookup_expr="icontains")
    contract_info = django_filters.CharFilter(lookup_expr="icontains")
    assigned_agent = django_filters.CharFilter(lookup_expr="icontains")
    from_date = django_filters.DateFilter(
        field_name="scheduled_time", lookup_expr="gte", label="Start Date"
    )
    to_date = django_filters.DateFilter(
        field_name="scheduled_time", lookup_expr="lte", label="End Date"
    )

    class Meta:
        model = TelesalesV2
        fields = [
            "call_status",
            "call_reason",
            "call_result",
            "mobile_number",
            "id_card_number",
            "contract_number",
            "contract_info",
            "assigned_agent",
            "from_date",
            "to_date",
        ]
