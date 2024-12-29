from celery import shared_task
from .services import OrderProcessingService
from django.db import transaction


@shared_task(bind=True, max_retries=3)
def process_order_task(self, data, store_type_name):
    try:
        with transaction.atomic():
            service = OrderProcessingService(data, store_type_name)
            service.process_data()
            return {"status": "success", "store_type_name": store_type_name}

    except Exception as e:
        # Retry the task in case of transient errors
        raise self.retry(exc=e, countdown=5)


# test task
@shared_task
def test_task():
    print("Task executed successfully.")
