from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import transaction

@csrf_exempt
def stores_webhooks(request, store_type_name):
    # you can use the store_type_pk to get the store, or store it in cahce or use a pre-defined store_type json.
    # you can chane the store_type_name to store_type_pk if you want to use it instead of the name.
    # you can remove it if you don't need it, and use pre-defined url paths.

    # Note that you need to respond with a 200 status code to the webhook request, the max time to respond is 5 seconds.

    # store_type = get_object_or_404(StoreType, name=store_type_name)
    body = request.body.decode('utf-8')
    json_body = json.loads(body)
    
    # LOGIC HERE.
    return HttpResponse('ok')
