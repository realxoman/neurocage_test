from django.db import models
from django.utils.translation import gettext_lazy as _

class CageAnalytical(models.Model):
    class Meta:
        verbose_name = _('Cage Analytical')
        verbose_name_plural = _('Cage Analytics')
        ordering = ('-created_at', )

    class Status(models.IntegerChoices):
        Bad     = 1, _("Bad")
        Ok      = 2, _("Ok")
        Perfect = 3, _("Perfect")

    cage_id     = models.ForeignKey("cages.Cage", verbose_name=_("Cage Id"), on_delete=models.CASCADE)
    status      = models.IntegerField(_("Cage Status"), choices=Status.choices)
    created_at  = models.DateTimeField(_("Cage Creation Time"), auto_now_add=True)