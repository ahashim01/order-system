from abc import ABC, abstractmethod


class BaseMapper(ABC):
    @abstractmethod
    def parse_store(self, data):
        pass

    @abstractmethod
    def parse_customer(self, data):
        pass

    @abstractmethod
    def parse_order(self, data):
        pass


class SallaMapper(BaseMapper):
    def parse_store(self, data):
        return {
            "id": str(data["merchant"]),
            "title": data.get("store", {}).get("name", {}).get("ar", "Unknown"),
            "url": data.get("urls", {}).get("admin", ""),
            "email": data.get("store", {}).get("user_email", ""),
            "logo": data.get("store", {}).get("avatar", ""),
        }

    def parse_customer(self, data):
        customer = data["data"]["customer"]
        return {
            "id": str(customer["id"]),
            "name": f"{customer.get('first_name', '')} {customer.get('last_name', '')}",
            "email": customer.get("email", ""),
            "mobile": customer.get("mobile", ""),
            "address": f"{customer.get('country', '')}, {customer.get('city', '')}",
            "gender": customer.get("gender", ""),
        }

    def parse_order(self, data):
        order_data = data["data"]
        return {
            "id": str(order_data["store"]["store_id"]),
            "date": order_data["date"]["date"],
            "total_price": order_data["amounts"]["total"]["amount"],
            "currency": order_data.get("currency", "SAR"),
        }


class ZidMapper(BaseMapper):
    def parse_store(self, data):
        return {
            "id": str(data["store_id"]),
            "title": data.get("store_name", "Unknown"),
            "url": data.get("store_url", ""),
        }

    def parse_customer(self, data):
        customer = data["customer"]
        return {
            "id": str(customer["id"]),
            "name": customer.get("name", ""),
            "email": customer.get("email", ""),
            "mobile": customer.get("mobile", ""),
            "address": data.get("shipping", {}).get("address", {}).get("formatted_address", ""),
        }

    def parse_order(self, data):
        return {
            "id": str(data["id"]),
            "date": data.get("updated_at", ""),
            "total_price": data["transaction_amount"],
            "currency": data.get("currency", "SAR"),
        }


class MapperResolver:
    _mappers = {"salla": SallaMapper, "zid": ZidMapper}

    @staticmethod
    def get_mapper(store_type) -> BaseMapper:
        mapper = MapperResolver._mappers.get(store_type.lower())
        if not mapper:
            raise ValueError(f"Unsupported store type: {store_type}")
        return mapper()
