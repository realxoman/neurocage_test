from django.test import TestCase
from django.urls import reverse, resolve
from cages.views import CageCreateView, CageDetailView, CageListView
from cages.models import Cage


class TestCageView(TestCase):
    def create_cage(self):
        return Cage.objects.create(label='Cage99', color='Blue', material='Iron', version='v1.2', dimensions='12x15x18')

    def test_create_cage(self):
        self.client.post('/cages/create/', {'label':'Cage99', 'color':'Blue', 'material':'Iron', 'version':'v1.2', 'dimensions':'12x15x18'})
        self.assertEqual(Cage.objects.last().label, "Cage99")
        

    def test_detail_cage(self):
        cage = self.create_cage()
        response  = self.client.get(reverse('cages:detail', kwargs={'pk': cage.pk}))
        self.assertContains(response, "Iron")

    def test_list_cages(self):
        cage = self.create_cage()
        response = self.client.get(reverse('cages:list'))
        self.assertIn(cage, response.context['cages'])
