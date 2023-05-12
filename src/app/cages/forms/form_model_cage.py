from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from cages.models import Cage

class FormCage(ModelForm):
    
    class Meta:
        model = Cage
        fields = ("label", "color", "material", "version", "dimensions")
        labels = {
            "label"         : _("Cage Label"),
            "color"         : _("Cage Colour"),
            "material"      : _("Cage Material"),
            "version"       : _("Cage Version"),
            "dimensions"    : _("Cage Dimensions")
        }
        