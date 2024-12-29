from django.core.cache import cache
from django.core.exceptions import ValidationError
import json
from .models import StoreTypes


def parse_json_request(body: bytes):
    """
    Parses and validates JSON data from the request body.

    Args:
        body (bytes): Raw request body.

    Returns:
        dict: Parsed JSON data.

    Raises:
        ValidationError: If JSON is invalid or cannot be decoded.
    """
    try:
        data = json.loads(body.decode("utf-8"))
        if not isinstance(data, dict):
            raise ValidationError("Invalid JSON format, expected an object.")
        return data
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise ValidationError("Invalid JSON data provided.")


def get_store_type_by_name(store_name: str) -> StoreTypes:
    """
    Retrieves a store type by name, using caching for faster lookups.

    Args:
        store_name (str): Name of the store type.

    Returns:
        StoreTypes instance.

    Raises:
        ValidationError: If store type does not exist.
    """
    store_type = cache.get(store_name)
    if store_type is None:
        try:
            store_type = StoreTypes.objects.get(name=store_name)
        except StoreTypes.DoesNotExist:
            raise ValidationError(f"Store type '{store_name}' does not exist.")
        cache.set(store_name, store_type, timeout=60 * 60 * 24)  # Cache for 24 hours
    return store_type
