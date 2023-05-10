from django.db.models import Subquery, OuterRef
from django.views.generic import ListView
from cages.models import Cage, CageAnalytical


class CageListView(ListView):
    model = Cage
    paginate_by = 10
    template_name = 'cages/list_cages.html'

    # def get_queryset(self):
    #     latest_statuses = CageAnalytical.objects.filter(cage_id=OuterRef('pk')).values('status').first()
    #     queryset = Cage.objects.annotate(latest_status=Subquery(latest_statuses))
    #     return queryset