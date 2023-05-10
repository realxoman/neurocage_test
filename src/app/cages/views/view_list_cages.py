from django.db.models import Subquery, OuterRef, F
from django.views.generic import ListView
from cages.models import Cage, CageAnalytical


class CageListView(ListView):
    model = Cage
    context_object_name = 'cages'
    paginate_by = 10
    template_name = 'cages/list_cages.html'

    def get_queryset(self):
        latest_statuses = CageAnalytical.objects.filter(cage_id=OuterRef('pk')).order_by('-created_at').values('status')[:1]
        queryset = Cage.objects.annotate(latest_status=Subquery(latest_statuses))
        return queryset