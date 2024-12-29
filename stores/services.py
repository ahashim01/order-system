from django.db import transaction
from .mappers import MapperResolver
from .models import Stores, Customers, Orders
from .utils import get_store_type_by_name
from django.db.utils import IntegrityError


class OrderProcessingService:
    def __init__(self, data, store_type_name):
        self.data = data
        self.store_type_name = store_type_name
        self.store_type = None

    def _load_store_type(self):
        """Loads the store type using caching."""
        self.store_type = get_store_type_by_name(self.store_type_name)

    def _process_store_data(self):
        """Processes store data."""
        store_data = self.mapper.parse_store(self.data)
        try:
            # use update_or_create to prevent duplicates,
            # and update the store data if it already exists.
            store, _ = Stores.objects.update_or_create(
                custom_identifier=store_data["id"],
                store_type=self.store_type,
                defaults={
                    "title": store_data.get("title", ""),
                    "url": store_data.get("url", ""),
                    "email": store_data.get("email", ""),
                    "logo": store_data.get("logo", ""),
                },
            )
            return store
        except Exception as e:
            # Handle exceptions gracefully to continue processing other stores.
            # Log the error for debugging purposes.
            print(f"Error processing store: {e}")
            return None

    def _process_customer_data(self, store):
        """Processes customer data and links to the store."""
        try:
            customer_data = self.mapper.parse_customer(self.data)
            customer, _ = Customers.objects.update_or_create(
                store_type=self.store_type,
                store_type_identifier=str(customer_data["id"]),
                defaults={
                    "name": customer_data.get("name", ""),
                    "email": customer_data.get("email", ""),
                    "mobile": customer_data.get("mobile", ""),
                    "address": customer_data.get("address", ""),
                    "gender": customer_data.get("gender", ""),
                },
            )
            # Add M2M link
            customer.stores.add(store)
            return customer
        except Exception as e:
            # Handle exceptions gracefully to continue processing other stores.
            # Log the error for debugging purposes.
            print(f"Error processing customer: {e}")
            return None

    def _process_order_data(self, store, customer):
        """Processes order data."""
        order_data = self.mapper.parse_order(self.data)
        try:
            order, _ = Orders.objects.update_or_create(
                store=store,
                order_id=str(order_data["id"]),
                defaults={
                    "customer": customer,
                    "order_date": order_data["date"],
                    "total_price": order_data["total_price"],
                    "currency": order_data["currency"],
                },
            )
            return order
        except Exception:
            # Handle exceptions gracefully to continue processing other stores.
            # Log the error for debugging purposes.
            return None

    def process_data(self):
        self._load_store_type()
        self.mapper = MapperResolver.get_mapper(self.store_type_name)
        try:
            with transaction.atomic():
                store = self._process_store_data()
                if store:
                    customer = self._process_customer_data(store)
                    if customer:
                        return self._process_order_data(store, customer)
                return None
        except IntegrityError:
            # Handle integrity errors gracefully
            return None
