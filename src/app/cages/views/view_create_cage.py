from django.urls import reverse_lazy
from django.views.generic import CreateView
from cages.models import Cage
from cages.forms import FormCage

class CageCreateView(CreateView):
    model = Cage
    form_class = FormCage
    success_url = reverse_lazy('cages:list')
    template_name = 'cages/create_cage.html'
    