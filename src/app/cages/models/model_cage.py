from django.db import models
from django.utils.translation import gettext_lazy as _


class Cage(models.Model):
    class Meta:
        verbose_name = _('Cage')
        verbose_name_plural = _('Cages')
        ordering = ('-id', )

    label       = models.CharField(_("Label"), max_length=256)
    color       = models.CharField(_("Cage Colour"), max_length=50, null=True, blank=True)
    material    = models.CharField(_("Cage Material"), max_length=50, null=True, blank=True)
    version     = models.CharField(_("Cage Version"), max_length=10, null=True, blank=True)
    dimensions  = models.CharField(_("Cage Dimensions"), max_length=50, null=True, blank=True)