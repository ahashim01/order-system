from stores.tasks import process_order_task
from stores.utils import parse_json_request
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def stores_webhooks(request, store_type_name):
    # you can use the store_type_pk to get the store, or store it in cahce or use a pre-defined store_type json.
    # you can chane the store_type_name to store_type_pk if you want to use it instead of the name.
    # you can remove it if you don't need it, and use pre-defined url paths.

    # Note that you need to respond with a 200 status code to the webhook request, the max time to respond is 5 seconds.

    # store_type = get_object_or_404(StoreType, name=store_type_name)
    try:
        # Validate request method
        if request.method != "POST":
            return JsonResponse({"error": "Invalid request method."}, status=405)

        # Parse and validate JSON body
        data = parse_json_request(request.body)

        # Trigger Celery task asynchronously
        process_order_task.delay(data, store_type_name)

        return JsonResponse({"status": "success"}, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
