from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "use_case_project.settings")

app = Celery("use_case_project")


app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


# example task for testing purposes
@app.task
def add(x, y):
    return x + y
