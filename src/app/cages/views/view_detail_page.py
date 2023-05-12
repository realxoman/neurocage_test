from django.views.generic import DetailView
from django.db.models import Count
from cages.models import Cage, CageAnalytical
from django.utils import timezone


class CageDetailView(DetailView):
    model = Cage
    context_object_name = "cage"
    template_name = 'cages/detail_cage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cage_analytical_today = CageAnalytical.objects.filter(
            cage=self.object.id,
            created_at__date=timezone.now().date()
        )
        if cage_analytical_today.count() >= 1:
            context['cage_analytical_today'] = cage_analytical_today
            perfects_count = cage_analytical_today.filter(status=3).count()
            context['functionality_percentages'] = int((perfects_count/len(cage_analytical_today)) * 100)
        return context