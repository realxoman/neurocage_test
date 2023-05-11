from django.test import TestCase
from cages.models import Cage, CageAnalytical

class TestCageModel(TestCase):
    def create_cage(self):
        return Cage.objects.create(label='Cage99', color='Blue', material='Iron', version='v1.2', dimensions='12x15x18')

    def test_cage_creation(self):
        cage = self.create_cage()
        self.assertTrue(isinstance(cage, Cage))
        self.assertEqual(cage.__str__(), cage.label)


class TestCageAnalyticalModel(TestCase):
    def create_cage_analytical(self):
        cage = Cage.objects.create(label='Cage99', color='Blue', material='Iron', version='v1.2', dimensions='12x15x18')
        return CageAnalytical.objects.create(cage=cage, status=1, time_taken=2.500)

    def test_cage_analytical_creation(self):
        cage_analytical = self.create_cage_analytical()
        self.assertTrue(isinstance(cage_analytical, CageAnalytical))
        self.assertEqual(cage_analytical.__str__(), f"{cage_analytical.cage} - {cage_analytical.created_at}")