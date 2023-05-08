from django.urls import reverse_lazy
from django.views.generic import CreateView
from cages.models import Cage


class CageCreateView(CreateView):
    model = Cage
    fields = "__all__"
    success_url = reverse_lazy('cages:list_cages')
    template_name = 'create_cage'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response