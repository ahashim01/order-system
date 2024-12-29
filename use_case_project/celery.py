from celery import Celery
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "use_case_project.settings")

app = Celery("use_case_project")


app.config_from_object(settings, namespace="CELERY")

app.conf.update(
    broker_url=settings.CELERY_BROKER_URL,
    result_backend=settings.CELERY_RESULT_BACKEND,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    broker_connection_retry_on_startup=True,
    beat_scheduler="django_celery_beat.schedulers:DatabaseScheduler",
)

app.autodiscover_tasks()


# example task for testing purposes
@app.task
def add(x, y):
    return x + y
