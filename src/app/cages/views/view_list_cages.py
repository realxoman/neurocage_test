from django.db.models import Subquery, OuterRef, F
from django.views.generic import ListView
from cages.models import Cage, CageAnalytical


class CageListView(ListView):
    model = Cage
    context_object_name = 'cages'
    paginate_by = 10
    template_name = 'cages/list_cages.html'
