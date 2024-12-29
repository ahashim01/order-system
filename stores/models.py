from django.db import models


class ModelBase(models.Model):
    """
    Represents a base model with created_at and updated_at fields.

    Attributes:
        created_at (DateTimeField): The date and time when the invoice was created.
        updated_at (DateTimeField): The date and time when the invoice was last updated.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StoreTypes(ModelBase):
    """
    Represents a type of store.

    Example:
        SALLA, ZID, SHOPIFY, etc.

    Attributes:
        name (CharField): The name of the store type.
        logo (URLField): The logo of the store.
        url (URLField): The URL of the store.
    """

    STORE_TYPES = [("salla", "Salla"), ("zid", "Zid"), ("shopify", "Shopify")]
    name = models.CharField(max_length=255, choices=STORE_TYPES)
    logo = models.URLField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Stores(ModelBase):
    """
    Represents a store 'merchant' on zalla or zid'.

    Attributes:
        custom_identifier (TextField): The custom identifier for the store, (eg, merchent store id on salla, etc).
        auth (ForeignKey): The foreign key to the Auth model.
        store_type (ForeignKey): The foreign key to the store_types model [SALLA - ZID - SHOPIFY].
        url (CharField): The URL of the store (optional).
        title (CharField): The title of the store (optional).
        logo (CharField): The logo of the store (optional).
        created_at (DateTimeField): The date and time when the store was created.
        updated_at (DateTimeField): The date and time when the store was last updated.
    """

    custom_identifier = models.CharField(max_length=255)
    shipping_tax_status = models.BooleanField(default=False, null=True, blank=True)
    store_type = models.ForeignKey("StoreTypes", models.CASCADE, related_name="stores")
    url = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    logo = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = [["custom_identifier", "store_type"]]


class Orders(ModelBase):
    """
    Represents orders in the stores.
    Attributes:
        store (ForeignKey): The store associated with the order.
        order_id (TextField): The ID of the order.
        order_id_extra (TextField, optional): Extra ID of the order (can be blank or null).
        customer (ForeignKey): The customer associated with the order.
        order_date (DateTimeField): The date of the order.
        total_price (FloatField): The total price of the order.
        payment_method (ForeignKey): The payment method used for the order.
        shipping_method (ForeignKey, optional): The shipping method used for the order (can be null).
        order_type (CharField): The type of the order (sale or buy).
        exchange_rate_to_sar (FloatField): The exchange rate to SAR (default is 1.0).
        currency (CharField): The currency used for the order (default is SAR).
    """

    store = models.ForeignKey("Stores", models.CASCADE, related_name="orders")

    order_id = models.TextField()
    order_id_extra = models.TextField(blank=True, null=True)

    customer = models.ForeignKey("Customers", models.PROTECT, related_name="orders")
    order_date = models.DateTimeField()
    total_price = models.FloatField()

    exchange_rate_to_sar = models.FloatField(default=1.0)
    currency = models.CharField(max_length=255, default="SAR")

    class Meta:
        unique_together = [["order_id", "store"]]  # prevent duplicate orders in the same store


class Products(ModelBase):

    store = models.ForeignKey("Stores", models.CASCADE, related_name="products")
    name_ar = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    description = models.JSONField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    quantity = models.PositiveBigIntegerField()


class Customers(ModelBase):
    """
    Represents a customer in the store.

    Attributes:

        store_type (TextField): The custom identifier for the customer based on the store type [salla, zid, etc.].

        stores (ManyToManyField): the stores associated with the customer. [user has bought from these stores]
        store_type (ForeignKey): The foreign key to the store_type model [where the customer was created from].
        name (CharField): The name of the customer.
        email (EmailField): The email address of the customer (optional).
        mobile (PhoneField): The mobile number of the customer (optional).
        address (TextField): The address of the customer (optional)
        gender (CharField): The gender of the customer (optional)

        created_at (DateTimeField): The date and time when the object was created.
        updated_at (DateTimeField): The date and time when the object was last updated.

    """

    GENDERS = (("male", "male"), ("female", "female"))

    store_type = models.ForeignKey(StoreTypes, models.PROTECT, related_name="customers")
    store_type_identifier = models.CharField(max_length=255)

    stores = models.ManyToManyField(Stores, related_name="customers", blank=True)

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=GENDERS, max_length=45, blank=True, null=True)

    class Meta:
        unique_together = [["store_type", "store_type_identifier"]]  # prevent duplicate customers in the same store
