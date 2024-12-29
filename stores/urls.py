from django.urls import path
from . import views
urlpatterns = [
    path(
        'webhooks/<str:store_type_name>/', 
        views.stores_webhooks, 
        name='stores_webhooks'
        ),
]
