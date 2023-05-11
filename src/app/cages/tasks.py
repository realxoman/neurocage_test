from neurotest.celery import app
from cages.models import Cage, CageAnalytical
import requests
from django.conf import settings

@app.task
def cage_health_checker(cage):
    request_health = requests.get(f"{settings.HEALTH_CHECKER_URL}{cage.id}")
    request_health_result = request_health.json()

    cage_analytical = CageAnalytical(
        cage=cage,
        status=request_health_result.get(),
        time_taken=request_health.elapsed.total_seconds(),
        )
    
    cage_analytical.save()
    return f"Cage Analytical {str(cage)} Created"



@app.task
def auto_cage_health_checker():
    cages = Cage.objects.all()
    for cage in cages:
        cage_health_checker.delay(cage.id)
    return "All Cages has scheduled"