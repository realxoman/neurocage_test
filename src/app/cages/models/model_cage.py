from django.db import models
from django.utils.translation import gettext_lazy as _
from cages.models.model_cage_analytical import CageAnalytical

class Cage(models.Model):
    class Meta:
        verbose_name = _('Cage')
        verbose_name_plural = _('Cages')
        ordering = ('id', )

    label       = models.CharField(_("Label"), max_length=256)
    color       = models.CharField(_("Cage Color"), max_length=50, null=True, blank=True)
    material    = models.CharField(_("Cage Material"), max_length=50, null=True, blank=True)
    version     = models.CharField(_("Cage Version"), max_length=10, null=True, blank=True)
    dimensions  = models.CharField(_("Cage Dimensions"), max_length=50, null=True, blank=True)
    created_at  = models.DateTimeField(_("Cage Creation Time"), auto_now_add=True)

    def __str__(self):
        return f"{self.label}"
    
    @property
    def last_status(self):
        last_status = CageAnalytical.objects.filter(cage=self).order_by('-created_at').only('status').first()
        return last_status
    
    # def save(
    #         self, force_insert=False, force_update=False, using=None, update_fields=None
    #     ):
    #     flag = False
    #     if self.id:
    #         flag = True

    #     data = super().save(force_insert,force_update,using,update_fields)

    #     if flag:
    #         pass

    #     return data
