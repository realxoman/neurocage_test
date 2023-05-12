from neurotest.celery import app
from cages.models import Cage, CageAnalytical
import requests
from django.conf import settings
from celery import shared_task

@app.task
def cage_health_checker(cage):
    request_health = requests.get(f"{settings.HEALTH_CHECKER_URL}{cage}/")
    request_health_result = request_health.json()
    my_status = request_health_result.get('status')
    if type(my_status) != type(int()):
        my_status = 0

    cage_analytical = CageAnalytical(
        cage_id=cage,
        status=my_status,
        time_taken=request_health.elapsed.total_seconds(),
        )
    
    cage_analytical.save()
    return f"Cage Analytical {str(cage)} Created"



@shared_task
def auto_cage_health_checker():
    cages = Cage.objects.all()
    for cage in cages:
        cage_health_checker.delay(cage.id)
    return "All Cages has scheduled"