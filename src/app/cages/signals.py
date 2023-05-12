from django.db.models.signals import post_save
from django.dispatch import receiver
from cages.models import Cage
from cages.tasks import cage_health_checker

@receiver(post_save, sender=Cage)
def send_user_email(sender, instance, created, *args, **kwargs):
    if created:
        cage_health_checker.delay(instance.id)
