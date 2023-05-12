from django.test import TestCase
from cages.models import Cage
from cages.forms import FormCage

class TestFormCage(TestCase):
    def test_valid_form(self):
        cage = Cage.objects.create(label='Cage99', color='Blue', material='Iron', version='v1.2', dimensions='12x15x18')
        data = {'label': cage.label, 'color': cage.color, 'material': cage.material, 'version': cage.version, 'dimensions': cage.dimensions}
        form = FormCage(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        cage = Cage.objects.create(label='Cage99', color='Blue', material='Iron', version='v1.2333333333333333333333333333333', dimensions='12x15x18')
        data = {'label': cage.label, 'color': cage.color, 'material': cage.material, 'version': cage.version, 'dimensions': cage.dimensions}
        form = FormCage(data=data)
        self.assertFalse(form.is_valid())