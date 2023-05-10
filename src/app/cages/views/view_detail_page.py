from django.views.generic import DetailView
from django.db.models import Count
from cages.models import Cage, CageAnalytical
from django.utils import timezone


class CageDetailView(DetailView):
    model = Cage
    template_name = 'cages/detail_cage.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     cage_analytical_today = CageAnalytical.objects.filter(
    #         cage_id=self.object,
    #         created_at__date=timezone.now().date()
    #     )
    #     context['cage_analytical_today'] = cage_analytical_today
    #     context['cage_functionality'] = cage_analytical_today.annotate(count=Count('id')).order_by('-count').distinct(
    #         'cage_id').values('status')
    #     return context