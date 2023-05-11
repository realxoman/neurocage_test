from django.test import TestCase
from django.urls import reverse, resolve
from cages.views import CageCreateView, CageDetailView, CageListView
from cages.models import Cage


class TestURLCage(TestCase):
    def test_create_cage(self):
        url = reverse('cages:create')
        self.assertEqual(resolve(url).func.view_class, CageCreateView)
        self.assertNotEqual(resolve(url).func.view_class, CageListView)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_detail_cage(self):
        Cage.objects.create(label='Cage99', color='Blue', material='Iron', version='v1.2', dimensions='12x15x18')
        url = reverse('cages:detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, CageDetailView)
        self.assertNotEqual(resolve(url).func.view_class, CageCreateView)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_list_cages(self):
        url = reverse('cages:list')
        self.assertEqual(resolve(url).func.view_class, CageListView)
        self.assertNotEqual(resolve(url).func.view_class, CageDetailView)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)